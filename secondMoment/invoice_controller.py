from configdb import get_connection

def add_invoice(date, id, price, balance):
    #doing id validation!!!
    myConnection = get_connection()
    with myConnection.cursor() as cursor:
        cursor.execute("INSERT INTO invoice (date, id, price, balance) VALUES (%s, %s, %s, %s)",(date, id, price, balance))
    myConnection.commit()
    myConnection.close()

def update_invoice(date, id, price, balance, number):
    myConnection = get_connection()
    with myConnection.cursor() as cursor:
        cursor.execute("UPDATE invoice SET date=%s, id=%s, price=%s, balance=%s WHERE number=%s",(date, id, price, balance, number))
    myConnection.commit()
    myConnection.close()

def delete_invoice(number):
    myConnection = get_connection()
    with myConnection.cursor() as cursor:
        cursor.execute("DELETE from invoice WHERE number=%s",(number))
    myConnection.commit()
    myConnection.close()

def get_invoice():
    myConnection = get_connection()
    invoices=[]
    with myConnection.cursor() as cursor:
        cursor.execute("SELECT number, date, id, price, balance FROM invoice")
        invoices=cursor.fetchall()
    myConnection.close()
    return invoices

def get_invoice_number(number):
    myConnection=get_connection()
    invoice=None
    with myConnection.cursor() as cursor:
        cursor.execute("SELECT id, date, price, balance, number FROM invoice WHERE number=%s",(number))
        invoice=cursor.fetchone()
    myConnection.close()
    return invoice
