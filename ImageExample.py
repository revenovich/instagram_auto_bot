from tkinter import *
from PIL import Image, ImageTk
import pygetwindow as gw


global img


def image_checkp():
    a = Toplevel()
    a.title("Example for check_personal.png")
    a.iconbitmap('./Images/app_logo.ico')
    global img
    im = Image.open('./ExampleImages/check_personal.png')

    img = ImageTk.PhotoImage(im)
    Label(a, text='Example:', font=("Arial", 12, 'bold')).grid(row=0, column=0)

    Label(a, text='You should take screenshot like the rectangle '
                  'or include the avatar.\n '
                  'But I recommend take like the example, '
                  'because when user change avatar,'
                  'it may break the detection '
                  'and you have to re-setup', font=("Arial", 8)).grid(row=1, column=0, rowspan=2)

    Label(a, image=img).grid(row=3, column=0)

    a.update()

    gw.getWindowsWithTitle("Example for check_personal.png")[0].moveTo(0, 0)
    gw.getWindowsWithTitle("Example for check_personal.png")[0].activate()
    if len(gw.getWindowsWithTitle("Example for check_personal.png")) >= 2:
        for i in range(len(gw.getWindowsWithTitle("Example for check_personal.png"))-1):
            gw.getWindowsWithTitle("Example for check_personal.png")[(i+1)].close()
    try:
        if len(gw.getWindowsWithTitle("Example for nofi.png")) == 1:
            gw.getWindowsWithTitle("Example for nofi.png")[0].close()
        if len(gw.getWindowsWithTitle("Example for notstoreinfo.png")) == 1:
            gw.getWindowsWithTitle("Example for notstoreinfo.png")[0].close()
        if len(gw.getWindowsWithTitle("Example for logedin.png")) == 1:
            gw.getWindowsWithTitle("Example for logedin.png")[0].close()
        if len(gw.getWindowsWithTitle("Example for seenby.png")) == 1:
            gw.getWindowsWithTitle("Example for seenby.png")[0].close()
    except Exception as err:
        print(err)


def image_nofi():
    a = Toplevel()
    a.title("Example for nofi.png")
    a.iconbitmap('./Images/app_logo.ico')
    global img
    im = Image.open('./ExampleImages/nofi.png')

    img = ImageTk.PhotoImage(im)
    Label(a, text='Example:', font=("Arial", 12, 'bold')).grid(row=0, column=0)

    Label(a, text='You should take screenshot like the rectangle.'
                  ' This error usually cause by the web browser language.',
          font=("Arial", 8)).grid(row=1, column=0, rowspan=2)

    Label(a, image=img).grid(row=3, column=0)

    a.update()

    gw.getWindowsWithTitle("Example for nofi.png")[0].moveTo(0, 0)
    gw.getWindowsWithTitle("Example for nofi.png")[0].activate()
    if len(gw.getWindowsWithTitle("Example for nofi.png")) >= 2:
        for i in range(len(gw.getWindowsWithTitle("Example for nofi.png"))-1):
            gw.getWindowsWithTitle("Example for nofi.png")[(i+1)].close()

    try:
        if len(gw.getWindowsWithTitle("Example for check_personal.png")) == 1:
            gw.getWindowsWithTitle("Example for check_personal.png")[0].close()
        if len(gw.getWindowsWithTitle("Example for notstoreinfo.png")) == 1:
            gw.getWindowsWithTitle("Example for notstoreinfo.png")[0].close()
        if len(gw.getWindowsWithTitle("Example for logedin.png")) == 1:
            gw.getWindowsWithTitle("Example for logedin.png")[0].close()
        if len(gw.getWindowsWithTitle("Example for seenby.png")) == 1:
            gw.getWindowsWithTitle("Example for seenby.png")[0].close()
    except Exception as err:
        print(err)


def image_notstoreinfo():
    a = Toplevel()
    a.title("Example for notstoreinfo.png")
    a.iconbitmap('./Images/app_logo.ico')
    global img
    im = Image.open('./ExampleImages/notstoreinfo.png')

    img = ImageTk.PhotoImage(im)
    Label(a, text='Example:', font=("Arial", 12, 'bold')).grid(row=0, column=0)

    Label(a, text='You should take screenshot like the rectangle.'
                  ' This error usually cause by the web browser language.',
          font=("Arial", 8)).grid(row=1, column=0, rowspan=2)

    Label(a, image=img).grid(row=3, column=0)

    a.update()

    gw.getWindowsWithTitle("Example for notstoreinfo.png")[0].moveTo(0, 0)
    gw.getWindowsWithTitle("Example for notstoreinfo.png")[0].activate()
    if len(gw.getWindowsWithTitle("Example for notstoreinfo.png")) >= 2:
        for i in range(len(gw.getWindowsWithTitle("Example for notstoreinfo.png"))-1):
            gw.getWindowsWithTitle("Example for notstoreinfo.png")[(i+1)].close()
    try:
        if len(gw.getWindowsWithTitle("Example for check_personal.png")) == 1:
            gw.getWindowsWithTitle("Example for check_personal.png")[0].close()
        if len(gw.getWindowsWithTitle("Example for nofi.png")) == 1:
            gw.getWindowsWithTitle("Example for nofi.png")[0].close()
        if len(gw.getWindowsWithTitle("Example for logedin.png")) == 1:
            gw.getWindowsWithTitle("Example for logedin.png")[0].close()
        if len(gw.getWindowsWithTitle("Example for seenby.png")) == 1:
            gw.getWindowsWithTitle("Example for seenby.png")[0].close()
    except Exception as err:
        print(err)


def image_logined():
    a = Toplevel()
    a.title("Example for logedin.png")
    a.iconbitmap('./Images/app_logo.ico')
    global img
    im = Image.open('./ExampleImages/logedin.png')

    img = ImageTk.PhotoImage(im)
    Label(a, text='Example:', font=("Arial", 12, 'bold')).grid(row=0, column=0)

    Label(a, text='You should take screenshot like the rectangle.'
                  ' This error usually cause by the web browser language.',
          font=("Arial", 8)).grid(row=1, column=0, rowspan=2)

    Label(a, image=img).grid(row=3, column=0)

    a.update()

    gw.getWindowsWithTitle("Example for logedin.png")[0].moveTo(0, 0)
    gw.getWindowsWithTitle("Example for logedin.png")[0].activate()
    if len(gw.getWindowsWithTitle("Example for logedin.png")) >= 2:
        for i in range(len(gw.getWindowsWithTitle("Example for logedin.png"))-1):
            gw.getWindowsWithTitle("Example for logedin.png")[(i+1)].close()
    try:
        if len(gw.getWindowsWithTitle("Example for check_personal.png")) == 1:
            gw.getWindowsWithTitle("Example for check_personal.png")[0].close()
        if len(gw.getWindowsWithTitle("Example for nofi.png")) == 1:
            gw.getWindowsWithTitle("Example for nofi.png")[0].close()
        if len(gw.getWindowsWithTitle("Example for notstoreinfo.png")) == 1:
            gw.getWindowsWithTitle("Example for notstoreinfo.png")[0].close()
        if len(gw.getWindowsWithTitle("Example for seenby.png")) == 1:
            gw.getWindowsWithTitle("Example for seenby.png")[0].close()
    except Exception as err:
        print(err)


global img1
global img2


def image_seenby():
    a = Toplevel()
    a.title("Example for seenby.png")
    a.iconbitmap('./Images/app_logo.ico')
    global img1
    global img2
    im1 = Image.open('./ExampleImages/seenby.png')
    im2 = Image.open('./ExampleImages/seenby1.png')

    img2 = ImageTk.PhotoImage(im2)
    img1 = ImageTk.PhotoImage(im1)
    Label(a, text='Example:', font=("Arial", 12, 'bold')).grid(row=0, column=0, columnspan=2)

    Label(a, text='You must take screenshot like the rectangle. Because include the avatars break the detection.'
                  '\nThis error usually cause by the web browser language. '
                  'You should find and capture the text that not change.',
          font=("Arial", 8)).grid(row=1, column=0, columnspan=2)

    Label(a, image=img1).grid(row=3, column=0, sticky="E")
    Label(a, image=img2).grid(row=3, column=1, sticky="W")

    a.update()

    gw.getWindowsWithTitle("Example for seenby.png")[0].moveTo(0, 0)
    gw.getWindowsWithTitle("Example for seenby.png")[0].activate()
    if len(gw.getWindowsWithTitle("Example for seenby.png")) >= 2:
        for i in range(len(gw.getWindowsWithTitle("Example for seenby.png"))-1):
            gw.getWindowsWithTitle("Example for seenby.png")[(i+1)].close()

    try:
        if len(gw.getWindowsWithTitle("Example for check_personal.png")) == 1:
            gw.getWindowsWithTitle("Example for check_personal.png")[0].close()
        if len(gw.getWindowsWithTitle("Example for nofi.png")) == 1:
            gw.getWindowsWithTitle("Example for nofi.png")[0].close()
        if len(gw.getWindowsWithTitle("Example for notstoreinfo.png")) == 1:
            gw.getWindowsWithTitle("Example for notstoreinfo.png")[0].close()
        if len(gw.getWindowsWithTitle("Example for logedin.png")) == 1:
            gw.getWindowsWithTitle("Example for logedin.png")[0].close()
    except Exception as err:
        print(err)
