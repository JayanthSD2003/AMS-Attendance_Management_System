import tkinter as tk
from tkinter import *
import os, cv2
import shutil
import csv
import numpy as np
from PIL import ImageTk, Image
import pandas as pd
import datetime
import time
import tkinter.font as font
import pyttsx3

# project module
import show_attendance
import takeImage
import trainImage
import automaticAttendance

# engine = pyttsx3.init()
# engine.say("Welcome!")
# engine.say("Please browse through your options..")
# engine.runAndWait()


def text_to_speech(user_text):
    engine = pyttsx3.init()
    engine.say(user_text)
    engine.runAndWait()


haarcasecade_path = "F:\Projects\AMS\haarcascade_frontalface_default.xml"  #haarcascade_frontalface_default.xml
trainimagelabel_path = (
    "F:\Projects\AMS\TrainingImageLabel\Trainner.yml"  #Trainner.yml
)
trainimage_path = "TrainingImage"
if not os.path.exists(trainimage_path):
    os.makedirs(trainimage_path)

studentdetail_path = (
    "F:\Projects\AMS\StudentDetails\studentdetails.csv"  #studentdetails.csv
)
attendance_path = "Attendance"


window = Tk()
window.title("AMS - Smart College!!")
window.geometry("1280x720")
dialog_title = "QUIT"
dialog_text = "Are you sure want to close?"
window.configure(background="#274c43")


# to destroy screen
def del_sc1():
    sc1.destroy()


# error message for name and no
def err_screen():
    global sc1
    sc1 = tk.Tk()
    sc1.geometry("400x110")
    sc1.iconbitmap("AMS.ico") #AMS.ico
    sc1.title("Warning!!")
    sc1.configure(background="#274c43")
    sc1.resizable(0, 0)
    tk.Label(
        sc1,
        text="Enrollment & Name required!!!",
        fg="yellow",
        bg="#274c43",
        font=("Ink Free", 20, " bold "),
    ).pack()
    tk.Button(
        sc1,
        text="OK",
        command=del_sc1,
        fg="yellow",
        bg="#274c43",
        width=9,
        height=1,
        activebackground="Red",
        font=("Ink Free", 20, " bold "),
    ).place(x=110, y=50)


def testVal(inStr, acttyp):
    if acttyp == "1":  # insert
        if not inStr.isdigit():
            return False
    return True


logo = Image.open("UI_Image/0001.png")
logo = logo.resize((50, 47), Image.Resampling.LANCZOS)
logo1 = ImageTk.PhotoImage(logo)
titl = tk.Label(window, bg="#274c43", relief=RIDGE, bd=10, font=("Ink Free", 35))
titl.pack(fill=X)
l1 = tk.Label(window, image=logo1, bg="black",)
l1.place(x=470, y=10)

titl = tk.Label(
    window, text="Smart College!!", bg="#274c43", fg="yellow", font=("Bradley Hand ITC", 27, "bold"),
)
titl.place(x=525, y=12)

a = tk.Label(
    window,
    text="Welcome to the Face Recognition Based\nAttendance Management System",
    bg="#274c43",
    fg="white",
    bd=10,
    font=("Ink Free", 35, "bold"),
)
a.pack()

ri = Image.open("UI_Image/register.png")
r = ImageTk.PhotoImage(ri)
label1 = Label(window, image=r)
label1.image = r
label1.place(x=100, y=270)

ai = Image.open("UI_Image/attendance.png")
a = ImageTk.PhotoImage(ai)
label2 = Label(window, image=a)
label2.image = a
label2.place(x=980, y=270)

vi = Image.open("UI_Image/verifyy.png")
v = ImageTk.PhotoImage(vi)
label3 = Label(window, image=v)
label3.image = v
label3.place(x=600, y=270)


def TakeImageUI():
    ImageUI = Tk()
    ImageUI.title("Student Enrollment...")
    ImageUI.geometry("780x480")
    ImageUI.configure(background="#274c43")
    ImageUI.resizable(0, 0)
    titl = tk.Label(ImageUI, bg="#274c43", relief=RIDGE, bd=10, font=("Ink Free", 35))
    titl.pack(fill=X)
    # image and title
    titl = tk.Label(
        ImageUI, text="Student Face Registration", bg="#274c43", fg="yellow", font=("Ink Free", 30),
    )
    titl.place(x=270, y=12)

    # heading
    a = tk.Label(
        ImageUI,
        text="Enter the details",
        bg="#274c43",
        fg="white",
        bd=10,
        font=("Ink Free", 24),
    )
    a.place(x=280, y=75)

    # ER no
    lbl1 = tk.Label(
        ImageUI,
        text="Enrollment No",
        width=10,
        height=2,
        bg="#274c43",
        fg="white",
        bd=5,
        relief=RIDGE,
        font=("Ink Free", 12),
    )
    lbl1.place(x=120, y=130)
    txt1 = tk.Entry(
        ImageUI,
        width=17,
        bd=5,
        validate="key",
        bg="#274c43",
        fg="white",
        relief=RIDGE,
        font=("Ink Free", 25, "bold"),
    )
    txt1.place(x=250, y=130)
    txt1["validatecommand"] = (txt1.register(testVal), "%P", "%d")

    # name
    lbl2 = tk.Label(
        ImageUI,
        text="Name",
        width=10,
        height=2,
        bg="#274c43",
        fg="white",
        bd=5,
        relief=RIDGE,
        font=("Ink Free", 12),
    )
    lbl2.place(x=120, y=200)
    txt2 = tk.Entry(
        ImageUI,
        width=17,
        bd=5,
        bg="#274c43",
        fg="white",
        relief=RIDGE,
        font=("Ink Free", 25, "bold"),
    )
    txt2.place(x=250, y=200)

    lbl3 = tk.Label(
        ImageUI,
        text="Notification",
        width=10,
        height=2,
        bg="#274c43",
        fg="white",
        bd=5,
        relief=RIDGE,
        font=("Ink Free", 12),
    )
    lbl3.place(x=120, y=270)

    message = tk.Label(
        ImageUI,
        text="",
        width=32,
        height=2,
        bd=5,
        bg="#274c43",
        fg="yellow",
        relief=RIDGE,
        font=("Ink Free", 12, "bold"),
    )
    message.place(x=250, y=270)

    def take_image():
        l1 = txt1.get()
        l2 = txt2.get()
        takeImage.TakeImage(
            l1,
            l2,
            haarcasecade_path,
            trainimage_path,
            message,
            err_screen,
            text_to_speech,
        )
        txt1.delete(0, "end")
        txt2.delete(0, "end")

    # take Image button
    # image
    takeImg = tk.Button(
        ImageUI,
        text="Take Image",
        command=take_image,
        bd=10,
        font=("Ink Free", 18),
        bg="#274c43",
        fg="white",
        height=2,
        width=12,
        relief=RIDGE,
    )
    takeImg.place(x=130, y=350)

    def train_image():
        trainImage.TrainImage(
            haarcasecade_path,
            trainimage_path,
            trainimagelabel_path,
            message,
            text_to_speech,
        )

    # train Image function call
    trainImg = tk.Button(
        ImageUI,
        text="Train Image",
        command=train_image,
        bd=10,
        font=("Ink Free", 18),
        bg="#274c43",
        fg="white",
        height=2,
        width=12,
        relief=RIDGE,
    )
    trainImg.place(x=360, y=350)


r = tk.Button(
    window,
    text="Register a new student",
    command=TakeImageUI,
    bd=10,
    font=("Ink Free", 16),
    bg="#274c43",
    fg="white",
    height=1,
    width=18,
)
r.place(x=100, y=520)


def automatic_attendance():
    automaticAttendance.subjectChoose(text_to_speech)


r = tk.Button(
    window,
    text="Take Attendance",
    command=automatic_attendance,
    bd=10,
    font=("Ink Free", 16),
    bg="#274c43",
    fg="white",
    height=1,
    width=15,
)
r.place(x=600, y=520)


def view_attendance():
    show_attendance.subjectchoose(text_to_speech)


r = tk.Button(
    window,
    text="View Attendance",
    command=view_attendance,
    bd=10,
    font=("Ink Free", 16),
    bg="#274c43",
    fg="white",
    height=1,
    width=15,
)
r.place(x=1000, y=520)
r = tk.Button(
    window,
    text="EXIT",
    bd=10,
    command=quit,
    font=("Ink Free", 19, "bold"),
    bg="#274c43",
    fg="red",
    height=1,
    width=8,
)
r.place(x=600, y=630)

window.mainloop()
