from email.mime import audio
import  moviepy.editor
from tkinter.filedialog import *

video = askopenfilename()
video = moviepy.editor.VideoFileClip(video)
theAudio = video.audio

theAudio.write_audiofile("sample.mp3")
print("Completed")
