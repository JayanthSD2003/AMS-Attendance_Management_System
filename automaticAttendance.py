import tkinter as tk
from tkinter import *
import os
import cv2
import pandas as pd
import datetime
import time

# Paths for required files
haarcasecade_path = "F:\\Projects\\AMS\\haarcascade_frontalface_default.xml"  # haarcascade_frontalface_default.xml
trainimagelabel_path = "F:\\Projects\\AMS\\TrainingImageLabel\\Trainner.yml"  #Trainner.yml 
studentdetail_path = "F:\\Projects\\AMS\\StudentDetails\\studentdetails.csv"  # studentdetails.csv
attendance_path = "F:\\Projects\\AMS\\Attendance"  # Attendance

# Function for choosing subject and filling attendance
def subjectChoose(text_to_speech):
    def FillAttendance():
        sub = tx.get()
        now = time.time()
        future = now + 20  # Time limit for filling attendance (20 seconds)
        
        if sub == "":
            t = "Please enter the subject name!!!"
            text_to_speech(t)
            return
        
        try:
            recognizer = cv2.face.LBPHFaceRecognizer_create()
            recognizer.read(trainimagelabel_path)  # Load the trained model

            faceCascade = cv2.CascadeClassifier(haarcasecade_path)  # Load Haar Cascade
            if faceCascade.empty():
                raise Exception("Haar Cascade not loaded properly.")

            df = pd.read_csv(studentdetail_path, header=None, names=["Enrollment", "Name"])  # Load student details
            print("Student details DataFrame after loading:")
            print(df)  # Print the entire DataFrame
            print("Columns in DataFrame:", df.columns.tolist())  # Print the column names
            
            # Check if "Enrollment" exists in DataFrame
            if "Enrollment" not in df.columns:
                raise Exception("Column 'Enrollment' not found in the student details DataFrame.")

            cam = cv2.VideoCapture(0)  # Initialize the webcam
            
            if not cam.isOpened():
                raise Exception("Camera not opened. Please check your camera settings.")

            cam.set(cv2.CAP_PROP_FRAME_WIDTH, 640)  # Set camera width
            cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)  # Set camera height
            font = cv2.FONT_HERSHEY_SIMPLEX
            col_names = ["Enrollment", "Name", "Date", "Time"]
            attendance = pd.DataFrame(columns=col_names)  # Initialize attendance DataFrame
            
            print("Camera initialized, starting face detection...")
            
            while True:
                ret, im = cam.read()  # Capture frame
                if not ret:
                    print("Failed to capture frame")
                    break
                
                gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)  # Convert to grayscale
                faces = faceCascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)  # Detect faces
                
                print(f"Detected faces: {len(faces)}")
                
                for (x, y, w, h) in faces:
                    global Id
                    Id, conf = recognizer.predict(gray[y: y + h, x: x + w])  # Predict ID
                    print(f"Predicted ID: {Id}, Confidence: {conf}")
                    
                    if conf < 70:
                        global Subject
                        global aa
                        global date
                        global timeStamp
                        Subject = tx.get()
                        ts = time.time()
                        date = datetime.datetime.fromtimestamp(ts).strftime("%Y-%m-%d")
                        timeStamp = datetime.datetime.fromtimestamp(ts).strftime("%H:%M:%S")
                        aa = df.loc[df["Enrollment"] == Id]["Name"].values[0]  # Get name from ID
                        attendance.loc[len(attendance)] = [Id, aa, date, timeStamp]  # Add to attendance
                        cv2.rectangle(im, (x, y), (x + w, y + h), (0, 260, 0), 4)
                        cv2.putText(im, f"{Id}-{aa}", (x, y - 10), font, 1, (255, 255, 0), 4)
                    else:
                        Id = "Unknown"
                        cv2.rectangle(im, (x, y), (x + w, y + h), (0, 25, 255), 7)
                        cv2.putText(im, str(Id), (x, y - 10), font, 1, (0, 25, 255), 4)
                
                if time.time() > future:
                    break
                
                attendance = attendance.drop_duplicates(["Enrollment"], keep="first")  # Remove duplicates
                cv2.imshow("Filling Attendance...", im)  # Show the current frame
                if cv2.waitKey(30) & 0xFF == 27:  # Exit on ESC key
                    break

            # Save attendance to CSV
            path = os.path.join(attendance_path, Subject)
            if not os.path.exists(path):
                os.makedirs(path)
            fileName = f"{path}/{Subject}_{date}.csv"
            attendance.to_csv(fileName, index=False)
            print(f"Attendance saved to {fileName}")

            m = f"Attendance Filled Successfully for {Subject}"
            text_to_speech(m)
            Notifica.configure(text=m, bg="#274c43", fg="white", width=33, relief=RIDGE, bd=5, font=("Ink Free", 15, "bold"))
            Notifica.place(x=20, y=250)

            cam.release()
            cv2.destroyAllWindows()
        except Exception as e:
            print(f"Error: {e}")  # Print any exceptions for debugging
            f = "An error occurred. Please check the console."
            text_to_speech(f)
            cv2.destroyAllWindows()

    subject = tk.Tk()
    subject.title("Filling Attendance...")
    subject.geometry("580x320")
    subject.resizable(0, 0)
    subject.configure(background="#274c43")

    titl = tk.Label(subject, bg="#274c43", relief=RIDGE, bd=10, font=("Ink Free", 30))
    titl.pack(fill=X)
    titl = tk.Label(
        subject,
        text="Subject Attendance Filling",
        bg="#274c43",
        fg="yellow",
        font=("Ink Free", 25, "bold"),
    )
    titl.place(x=160, y=12)

    Notifica = tk.Label(
        subject,
        text="Attendance filled Successfully",
        bg="#274c43",
        fg="white",
        width=33,
        height=2,
        font=("Ink Free", 15),
    )

    def Attf():
        sub = tx.get()
        if sub == "":
            t = "Please enter the subject name!!!"
            text_to_speech(t)
        else:
            os.startfile(f"Attendance\\{sub}")

    attf = tk.Button(
        subject,
        text="Check Sheets",
        command=Attf,
        bd=7,
        font=("Ink Free", 15),
        bg="#274c43",
        fg="white",
        height=2,
        width=10,
        relief=RIDGE,
    )
    attf.place(x=360, y=170)

    sub = tk.Label(
        subject,
        text="Enter Subject",
        width=10,
        height=2,
        bg="#274c43",
        fg="white",
        bd=5,
        relief=RIDGE,
        font=("Ink Free", 15),
    )
    sub.place(x=50, y=100)

    tx = tk.Entry(
        subject,
        width=15,
        bd=5,
        bg="#274c43",
        fg="white",
        relief=RIDGE,
        font=("Ink Free", 30, "bold"),
    )
    tx.place(x=190, y=100)

    fill_a = tk.Button(
        subject,
        text="Fill Attendance",
        command=FillAttendance,
        bd=7,
        font=("Ink Free", 15),
        bg="#274c43",
        fg="white",
        height=2,
        width=12,
        relief=RIDGE,
    )
    fill_a.place(x=195, y=170)

    subject.mainloop()
