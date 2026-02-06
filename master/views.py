from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render,redirect

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

def index1(request):
    return render(request,"index1.html")

def header(request):
    return render(request,"header.html")

def footer(request):
    return render(request,"footer.html")

def base(request):
    return render(request,"base.html")

def navbar(request):
    return render(request,"navbar.html")

def l17(request):
    data1 = {
        'topic':"For Loop",
        'title':"For loop",
        'bdata':"Nischay is chomu",
        'clist':['php','java','python'],
        'student':[{
            'name':'shivam',
            'phone':7898136977,
        },
        {
            'name':'shobhit',
            'phone':4549161541,
        
        }]
    }
    return render(request,"l17.html",data1)

def l18(request):
    data2 = {
        'topic':"IF Else",
        'title':"If else",
        'number':[10,20,30,40],

        'student':[{
            'name':'shivam',
            'phone':7898136977,
        },
        {
            'name':'shobhit',
            'phone':4549161541,
        
        }]
    }
    return render(request,"l18.html",data2)

def l19(request):
    data3 = {
        'topic':"Static files Management",
        'title':"Static files management",
        'css':'Static files from CSS',
        'image':'Files from image',
    }
    return render(request,"l19.html",data3)

def l20(request):
    return render(request,"l20.html")

def l22(request):
    finalans=0
    try:
        n1 = int(request.GET['num1'])
        n2 = int(request.GET['num2'])
        finalans=n1+n2
    except:
        pass
    return render(request,"l22.html",{'output':finalans})

def l23(request):
    finalans=0
    try:
        if request.method=="POST":
         n1 = int(request.POST.get('num1'))
         n2 = int(request.POST.get('num2'))
         finalans=n1+n2
    except:
        pass
    return render(request,"l23.html",{'output':finalans})

def l24(request):
    finalans=0
    try:
        if request.method=="POST":
         n1 = int(request.POST.get('num1'))
         n2 = int(request.POST.get('num2'))
         finalans=n1+n2
         data={
             'n1':n1,
             'n2':n2,
             'output':finalans
         }
    except:
        pass
    url = "/l19/  output={}".format(finalans)
    return HttpResponseRedirect('/l18/')