from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from .forms import ContactForm

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = "You have a new customer enquiry"
            body = {
                'full_name': form.cleaned_data['full_name'],
                'email': form.cleaned_data['email'],
                'subject': form.cleaned_data['subject'],
                'enquiry': form.cleaned_data['enquiry'],
            }
            body_string = '\n'.join([f"{key}: {value}" for key, value in body.items()])

            messages.success(request, 'Thank you! Your enquiry has been submitted successfully!')
            send_mail(subject, body_string, 'theinhometeam@gmail.com', ['theinhometeam@gmail.com'])
            return render(request, 'home/index.html')

    form = ContactForm()
    return render(request, 'contact/contact.html', {'form':form})
