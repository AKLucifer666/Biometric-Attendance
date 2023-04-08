#Biometric-Attendance

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

## Points to consider

1. There's a case where the api key being used to access webcam.js through soundflare be expired. In such a scenario, replace it with a fresh API Key through this website https://cdnjs.com/libraries/webcamjs

2. Don't forget to make migrations.

3. Don't forget to activate venv before running ```python3 manage.py runserver```

## Working

### The Navbar is divided into four paths:

### Attendance
This is the homepage of the website.

### Mark Attendance
This page accepts 3 parameters, **Roll No.**, **Password**, **Face**.
If the face and password to the corresponding roll number is correct, it then proceeds to a confirmation page which results in the marking of attendance on that date.

### Register Student
This page is used to register a new student in the database.

### Track Attendance
This page offers a dropdown of dates among which the user chooses one. All the present students on that date is displayed in a table.


