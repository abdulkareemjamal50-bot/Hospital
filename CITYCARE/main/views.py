from django.shortcuts import render, redirect
from .models import ContactMessage

from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
# Create your views here.
def health(request):
    return render(request, "health.html")

def about(request):
    return render(request, "about.html")

def care(request):
    return render(request, "404.html")

def appointment(request):
    return render(request, "appointment.html")

def contact(request):
     if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject= request.POST.get('subject')
        message = request.POST.get('message')

            # save to database
        ContactMessage.objects.create(
                name=name,
                email=email,
                subject=subject,
                message=message
            )
        # send notification to mail
        send_mail(
            subject=f"{name},New contact message from citycare website",
            message=f"""
name:{name}
Email:{email}

Message:{message}
""",
from_email=settings.DEFAULT_FROM_EMAIL,
recipient_list=["abdulkareemjamal50@gmail.com"],
fail_silently=False,
        )
        messages.success(request,"Message sent succesfully")
        return redirect('contact')
     return render(request, "contact.html")

def departmentDetails(request):
    return render(request, "department-details.html")

def departments(request):
    return render(request, "departments.html")

def doctors(request):
    return render(request, "doctors.html")

def faq(request):
    return render(request, "faq.html")

def gallery(request):
    return render(request, "gallery.html")

def index(request):
    return render(request, "index.html")

def privacy(request):
    return render(request, "privacy.html")

def serviceDetails(request):
    return render(request, "service-details.html")

def services(request):
    return render(request, "services.html")

def starterPage(request):
    return render(request, "starter-page.html")

def terms(request):
    return render(request, "terms.html")

def testimonials(request):
    return render(request, "testimonials.html")