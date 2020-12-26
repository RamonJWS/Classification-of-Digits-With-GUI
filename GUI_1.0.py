import numpy as np
import pandas as pd
import warnings
warnings.filterwarnings("ignore")
import pickle 
from sklearn.model_selection import train_test_split
from sklearn.decomposition import PCA
import tkinter as tk
from tkinter import *
from PIL import ImageGrab, Image

# Initial set up of Variables
width=800
height=600
image_name = "digit.png"
image_size = (28,28)

load_model = pickle.load(open("Classifier_Model_NOPCA.sav", "rb"))

def draw(event):
    python_green = "#000000"
    pen_size = 10
    x1, y1 = ( event.x - pen_size ), ( event.y - pen_size )
    x2, y2 = ( event.x + pen_size ), ( event.y + pen_size )
    draw_canvas.create_oval( x1, y1, x2, y2, fill = python_green )   

def collect_image():   
    # the code below find the x,y position of the top and bottom corner of the draw_canvas
    x = draw_canvas.winfo_rootx() + 5
    y = draw_canvas.winfo_rooty() + 5
    x1 = x + draw_canvas.winfo_width() - 10 
    y1 = y + draw_canvas.winfo_height() - 10
    
    # grab a screen capture of the area specified above.
    ImageGrab.grab(bbox=(x,y,x1,y1)).save(image_name)
    image = np.array(ImageGrab.grab(bbox=(x,y,x1,y1)))
    
    # Call the model image_conversion method
    image_conversion()
    
def image_conversion():
    # Open saved image and convert to 28 by 28 pixels
    image_resize = Image.open(image_name).resize(image_size).convert("L")
    image_resize.save(image_name)
    
    # Reopen now 28 by 28 image and convert into matrix
    image_matrix = np.array(Image.open(image_name))
    
    # Call the prediction method
    prediction(image_matrix)

def prediction(image_matrix):   
    
    for idx, i in enumerate(image_matrix):
        for jdx, j in enumerate(i):
            image_matrix[idx][jdx] = abs(j-255)
    
    batch = image_matrix.reshape(1,784)
    prediction = load_model.predict(batch)[0]
    print_prediction(prediction)
    
def print_prediction(prediction):
    myLabel = Label(frame_output, text=prediction, )
    myLabel.config(font=("Times", 200))
    myLabel.place(relx = 0.2, rely = 0.15, relwidth=0.7, relheight=0.6)

def clear_frame():
    draw_canvas.delete("all")


# Set up GUI Window
root = tk.Tk()

# Create Canvas
canvas = Canvas(root, width=width, heigh=height, bg = "#AFBFF5")
canvas.pack()

# Create Drawing Frame
frame_draw = Frame(root)
frame_draw.place(relx = 0.05, rely = 0.3, relwidth=0.4, relheight=0.53)

# Create Canvas on Drawing Frame
draw_canvas = Canvas(frame_draw, bg = "#ffffff")
draw_canvas.place(relx = 0, rely = 0, relwidth = 1, relheight = 1)
draw_canvas.bind( "<B1-Motion>", draw)

# Create Output Frame
frame_output = Frame(root)
frame_output.place(relx = 0.55, rely = 0.3, relwidth=0.4, relheight=0.53)

# Button for Classification
classify_button = Button(root, text = "Classify", command = collect_image, bg = "#D2D2D2")
classify_button.place(relx = 0.05, rely = 0.2, relwidth=0.2, relheight=0.1)

# Button to Clear
clear_button = Button(root, text = "Clear", command = clear_frame, bg = "#D2D2D2")
clear_button.place(relx = 0.25, rely = 0.2, relwidth=0.2, relheight=0.1)

# Comment Prediction above output frame
label_prediction = Label(root, text = "Model Prediction", bg = "#D2D2D2")
label_prediction.place(relx = 0.55, rely = 0.2, relwidth=0.4, relheight=0.1)

# Comment title
label_title = Label(root, text = "Classification of Digits using SVC", bg = "#AFBFF5")
label_title.config(font=("Times", 20))
label_title.place(relx = 0.25, rely = 0.05, relwidth=0.5, relheight=0.1)

root.mainloop()