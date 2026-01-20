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

def ifelse(request):
    data3 = {"title":"ifelse","number":[11,22,33,44,55,66,],
    "college_details":[{
        "name":"Medicaps University",
        "ROllNO":"2022",
        "Contact_NO":97658939320,
        },
        {   "name":"IPS",
            "ROllNO":"2020",
            "Contact_NO":1111111111111111,
        },
    ]
    }
    return render (request,"ifelse.html",data3)

def home(request):
    return render(request,"home.html")

def about(request):
    return render(request,"about.html")

def contact(request):
    return render(request,"contact.html")

def services(request):
    return render(request,"services.html")