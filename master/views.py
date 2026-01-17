from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return HttpResponse("Shriyash")

def coursedetails(request,courseid):
    return HttpResponse(courseid)

def homepage(request):
    return render(request,"index.html")

def basic(request):
    data={'title':"Basic Page",
    'name':"Shriyash",
    'course':"Django",
    'duration':"2 months",
    'fees':1000,
    'topics':["HTML","CSS"]}
    return render(request,"basic.html",data)

def forloop(request):
    data1={'title':"Forloop",
    'name':"PAPA",
    'Clist':["CHP","PHP","Python","JAVA","HTML"],
    "Student_details":[{
        "name":"Shriyash",
        "ROllNO":"EN22CS301938",
        "Contact_NO":9343892227,
    },
    {   "name":"Shobhit",
        "ROllNO":"EN22CS301923",
        "Contact_NO":7222983439,
    },
    ]
    }
    return render (request,"forloop.html",data1)
