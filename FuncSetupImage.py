import tkinter.filedialog
import cv2
from tkinter import messagebox
import pygetwindow as gw


def check_w():
    print(gw.getWindowsWithTitle('Re-setup image'))


def set_image_story_check_person():
    path = tkinter.filedialog.askopenfilename(filetypes=[("Image File", '.jpg'), ("Image File", '.png')])
    img = cv2.imread(path)
    try:
        cv2.imwrite('./Images/check_personal.png', img)
        messagebox.showinfo(title="Saved", message="The image has been re-setup")
    except cv2.error as e:
        # handle error: empty image
        if e.err == "!_img.empty()":
            messagebox.showerror(title="No Image", message="Error: Image hasn't been choose")
        else:
            # inspect error object
            print(e)
            for k in dir(e):
                if k[0:2] != "__":
                    print("e.%s = %s" % (k, getattr(e, k)))


def set_image_logedin():
    path = tkinter.filedialog.askopenfilename(filetypes=[("Image File", '.jpg'), ("Image File", '.png')])
    img = cv2.imread(path)
    try:
        cv2.imwrite('./Images/logedin.png', img)
        messagebox.showinfo(title="Saved", message="The image has been re-setup")
    except cv2.error as e:
        # handle error: empty image
        if e.err == "!_img.empty()":
            messagebox.showerror(title="No Image", message="Error: Image hasn't been choose")
        else:
            # inspect error object
            print(e)
            for k in dir(e):
                if k[0:2] != "__":
                    print("e.%s = %s" % (k, getattr(e, k)))


def set_image_notstoreinfo():
    path = tkinter.filedialog.askopenfilename(filetypes=[("Image File", '.jpg'), ("Image File", '.png')])
    img = cv2.imread(path)
    try:
        cv2.imwrite('./Images/notstoreinfo.png', img)
        messagebox.showinfo(title="Saved", message="The image has been re-setup")
    except cv2.error as e:
        # handle error: empty image
        if e.err == "!_img.empty()":
            messagebox.showerror(title="No Image", message="Error: Image hasn't been choose")
        else:
            # inspect error object
            print(e)
            for k in dir(e):
                if k[0:2] != "__":
                    print("e.%s = %s" % (k, getattr(e, k)))


def set_image_nofi():
    path = tkinter.filedialog.askopenfilename(filetypes=[("Image File", '.jpg'), ("Image File", '.png')])
    img = cv2.imread(path)
    try:
        cv2.imwrite('./Images/nofi.png', img)
        messagebox.showinfo(title="Saved", message="The image has been re-setup")
    except cv2.error as e:
        # handle error: empty image
        if e.err == "!_img.empty()":
            messagebox.showerror(title="No Image", message="Error: Image hasn't been choose")
        else:
            # inspect error object
            print(e)
            for k in dir(e):
                if k[0:2] != "__":
                    print("e.%s = %s" % (k, getattr(e, k)))


def set_image_seenby():
    path = tkinter.filedialog.askopenfilename(filetypes=[("Image File", '.jpg'), ("Image File", '.png')])
    img = cv2.imread(path)
    try:
        cv2.imwrite('./Images/seenby.png', img)
        messagebox.showinfo(title="Saved", message="The image has been re-setup")
    except cv2.error as e:
        # handle error: empty image
        if e.err == "!_img.empty()":
            messagebox.showerror(title="No Image", message="Error: Image hasn't been choose")
        else:
            # inspect error object
            print(e)
            for k in dir(e):
                if k[0:2] != "__":
                    print("e.%s = %s" % (k, getattr(e, k)))
