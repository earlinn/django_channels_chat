from django.contrib.auth import login
from django.db import IntegrityError
from django.shortcuts import redirect, render

from users.models import User


def register(request):
    if request.method == "POST":
        try:
            username = request.POST["username"]
            email = request.POST.get("email").strip()
            password = request.POST["password"]
            user = User.objects.create_user(username=username, email=email, password=password)
            login(request, user)
            return redirect("index")
        except IntegrityError:
            request.session["register_error"] = "Пользователь с таким именем или email уже существует."
            return redirect("index")
    return render(request, "registration/register.html")
