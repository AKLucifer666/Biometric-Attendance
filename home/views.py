from django.shortcuts import render, HttpResponse
from home.models import studentsData, attendance
import base64
import numpy as np
import cv2
import cryptocode
import face_recognition
from django.contrib import messages
from datetime import datetime
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

def index(request):
    return render(request,"index.html")

@csrf_exempt
def trackAttendance(request):
    chosen="none"
    if request.method == "POST":
        chosen = request.POST.get("sel")
    data = attendance.objects.all()
    context = {}
    details = []
    dates = []
    for row in data:
        details.append({"name":row.name,"rollno": row.rollno,"branch": row.branch,"date": row.date})
        if row.date not in dates:
            dates.append(row.date)
    context["data"] = details
    context["dates"] = dates
    context["chosen"] = chosen
    return render(request,"trackAttendance.html",context)

def markAttendance(request):
    if request.method == "POST":
        data = studentsData.objects.all()
        rno = request.POST.get("rollno")
        password = request.POST.get("password")
        photo = request.POST.get("base64")
        try:
            curr_img = decode_data(photo)
            f = 1
            for row in data:
                if row.rollno == rno:
                    f = 0
                    img = (row.photo_coordinates)
                    img = img.replace("\n", "" )[1:-2]
                    img = np.fromstring(img, dtype=float, sep=' ')
                    img = np.asarray(img, dtype = np.float64, order ='C')
                    result = checkImage(img,curr_img)
                    if result[0]:
                        decoded = cryptocode.decrypt(row.password, password)
                        if decoded=="IIT BHU":
                            messages.success(request, "Student Found!")
                            context = {"name": row.name, "branch": row.branch, "contact": row.contact, "rollno": row.rollno}
                            return render(request,"confirmAttendance.html",context=context)
                        else:
                            messages.warning(request, "Wrong Password!")
                    else:
                        messages.warning(request, "Biometrics didn't match!")
                    break
        except:
            messages.warning(request, "Picture not clear!")
            return render(request,"markAttendance.html")
        if f:
            messages.warning(request, "Not Found!")

    return render(request,"markAttendance.html")

def confirmAttendance(request):
    if request.method=="POST":
        data = attendance.objects.all()
        name = request.POST.get("name")
        rollno = request.POST.get("rollno")
        branch = request.POST.get("branch")
        date = str(datetime.now())[:10]
        for row in data:
            if row.rollno==rollno and date==row.date:
                messages.warning(request, "Attendance Already Marked!")
                return render(request,"markAttendance.html")
        mark = attendance(name=name,rollno=rollno,branch=branch,date=date)
        mark.save()
        messages.success(request, "Attendance Marked!")
    return render(request,"markAttendance.html")

def registerStudent(request):
    np.set_printoptions(suppress=True,formatter={'float_kind':'{:f}'.format})
    if request.method=="POST":
        data = studentsData.objects.all()
        name = request.POST.get("name")
        rollno = request.POST.get("rollno")
        contact = request.POST.get("contact")
        branch = request.POST.get("branch")
        password = request.POST.get("password1")
        photo = request.POST.get("base64")
        for row in data:
            if row.rollno==rollno:
                messages.warning(request, "User already exists!")
                return render(request,"registerStudent.html")

        try:
            photo_coordinates = decode_data(photo)
            password = cryptocode.encrypt("IIT BHU",password)
            register = studentsData(name=name,rollno=rollno,contact=contact,branch=branch,password=password,photo_coordinates=photo_coordinates)
            register.save()
            messages.success(request, "Your profile has been set!")
        except:
            messages.warning(request, "Picture not clear")
            return render(request,"registerStudent.html")

    return render(request,"registerStudent.html")

def decode_data(encoded_data):
    encoded_data = encoded_data.split("base64,")[1]
    decoded_data=base64.b64decode((encoded_data))
    file_bytes = np.asarray(bytearray(decoded_data), dtype=np.uint8)
    img = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)
    img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    encode = face_recognition.face_encodings(img)[0]
    return encode

def checkImage(coordinates,current):
    matches = face_recognition.compare_faces([coordinates],current)
    return matches