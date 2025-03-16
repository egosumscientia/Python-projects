from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from typing import List
import sqlite3
import jwt
import pandas as pd
import matplotlib.pyplot as plt
import io
import base64
from sklearn.linear_model import LinearRegression
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from fastapi.responses import JSONResponse
from datetime import datetime, timezone, timedelta


app = FastAPI()
security = HTTPBearer()
SECRET_KEY = "mysecretkey"


# Database setup
def init_db():
    conn = sqlite3.connect("inventory.db")
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS products (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        category TEXT NOT NULL,
        stock INTEGER NOT NULL
    )
    ''')
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS inventory_movements (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        product_id INTEGER NOT NULL,
        type TEXT NOT NULL CHECK(type IN ('IN', 'OUT')),
        quantity INTEGER NOT NULL,
        timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY(product_id) REFERENCES products(id)
    )
    ''')
    conn.commit()
    conn.close()


init_db()


# Authentication
class UserAuth(BaseModel):
    username: str
    password: str


def create_jwt_token(username: str):
    payload = {
        "sub": username,
        "exp": datetime.now(timezone.utc) + timedelta(hours=1)
    }
    return jwt.encode(payload, SECRET_KEY, algorithm="HS256")


def verify_token(credentials: HTTPAuthorizationCredentials = Depends(security)):
    try:
        payload = jwt.decode(credentials.credentials, SECRET_KEY, algorithms=["HS256"])
        return payload["sub"]
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token expired")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail="Invalid token")


@app.post("/login/")
def login(user: UserAuth):
    if user.username == "admin" and user.password == "password":  # Replace with real authentication
        token = create_jwt_token(user.username)
        return {"access_token": token}
    raise HTTPException(status_code=401, detail="Invalid credentials")


# Pydantic Models
class Product(BaseModel):
    name: str
    category: str
    stock: int


class ProductResponse(Product):
    id: int


class InventoryMovement(BaseModel):
    product_id: int
    type: str  # 'IN' or 'OUT'
    quantity: int


# CRUD Endpoints
@app.post("/products/", response_model=ProductResponse)
def create_product(product: Product, _: str = Depends(verify_token)):
    conn = sqlite3.connect("inventory.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO products (name, category, stock) VALUES (?, ?, ?)",
                   (product.name, product.category, product.stock))
    conn.commit()
    product_id = cursor.lastrowid
    conn.close()
    return {"id": product_id, **product.model_dump()}


@app.get("/products/", response_model=List[ProductResponse])
def get_products(_: str = Depends(verify_token)):
    conn = sqlite3.connect("inventory.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM products")
    products = cursor.fetchall()
    conn.close()
    return [{"id": row[0], "name": row[1], "category": row[2], "stock": row[3]} for row in products]


@app.get("/predict-demand/{product_id}")
def predict_demand(product_id: int, _: str = Depends(verify_token)):
    conn = sqlite3.connect("inventory.db")
    cursor = conn.cursor()
    cursor.execute("SELECT timestamp, quantity FROM inventory_movements WHERE product_id = ? AND type = 'OUT'",
                   (product_id,))
    data = cursor.fetchall()
    conn.close()

    if len(data) < 2:
        raise HTTPException(status_code=400, detail="Not enough data to make a prediction")

    df = pd.DataFrame(data, columns=["timestamp", "quantity"])
    df["timestamp"] = pd.to_datetime(df["timestamp"]).astype(int) // 10 ** 9  # Convert to Unix timestamp
    X = df[["timestamp"]]
    y = df["quantity"]

    model = LinearRegression()
    model.fit(X, y)

    future_timestamp = (datetime.now(timezone.utc).timestamp() + 86400)  # Predict for the next day
    predicted_demand = model.predict([[future_timestamp]])[0]

    # Generate plot
    plt.figure(figsize=(8, 5))
    plt.scatter(X, y, color='blue', label='Historical Sales')
    plt.plot(X, model.predict(X), color='red', label='Regression Line')
    plt.scatter([future_timestamp], [predicted_demand], color='green', marker='x', label='Predicted Demand')
    plt.xlabel('Timestamp')
    plt.ylabel('Quantity Sold')
    plt.legend()
    plt.title(f'Demand Prediction for Product {product_id}')

    # Save the plot as a base64-encoded image
    buf = io.BytesIO()
    plt.savefig(buf, format="png")
    buf.seek(0)
    image_base64 = base64.b64encode(buf.getvalue()).decode("utf-8")
    buf.close()

    return JSONResponse(content={"predicted_demand": max(0, int(predicted_demand)), "plot": image_base64})
