from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from .models import MailForm

def registration(request):
    return render(request, 'registration.html')

def reg(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        age = request.POST.get('age')
        email = request.POST.get('email')
        add = request.POST.get('address')
        form = MailForm(
            Name=name,
            Age=age,
            Email=email,
            Address=add,
        )
        form.save()

        subject = "Application for python developer"
        message = "Hello " + name + ",\n\nWe have received your application for python developer.\n email: " + email + "\n\nThank you!"
 
        recipient = form.Email
        send_mail(subject, message, settings.EMAIL_HOST_USER, [recipient])

    return redirect('registration')

