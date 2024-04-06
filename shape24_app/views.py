from django.shortcuts import render, redirect
from django.conf import settings
from django.http import HttpResponse
from shape24_app.models import Users
from shape24_app.models import Projects
import hashlib
import datetime
import jwt
import random


def bypass_login_check(request):
    jwt_token = request.session.get("jwt-token", None)
    _id = request.session.get("_id")

    if not (jwt_token or _id):
        return False

    try:
        decoded_jwt = jwt.decode(jwt_token, settings.SECRET_KEY, algorithms=["HS256"])
    except jwt.InvalidTokenError:
        return False

    email = decoded_jwt.get("email")

    user_object = Users.objects.filter(user_id=_id)

    if not user_object:
        return False

    user_object = user_object[0]

    user_email = user_object.email

    if not user_email:
        return False

    hashed_email = str(hashlib.sha256(user_email.encode("utf-8")).hexdigest())

    if hashed_email == email:
        return True

    return False


def login(request):
    if request.method == "GET":
        try:
            jwt_token = request.session.get("jwt-token", None)

            if jwt_token:
                if not bypass_login_check(request):
                    return render(request, "index.html")
                else:
                    return redirect("/dashboard/")
        except:
            return render(request, "index.html")

        return render(request, "index.html")

    if request.method == "POST":
        email = request.POST.get("email", None)
        password = request.POST.get("pass", None)

        if email and password:
            user = Users.objects.filter(email=email)

            if not user:
                return render(
                    request, "index.html", {"alertmessage": "Invalid credentials!"}
                )

            user = user[0]

            if user.password != password:
                return render(
                    request, "index.html", {"alertmessage": "Invalid credentials!"}
                )

            _id = user.user_id

            token = jwt.encode(
                {
                    "email": str(hashlib.sha256(email.encode("utf-8")).hexdigest()),
                    "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=90),
                    "iat": datetime.datetime.utcnow(),
                },
                settings.SECRET_KEY,
            )

            request.session["_id"] = _id
            request.session["jwt-token"] = token

            return redirect("/dashboard/")

    return render(request, "index.html", {"alertmessage": "Invalid credentials!"})


def dashboard(request):
    if request.method == "GET":
        projects = Projects.objects.all()

        projects_list = []

        for project in projects:
            project_attributes = vars(project).copy()
            del project_attributes['_state']
            projects_list.append(project_attributes)
        
        random.shuffle(projects_list)

    return render(request, "dashboard.html", {"projects": projects_list})

def check_availability(request, project_id):
    if request.method == "GET":
        project = Projects.objects.filter(project_id=project_id)
        
        if not project:
            return HttpResponse(0)
        else:
            return HttpResponse(project[0].availability)