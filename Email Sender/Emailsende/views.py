from django.shortcuts import render
from django.core.mail import send_mail

# Create your views here.
def sendemail(request):
    return render(request,'sendemail.html')
def sendmail(request):
    message_email = request.POST['email']
    message = request.POST['content']
    Subject = request.POST['subject']
    send_mail(
    Subject,#Subject
    message,#Content
    '',#From
    [message_email],#TO
    fail_silently=True,
    )
    return render(request,'sentemail.html')