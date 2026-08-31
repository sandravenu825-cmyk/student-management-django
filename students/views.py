from django.shortcuts import render, redirect, get_object_or_404
from .models import Student


def home(request):
    students = Student.objects.all()

    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        course = request.POST['course']
        age = request.POST['age']

        Student.objects.create(
            name=name,
            email=email,
            course=course,
            age=age
        )

        return redirect('home')

    return render(request, 'students/home.html', {
        'students': students
    })


def delete_student(request, id):
    student = get_object_or_404(Student, id=id)
    student.delete()

    return redirect('home')