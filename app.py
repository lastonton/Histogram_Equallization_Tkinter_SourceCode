import tkinter as tk
from tkinter import *
from tkinter.ttk import Label
from PIL import Image, ImageTk
from tkinter import filedialog
import os
import cv2
import scipy
import numpy as np
import imageio.v2 as iio
import seaborn as sns
import pandas as pd
import asyncio
import importlib
import matplotlib as mpl
import matplotlib.pyplot as plt

def resize_image(img, max_size):
    width, height = img.size
    if width > max_size or height > max_size:
        if width > height:
            new_width = max_size
            new_height = int(height * (max_size / width))
        else:
            new_height = max_size
            new_width = int(width * (max_size / height))
        return img.resize((new_width, new_height))
    else:
        return img

def resize_histogram(img):
    width, height = img.size
    if width > 400 or height > 245:
        if width > height:
            new_width = 400
            new_height = 245
        else:
            new_height = 400
            new_width = int(width * (245 / height))
        return img.resize((new_width, new_height))
    else:
        return img

def update_display_frames():
    global image1, new_img
    if image1 is not None:
        new_width, new_height = image1.size
        if new_img is not None:
            new_width2, new_height2 = new_img.size
            if new_width2 > new_width or new_height2 > new_height:
                if new_width2 > new_height2:
                    new_width = min(new_width, 400)
                    new_height = int(new_height2 * (new_width / new_width2))
                else:
                    new_height = min(new_height, 400)
                    new_width = int(new_width2 * (new_height / new_height2))
    f1.config(width=new_width, height=new_height)
    f2.config(width=new_width, height=new_height)
    

def display_result_image(new_img, name):
    new_img = resize_image(new_img, 400)
    result = ImageTk.PhotoImage(new_img)
    lbl2.configure(image=result)
    lbl2.image = result
    lbl2.update_idletasks()
    update_display_frames()
    return new_img

def create_histogram(img):
    assert len(img.shape) == 2 # check grayscale image
    histogram = [0] * 256 # list of intensity frequencies, 256 zero values
    for row in range(img.shape[0]): # traverse by row (y-axis)
        for col in range(img.shape[1]): # traverse by column (x-axis)
            histogram[img[row, col]] += 1
    return histogram
def visualize_histogram(histogram, output='histogram\\histogram.png'):
    hist_data = pd.DataFrame({'intensity': list(range(256)), 'frequency': histogram})
    sns_hist = sns.barplot(x='intensity', y='frequency', data=hist_data, color='blue')
    sns_hist.set(xticks=[]) # hide x ticks
    
    fig = sns_hist.get_figure()
    fig.savefig(output)
    return output

def save_img():
    img = new_img #Whatever the given image is
    file_name = f"{name}.jpg"
    complete_name = os.path.join(os.getcwd()+'\\images', file_name)
    img.save(complete_name) #This adds it to the directory

def showimage():
    global path, image1, new_img
    lbl1.configure(image=None)
    lbl1.image = None
    lbl2.configure(image=None)
    lbl2.image = None
    lbl3.configure(image=None)
    lbl3.image = None
    lbl4.configure(image=None)
    lbl4.image = None
    f_types = [('Jpg Files', '*.jpg'),('PNG Files','*.png')] 
    path = filedialog.askopenfilename(filetypes=f_types)
    img = cv2.imread(path)
    #img = cv2.resize(img, (500,500))
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img_gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    image1 = Image.fromarray(img_gray)
    image1 = resize_image(image1, 400)
    importedimage = ImageTk.PhotoImage(image1)
    lbl1.configure(image=importedimage, width=380)
    lbl1.image=importedimage
    lbl1.update_idletasks()
    slider.configure(state=NORMAL)
    slider.state = NORMAL
    update_display_frames()

def export_histogram():
    importlib.reload(mpl); importlib.reload(plt); importlib.reload(sns)
    sns.reset_orig()
    histogram_before_result = None
    histogram_after_result = None
    histogram = None
    histogram_after_process = None
    hist_img_path = None
    hist_img_path = None
    if os.listdir != 0:
        os.remove('histogram/histogram.png')
        os.remove('histogram/histogram_after.png')
    histogram = create_histogram(img_gray)
    hist_img_path = visualize_histogram(histogram)

    histogram_after_process = create_histogram(im3)
    hist_img_path = visualize_histogram(histogram_after_process,output='histogram\\histogram_after.png')

    histogram_before = Image.open(os.getcwd()+'\\histogram\\histogram.png')
    histogram_after = Image.open(os.getcwd()+'\\histogram\\histogram_after.png')

    histogram_before = resize_histogram(histogram_before)
    histogram_after = resize_histogram(histogram_after)

    histogram_before_result= ImageTk.PhotoImage(histogram_before)
    histogram_after_result= ImageTk.PhotoImage(histogram_after)

    lbl3.configure(image=histogram_before_result, width=380)
    lbl3.image=histogram_before_result
    lbl4.configure(image=histogram_after_result, width=380)
    lbl4.image=histogram_after_result

def showresultimage_Histogram_equalization_using_basic_code():
    global new_img, name, img_gray, im3
    img_gray = None
    im3= None
    img = cv2.imread(path)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img_gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

    iml = np.asarray(img_gray)

    bl = iml.flatten()

    hist, bins = np.histogram(iml, 256, [0,255])

    cdf = hist.cumsum()

    cdf_m = np.ma.masked_equal(cdf, 0)

    num_cdf_m = (cdf_m-cdf_m.min())*255
    den_cdf_m = (cdf_m.max() - cdf_m.min())
    cdf_m = num_cdf_m/den_cdf_m

    cdf = np.ma.filled(cdf_m,0).astype('uint8')

    im2 = cdf[bl]

    im3 = np.reshape(im2, iml.shape)

    new_img = Image.fromarray(im3)

    name = 'picture_after_Histogram_equalization'
    new_img = display_result_image(new_img, name)

def slider_img(event):
    slider = current_value.get()
    global new_img, name, img_gray, im3
    img_gray = None
    im3= None
    img = cv2.imread(path)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img_gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

    iml = np.asarray(img_gray)

    bl = iml.flatten()

    hist, bins = np.histogram(iml, 256, [0,255])

    cdf = hist.cumsum()

    cdf_m = np.ma.masked_equal(cdf, 0)

    num_cdf_m = (cdf_m-cdf_m.min())*slider
    den_cdf_m = (cdf_m.max() - cdf_m.min())
    cdf_m = num_cdf_m/den_cdf_m

    cdf = np.ma.filled(cdf_m,0).astype('uint8')

    im2 = cdf[bl]

    im3 = np.reshape(im2, iml.shape)

    new_img = Image.fromarray(im3)

    name = 'picture_after_Histogram_equalization'
    new_img = display_result_image(new_img, name)

window = tk.Tk()

window.title("Histogram Equalization")
window.geometry("1024x1024+100+100")
window.configure(bg="white")
#source
title = Label(window, text = 'Histogram Equalization', font="arial 14 bold"). place(x=380,y=0)
original = Label(window, text = 'Gray Scale', font="arial 12 bold"). place(x=30,y=360)
result = Label(window, text='Result', font="arial 12 bold").place(x=530, y=360)
before = Label(window, text = 'Before', font="arial 12 bold"). place(x=30,y=630)
after = Label(window, text='After', font="arial 12 bold").place(x=530, y=630)
selectimage = Frame(width=420, height=330, bg="#d6dee5")
selectimage.place(x=10, y=30)
#result
resultimage = Frame(width=420, height=330, bg="#d6dee5")
resultimage.place(x=510, y=30)

f1 = Frame(selectimage, bg="black", width=400, height=300)
f1.place(x=10, y=10)

f2 = Frame(resultimage, bg="black", width=400, height=300)
f2.place(x=10, y=10)

f3 = Frame(window, bg="black", width=400, height=245)
f3.place(x=20, y=380)

f4 = Frame(window, bg="black", width=400, height=245)
f4.place(x=520, y=380)


lbl1 = Label(f1, background="black")
lbl1.place(x=0, y=0)

lbl2 = Label(f2, background="black")
lbl2.place(x=0,y=0)

lbl3 = Label(f3, background="black")
lbl3.place(x=0, y=0)

lbl4 = Label(f4,background="black")
lbl4.place(x=0,y=0)

current_value = tk.IntVar()

Button(window, text="Select image", width=12, height=2, font="arial 14 bold", command=showimage).place(x=10, y=650)
Button(window,text="Run", width=10, height=2, font="arial 14 bold", command=showresultimage_Histogram_equalization_using_basic_code).place(x=170, y=650)
Button(window,text="Export Histogram", width=15, height=2, font="arial 14 bold", command=export_histogram).place(x=320, y=650)
Button(window,text="Save Image", width=15, height=2, font="arial 14 bold", command=save_img).place(x=520, y=650)
slider = Scale(window, from_=0, to=255, orient="horizontal", command=slider_img, variable=current_value, takefocus=255).place(x=900, y=340)


path = None
image1 = None
new_img = None
window.mainloop()