from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from .models import Course, Enrollment
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required,  permission_required


@login_required(login_url='/login')
def main_view(request):
    courses = Course.objects.all()
    return render(request, 'course_list.html', {'courses': courses})

@login_required(login_url='index')
@permission_required("e_learning.add_student", login_url='login', raise_exception=True)
def user_register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})


def user_login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('index')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})





def user_logout(request):
    logout(request)
    return redirect('index')

@login_required(login_url='index')
@permission_required("e_learning.add_course", login_url='login', raise_exception=True)
def add_course(request):
    if request.method == "POST":
        course = Course(
            name = request.POST.get('name'),
            description = request.POST.get('description'),
            category = request.POST.get('category'),
            url=request.POST.get('url'),
        )
        course.save()
        return redirect('index')
    return render(request, 'add.html')
    


def details(request,name):
    course = get_object_or_404(Course, name=name)
    enrollment_exists = Enrollment.objects.filter(user=request.user, course=course).exists()

    if request.method == 'POST':
        if not enrollment_exists:
            # If not enrolled, create a new enrollment
            progress = Enrollment(course=course, user=request.user)
            progress.save()
            return redirect('index')
        else:
            return HttpResponse("Already enrolled")
    return render(request, "details.html", {'course': course})



@login_required(login_url='index')
def progress(request,user):
    user_enrollments = Enrollment.objects.filter(user=request.user)
    return render(request, 'progress.html', {'user_enrollments': user_enrollments})

 
@login_required(login_url='index')
def complete_course(request, course):
    finished_course = get_object_or_404(Course, name=course)
    enrollment = Enrollment.objects.get(
        user=request.user,
        course=finished_course
    )
    if request.method == 'POST':
        enrollment.is_done = True
        enrollment.save()
        return redirect('index')
    return render(request, 'complete.html')

def delete_from_progress(request, course):
    course = get_object_or_404(Course, name=course)
    course_in_progress = Enrollment.objects.get(
        user=request.user,
        course=course
    )
    if request.method == "POST":
        course_in_progress.delete()
        return redirect('index')
    return render(request, 'complete.html')

@login_required(login_url='index')
@permission_required("e_learning.change_course", login_url='login', raise_exception=True)
def edit_course(request, name):
    course = Course.objects.get(name=name)
    if request.method =="POST":
        course.name = request.POST.get('name')
        course.description = request.POST.get('description')
        course.category = request.POST.get('category')
        course.save()
        return redirect('index')
    
    return render(request, 'edit.html', {'course': course})


@login_required(login_url='index')
@permission_required("e_learning.delete_course", login_url='login', raise_exception=True)
def delete_course(request, name):
    course = Course.objects.get(name=name)
    if request.method =="POST":
        course.delete()
        return redirect('index')
    return render(request, 'delete.html', {'course': course})



