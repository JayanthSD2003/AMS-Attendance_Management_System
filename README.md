
# Face based attendance system using python and openCV

[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)                 
[![Python 3.11](https://img.shields.io/badge/python-3.11-blue.svg)](https://www.python.org/downloads/release/python-360/) 

[![NumPy](https://img.shields.io/badge/numpy-1.16.1-blue.svg)](https://pypi.org/project/numpy/1.16.1/)
[![OpenCV-contrib-python](https://img.shields.io/badge/opencv--contrib--python-4.2.0.34-blue.svg)](https://pypi.org/project/opencv-contrib-python/4.2.0.34/)
[![OpenCV-python](https://img.shields.io/badge/opencv--python-4.2.0.34-blue.svg)](https://pypi.org/project/opencv-python/4.2.0.34/)
[![openpyxl](https://img.shields.io/badge/openpyxl-3.0.3-blue.svg)](https://pypi.org/project/openpyxl/3.0.3/)
[![pandas](https://img.shields.io/badge/pandas-1.0.3-blue.svg)](https://pypi.org/project/pandas/1.0.3/)
[![Pillow](https://img.shields.io/badge/Pillow-7.1.1-blue.svg)](https://pypi.org/project/Pillow/7.1.1/)
[![pyttsx3](https://img.shields.io/badge/pyttsx3-2.71-blue.svg)](https://pypi.org/project/pyttsx3/2.71/)
[![Haar Cascade](https://img.shields.io/badge/Haar_Cascade-OpenCV-blue.svg)](https://docs.opencv.org/3.4/db/d28/tutorial_cascade_classifier.html)
[![Powered by ChatGPT](https://img.shields.io/badge/Powered_by-ChatGPT-00A884.svg)](https://openai.com/chatgpt)


### What steps you have to follow??
- Download or clone my Repository to your device
- type `pip install -r requirements.txt` in command prompt(this will install required package for project)
- Create a `TrainingImage` folder in a project folder.
- open `attendance.py` and `automaticAttendance.py`, change all the path accoriding to your system
- Run `attandance.py` file

### Project flow & explaination
- After you run the project you have to register your face so that system can identify you, so click on register new student
- After you click a small window will pop up in that you have to enter you ID and name and then click on `Take Image` button
- After clicking `Take Image` button A camera window will pop up and it will detect your Face and take upto 50 Images(you can change the number of Image it can take) and stored in the folder named `TrainingImage`. more you give the image to system, the better it will perform while recognising the face.
- Then you have to click on `Train Image` button, It will train the model and convert all the Image into numeric format so that computer can understand. we are training the image so that next time when we will show the same face to the computer it will easily identify the face.
- It will take some time(depends on you system).
- After training model click on `Automatic Attendance` ,you have to enter the subject name and then it can fill attendace by your face using our trained model.
- it will create `.csv` file for every subject you enter and seperate every `.csv` file accoriding the subject
- You can view the attendance after clicking `View Attendance` button. It will show record in tabular format.
- check sheets in each window is a auto-generated csv file of respective data in respective path(you can see the csv file right away).

### Screenshots-----

- Home - AMS
  ![Home](https://github.com/JayanthSD2003/AMS-Attendance_Management_System/blob/e6c5be12d1cfb04d4c8e038f534b0eb20c16261a/Screenshots/1.%20Home-AMS.png)

- Student Enrollment - AMS
  
   
- Face Capture - AMS
  
 
- Saving Face Data - AMS
 

- Face Data Training - AMS
  

- Subject Attendance Filling - AMS
  
  
- Subjecct Attendance Filling_sample - AMS
 

- Subject Attendance Filling_face-recognize - AMS
  
  
- Subject Attendance Filling_success - AMS
  

- Attendance Report Portal  - AMS
  

- Attendance Report Portal_sample - AMS
  
  
- Attendance Report - AMS
  
  

- Screenshots folder link:
https://github.com/JayanthSD2003/AMS-Attendance_Management_System/tree/a817a7983151a3b7642ac04c06b51d7ecba33da6/Screenshots
