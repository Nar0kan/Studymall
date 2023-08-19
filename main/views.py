from django.shortcuts import render, redirect
from django.core.mail import EmailMessage
from django.conf import settings
from .forms import *


def redirect_to_home_page(request):
    return redirect('/home')


def operate_with_contact(request):
    form = ContactForm(request.POST)

    if form.is_valid():
        subject = form.cleaned_data["subject"]
        message = form.cleaned_data["message"]
        user_email = form.cleaned_data["email"]
        name = form.cleaned_data["name"]

        try:
            recepients = user_email
            email = EmailMessage(
                subject=f"Вітаємо, {name}!",
                body="""
                    Ваш запит було успішно надіслано.
                    Він буде опрацьований спеціалістами.
                    """,
                from_email=settings.EMAIL_HOST_USER,
                to=[recepients]
            )
            email.fail_silently = False
            email.send()

            recepients = 'wertynhard@gmail.com'
            email = EmailMessage(
                subject=f"{user_email} | {subject}",
                body=message,
                from_email=settings.EMAIL_HOST_USER,
                to=[recepients]
            )
            email.fail_silently = False
            email.send()
            message = 'success'

        except Exception as e:
            message = 'error'
    else:
        message = 'error'
    
    return (form, message)


def home_page(request):
    if request.method == "POST":
        form, message = operate_with_contact(request)
    else:
        message = ''
        form = ContactForm()

    return render(request, 'home.html', {"form": form, 'message': message})


def contact_page(request):
    if request.method == "POST":
        form, message = operate_with_contact(request)
    else:
        message = ''
        form = ContactForm()

    return render(request, "contact.html", {"form": form, 'message': message})


def study_programs_page(request):
    return render(request, 'study_programs.html', {})


def python_study_plan_page(request):
    return render(request, 'python_study.html', {})


def about_page(request):
    return render(request, 'about.html', {})


# custom 404 view
def custom_404_view(request, exception):
    return render(request, '404.html', status=404)


# custom 500 view
def custom_500_view(request):
    return render(request, '500.html', status=500)
