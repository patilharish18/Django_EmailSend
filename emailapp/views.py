from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail
from .models import StoreData

def mypage(request):
    return render(request,'emailapp/index.html') 

def send_mail(request):
    if request.method == 'POST':
        subject = request.POST.get('subject',"")
        message = request.POST.get('message',"")
        my_email = request.POST.get('youremail',"")
        custom_email = request.POST.get('customeremail',"")
        info = StoreData.objects.create(Subj = subject, Messa = message, Self_email = my_email, Customer_email = custom_email)

        
        try:
            send_mail(subject,
            message,
            my_email,
            [customer_email],
            fail_silently = False,
            )
            return HttpResponse('Email will be sent')
        except Exception as e:
            return HttpResponse('Email could not be sent')


    else:
        return render(request,'emailapp/index.html')
        
