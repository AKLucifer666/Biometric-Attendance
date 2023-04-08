# Biometric-Attendance
$${\color{red}Welcome \space \color{lightblue}To \space \color{lightgreen}Biometric Attendance}$$
## Installation
1. Preferably use python3.8 and set up a virtual environment using the command:
```
python3 -m venv <venv name>
```
```
source <venv name>/bin/activate
```

2. Clone the project

3. Run in terminal the following command: 
```
pip3 install -r requirements.txt
```

## Technologies Used

1. Django inbuilt _sqlite3_ is used to store data and attendance of user.
2. _Encrypted Password_ is stored in the students data table.
3. _face_recognition_ and _openCV_ module is used for computer vision.
4. Captured photo is being processed in the form of _base64_ with the help of _webcam.js library API_ being offered by _soundflare_ which is then decoded in python

## Points to consider

1. There's a case where the api key being used to access webcam.js through soundflare be expired. In such a scenario, replace it with a fresh API Key through this website https://cdnjs.com/libraries/webcamjs

2. Don't forget to make migrations.

3. Don't forget to activate venv before running ```python3 manage.py runserver```

## Working

### The Navbar is divided into four paths:

### Attendance
+ This is the homepage of the website.

### Mark Attendance

+ This page accepts 3 parameters, **Roll No.**, **Password**, **Face**.
If the face and password to the corresponding roll number is correct, it then proceeds to a confirmation page which results in the marking of attendance on that date.

### Register Student
+ This page is used to register a new student in the database.

### Track Attendance
+ This page offers a dropdown of dates among which the user chooses one. All the present students on that date is displayed in a table.

## Demonstration:

https://user-images.githubusercontent.com/97111211/230719839-2a3de5f7-e1a1-4178-b0c4-e7975915e0c4.mp4


