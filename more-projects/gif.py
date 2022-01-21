from moviepy.editor import VideoFileClip
from tkinter.filedialog import *

from numpy import clip

video = askopenfilename();
clip = VideoFileClip(video)
clip.write_gif("mygif.gif", fps=10)