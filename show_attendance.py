import pandas as pd
from glob import glob
import os
import tkinter
import csv
import tkinter as tk
from tkinter import *
from tkinter import ttk
from datetime import datetime

def subjectchoose(text_to_speech):
    def calculate_attendance():
        Subject = tx.get()
        if Subject == "":
            t = 'Please enter the subject name.'
            text_to_speech(t)
            return

        folders = [
            r"F:\\Projects\\AMS\\Attendance\\AI-ML",  # AI-ML
            r"F:\\Projects\\AMS\\Attendance\\DA-DS",  # DA-DS
            r"F:\\Projects\\AMS\\Attendance\\Mathematics"  # Mathematics
        ]

        filenames = []
        for folder in folders:
            files_found = glob(f"{folder}\\{Subject}*.csv")
            filenames.extend(files_found)
        
        if not filenames:
            t = f'No CSV files found for subject: {Subject}'
            text_to_speech(t)
            return

        # Read all CSV files and concatenate them into one DataFrame
        df_list = [pd.read_csv(f) for f in filenames]
        newdf = pd.concat(df_list, ignore_index=True)

        # Add current date and timestamp to DataFrame
        current_date = datetime.now().strftime('%Y-%m-%d')
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        newdf['Current_Date'] = current_date
        newdf['Timestamp'] = timestamp

        # Group the data by Enrollment to get total unique attendance dates
        grouped = newdf.groupby("Enrollment").agg({
            'Enrollment': 'first',
            'Name': 'first',
            'Date': 'nunique',  # Count unique dates for attendance
            'Current_Date': 'first',  # Show the current date
            'Timestamp': 'first'  # Show the timestamp
        })

        # Calculate attendance percentage
        grouped["Percentage"] = (grouped["Date"] / len(filenames)) * 100
        result_df = grouped.rename(columns={"Date": "Total_Present_Classes"})

        # Create a new window to display the result
        result_window = tk.Tk()
        result_window.title("Attendance Report")  # Set the title to "Attendance Report"
        result_window.geometry("1100x500")

        pt = ttk.Treeview(result_window)

        # Define columns for the Treeview
        pt['columns'] = ('Enrollment', 'Name', 'Total Present Classes', 'Attendance Percentage', 'Current Date', 'Timestamp')
        pt.heading("#0", text="", anchor=tk.W)
        pt.column("#0", width=0)
        pt.heading("Enrollment", text="Enrollment")
        pt.heading("Name", text="Name")
        pt.heading("Total Present Classes", text="Total Present Classes")
        pt.heading("Attendance Percentage", text="Attendance Percentage")
        pt.heading("Current Date", text="Current Date")
        pt.heading("Timestamp", text="Timestamp")

        # Insert rows into the Treeview
        for i, row in result_df.iterrows():
            pt.insert("", "end", text="", values=(row["Enrollment"], row["Name"], row["Total_Present_Classes"], f'{row["Percentage"]:.2f}%', row["Current_Date"], row["Timestamp"]))

        pt.pack()
        result_window.mainloop()

    def open_sheets():
        Subject = tx.get()
        if Subject == "":
            t = 'Please enter the subject name to open sheets.'
            text_to_speech(t)
            return

        folders = [
            r"F:\\Projects\\AMS\\Attendance\\AI-ML",  # AI-ML
            r"F:\\Projects\\AMS\\Attendance\\DA-DS",  # DA-DS
            r"F:\\Projects\\AMS\\Attendance\\Mathematics"  # Mathematics
        ]
        
        for folder in folders:
            if os.path.exists(folder):
                files_found = glob(f"{folder}\\{Subject}*.csv")
                if files_found:
                    os.startfile(folder)  # Opens the folder where the attendance sheets are stored.
                    break
        else:
            t = f'No CSV files found for subject: {Subject}.'
            text_to_speech(t)

    subject = tk.Tk()
    subject.title("Viewing Attendance...")
    subject.geometry("580x320")
    subject.resizable(0, 0)
    subject.configure(background="#274c43")

    titl = tk.Label(subject, bg="#274c43", relief=RIDGE, bd=10, font=("Ink Free", 30))
    titl.pack(fill=X)
    titl = tk.Label(
        subject,
        text="Attendance report",
        bg="#274c43",
        fg="yellow",
        font=("Ink Free", 25),
    )
    titl.place(x=160, y=12)

    Notifica = tk.Label(
        subject,
        text="Attendance Report Generated Successfully",
        bg="#274c43",
        fg="black",
        width=33,
        height=2,
        font=("Ink Free", 15, "bold"),
    )

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

    calculate_att = tk.Button(
        subject,
        text="Show Attendance",
        command=calculate_attendance,
        bd=7,
        font=("Ink Free", 15),
        bg="#274c43",
        fg="white",
        height=2,
        width=14,
        relief=RIDGE,
    )
    calculate_att.place(x=190, y=170)

    # Add a button to check attendance sheets
    check_sheets = tk.Button(
        subject,
        text="Check Sheets",
        command=open_sheets,
        bd=7,
        font=("Ink Free", 15),
        bg="#274c43",
        fg="white",
        height=2,
        width=10,
        relief=RIDGE,
    )
    check_sheets.place(x=370, y=170)

    subject.mainloop()
