from datetime import datetime
from django.shortcuts import render

# Create your views here.
def learn_django(request):
    d = datetime.now()
    return render(request, 'course/courseone.html', {'dt': d})

def learn_python(request):
    return render(request, 'course/coursetwo.html', {'p1':56.24321, 'p2':56.000, 'p3':56.37000})  

def learn_tags(request):
    return render(request, 'course/coursethree.html', {'nm':'Django', 'st': 10})

def learn_loops(request):
    student = {'names':['Rahul', 'Seema', 'Aman', 'Sahil']}
    return render(request, 'course/coursefour.html', student)

def learn_complx(request):
    stu =  { 'stu1': {'name' : 'rahul', 'roll':101},
    'stu2' : {'name' : 'seema', 'roll':102},
    'stu3' : {'name' : 'aman', 'roll':103},
    'stu4' : {'name' : 'raj', 'roll':104},
     }
    students = {'student' :stu}


    return render(request, 'course/coursefive.html', students)


