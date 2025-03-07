import moviepy.editor
from tkinter.filedialog import *

from moviepy import VideoFileClip
from numpy import clip

video = askopenfilename();
clip = VideoFileClip(video)
clip.write_gif("mygif.gif", fps=10)