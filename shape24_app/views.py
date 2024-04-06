from django.shortcuts import render, redirect
from django.conf import settings
from django.http import HttpResponse
from shape24_app.models import Users
from shape24_app.models import Projects
from shape24_app.models import AssignedProjects
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


def is_already_selected(request):
    user_id = request.session["_id"]

    assigned_project = AssignedProjects.objects.filter(user=user_id)

    if not assigned_project:
        return False
    
    assigned_project = assigned_project[0]
    
    return True


def login(request):
    if request.method == "GET":
        try:
            jwt_token = request.session.get("jwt-token", None)

            if jwt_token:
                if not bypass_login_check(request):
                    return render(request, "index.html")
                else:
                    if is_already_selected(request):
                        return redirect("/view_selected_project/")
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

        if is_already_selected(request):
            return redirect("/view_selected_project/")

        projects = Projects.objects.all()

        projects_list = []

        for project in projects:
            project_attributes = vars(project).copy()
            del project_attributes['_state']
            projects_list.append(project_attributes)
        
        random.shuffle(projects_list)

        return render(request, "dashboard.html", {"projects": projects_list, "user_id": request.session["_id"]})

def check_availability(request, project_id):
    if request.method == "GET":
        project = Projects.objects.filter(project_id=project_id)
        
        if not project:
            return HttpResponse(0)
        else:
            return HttpResponse(project[0].availability)

def confirm_project(request):
    if request.method == "POST":
        user_id = request.POST.get("user_id")
        project_id = request.POST.get("project_id")

        if str(request.session['_id']) != str(user_id):
            return HttpResponse("Unauthorized", status=401)

        existing_user = AssignedProjects.objects.filter(user_id=user_id)

        if existing_user:
            return HttpResponse("Already selected!", status=409)
        
        existing_project = Projects.objects.filter(project_id=project_id)

        if not existing_project:
            return HttpResponse("Project not found!", status=404)
        
        existing_project = existing_project[0]

        if existing_project.availability <= 0:
            return HttpResponse("Project unavailable!", status=409)
        
        existing_project.availability = existing_project.availability - 1
        existing_project.save()

        user = Users.objects.filter(user_id=user_id)

        if not user:
            return HttpResponse("User not found!", status=404)
        
        user = user[0]

        assigned_project = AssignedProjects.objects.create(user=user, project=existing_project)

        return HttpResponse("OK", status=200)

    return HttpResponse("Bad Request", status=400)

def view_selected_project(request):
    user_id = request.session["_id"]

    assigned_project = AssignedProjects.objects.filter(user=user_id)

    if not assigned_project:
        return redirect("/dashboard/")
    
    assigned_project = assigned_project[0]
    
    project = Projects.objects.get(project_id=assigned_project.project.project_id)
    
    return render(request, "result.html", {"project": project.project_title})

def logout(request):
    request.session.clear()
    return redirect("/login/")