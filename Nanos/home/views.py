from django.shortcuts import render, HttpResponse
from datetime import datetime
from django.core.mail import send_mail
from home.models import Contact
from django.contrib import messages
from django.conf import settings
from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    context = {
        "variable1": "naino is great",
        "variable2": "hasnain is great"
    } 
    return render(request, 'index.html', context)

def about(request):
    return render(request, 'about.html') 

def resume(request):
    return render(request, 'resume.html') 

def services(request):
    return render(request, 'services.html')

def working(request):
    return render(request, 'working.html')
 
def contact(request):
    if request.method == "POST":
        name = request.POST.get('name').strip()
        email = request.POST.get('email').strip()
        phone = request.POST.get('phone').strip()
        desc = request.POST.get('desc').strip()

        # Check if any field is empty
        if not name or not email or not phone or not desc:
            messages.error(request, "Please fill in all fields before submitting.")
            return redirect('contact')  # redirect instead of render

        # Save to database
        contact = Contact(name=name, email=email, phone=phone, desc=desc, date=datetime.today())
        contact.save()

        # Email setup
        subject = f"New Contact Message from {name}"
        message = f"""
hay Naino! You have received a new message from your website contact form.

Name: {name}
Email: {email}
Phone: {phone}
Message:
{desc}
"""
        from_email = settings.EMAIL_HOST_USER
        recipient_list = ["hasnain2244567@gmail.com"]  

        try:
            send_mail(subject, message, from_email, recipient_list, fail_silently=False)
            messages.success(request, 'Your message has been sent and emailed successfully!')
        except Exception as e:
            messages.error(request, f'Message saved but email failed to send: {e}')

        # Redirect after POST to prevent resubmission
        return redirect('contact')

    return render(request, 'contact.html')
