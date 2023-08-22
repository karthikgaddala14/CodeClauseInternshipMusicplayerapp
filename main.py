#importing libraries

import os
from tkinter import *
from tkinter import Tk
from tkinter import filedialog
from pygame import mixer


# Create a GUI window
root = Tk()
root.title("Music Player")
root.geometry("920x600+290+85")
root.configure(background='#212121')
root.resizable(False, False)
mixer.init()i