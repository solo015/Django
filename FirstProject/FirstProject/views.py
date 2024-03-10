from django.http import HttpResponse
from django.shortcuts import render

def homePage(request):
    # titledata={'title':'Home Page','welcome':'Welcome in My Website (Saif is owner of this site)','clist':['java','php','python','javascript'],'numbers':[10,20,30,40,50],'student_details':[{'name':'pradeep','phone':923028383},{'name':'tesing','phone':938298394}]}

    return render(request,"index.html")

def aboutUs(request):
    return HttpResponse("Welcome to my Website")
def course(requet):
    return HttpResponse("<b>Welcome to 2nd Website</b>")

def courseDetailsInt(request, courseId):
    return HttpResponse(courseId)

def courseDetailsStr(request, courseId):
    return HttpResponse(courseId)

def courseDetailsSlug(request, courseId):
    return HttpResponse(courseId," slug")

def courseDetails(request, courseId):
    return HttpResponse(courseId+ " None defined Value")