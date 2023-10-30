from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.
def index(request):
    nbdata=newbatches.objects.all().order_by('-id')
    mydict={"nbdata":nbdata}
    return render(request,'user/index.html',mydict)

def mynewbatches(request):
    batchdata=newbatches.objects.all().order_by('-id')
    md={"bdata":batchdata}
    return render(request,'user/batches.html',md)

def contact(request):
    if request.method=="POST":
        a1=request.POST.get('name')
        a2=request.POST.get('email')
        a3=request.POST.get('mobile')
        a4=request.POST.get('message')
       # print(a1,a2,a3,a4)
        x=contactus(Name=a1,Email=a2,Mobile=a3,Message=a4).save()
        return HttpResponse("<script>alert('thank you for connecting with us..');location.href='/user/contact'</script>")


    return render(request,'user/contact.html')

def feedback(request):
    return render(request,'user/feedback.html')

def ourfacilaty(request):
    return render(request,'user/facilaty.html')

def successstories(request):
    clg = request.GET.get('college')
    year = request.GET.get('year')
    pdata="";
    if clg is not None and year is not None:
        pdata = placement.objects.filter(college=clg, session=year)
    else:
        pdata=placement.objects.all()


    collegedata=college.objects.all().order_by('-id')
    sdata=session_year.objects.all().order_by('-id')




    md={"cdata":collegedata,"sdata":sdata,"pdata":pdata}
    return render(request,'user/stories.html',md)

def registration(request):
    bdata=studentbatch.objects.all()
    md={"bdata":bdata}
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')#abc@gmail.com
        mobile=request.POST.get('mobile')
        passwd=request.POST.get('passwd')
        college=request.POST.get('college')
        course=request.POST.get('course')
        picture=request.FILES['fu']
        pyear=request.POST.get('pyear')
        batch=request.POST.get('batch')
        print(batch)
        x=signup.objects.filter(email=email).count()
        if x==0:
            signup(name=name,email=email,mobile=mobile,college=college,course=course,pyear=pyear,profile=picture,passwd=passwd,status='Pending',batchid=batch).save()
            return HttpResponse("<script>alert('You are registered Successfully..');location.href='/user/signup/'</script>")
        else:
            return HttpResponse("<script>alert('you are already registered...');location.href='/user/signup/'</script>")
    return render(request,'user/registration.html',md)



def aboutus(request):
    return render(request,'user/about.html')




def signin(request):

    if request.method=="POST":
        email=request.POST.get('email')#rs@gmail.com
        passwd=request.POST.get('passwd')#123
        x=signup.objects.filter(passwd=passwd,email=email).count()
        if x==1:
            request.session['user']=email
            y=signup.objects.filter(email=email,passwd=passwd)
            request.session['userpic']=str(y[0].profile)
            request.session['username']=str(y[0].name)
            request.session['batchid']=str(y[0].batchid)

            return HttpResponse("<script>location.href='/student/index/'</script>")
        else:
            return HttpResponse("<script>alert('Your username or password is incorrect..');"
                                "location.href='/user/signin/'</script>")


    return render(request,'user/studentlogin.html')