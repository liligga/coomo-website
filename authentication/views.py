import math
import random
from dataclasses import dataclass
from abc import ABC, abstractmethod

from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.urls import reverse
from django.conf import settings
from authentication.models import OneTimePassword
from django.http import JsonResponse
from online_test.models import OnlineTest, AnswerTest


def generate_otp():
    digits = "0123456789"
    otp = ""

    for i in range(4):
        otp += digits[math.floor(random.random() * 10)]

    return otp


@dataclass
class OTPNotifierService(ABC):
    email: str
    username: str
    otp: str

    @abstractmethod
    def send(self): ...


class EmailOTPNotifierService(OTPNotifierService):
    def send(self):
        send_mail(
            subject="Код подтверждения",
            message=f"Здравствуйте, {self.username}! Ваш код: {self.otp}",
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[
                self.email,
            ],
            fail_silently=False,
        )


class CliNotifierService(OTPNotifierService):
    def send(self):
        print(f"Код подтверждения: {self.otp}")


# def send_email(email, username, otp):
#     send_mail(
#         subject='Код подтверждения',
#         message=f'Здравствуйте, {username}! Ваш код: {otp}',
#         from_email=settings.DEFAULT_FROM_EMAIL,
#         recipient_list=[email,],
#         fail_silently=False,
#     )


def notify_user_otp(service: OTPNotifierService):
    service.send()


def login_page(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None and user.is_staff:
            otp = generate_otp()
            user_otp = OneTimePassword.objects.get_or_create(user=user)[0]
            user_otp.otp = otp
            user_otp.save()
            if settings.DEBUG:
                notify_user_otp(
                    CliNotifierService(
                        email=user.email, username=user.username, otp=otp
                    )
                )
            else:
                notify_user_otp(
                    EmailOTPNotifierService(
                        email=user.email, username=user.username, otp=otp
                    )
                )
            return redirect(reverse("check_otp", kwargs={"email": user.email}))
        else:
            messages.error(request, message="Неправильный логин или пароль")
            return redirect("/levdbt/")

    return render(request, "admin/login.html")


def check_otp(request, email):
    if request.method == "POST":
        user = User.objects.get(email=email)
        otp = request.POST.get("otp")
        user_otp = OneTimePassword.objects.get(user=user)
        if user_otp.otp == int(otp) and user.is_staff:
            login(request, user)
            user_otp.otp = 0
            user_otp.save()
            return redirect("/aqajbl/")
        else:
            return redirect("/levdbt/")
    return render(request, "admin/otp.html")


def example(request):
    tests = OnlineTest.objects.all()
    return JsonResponse({"tests": list(tests.values())})
