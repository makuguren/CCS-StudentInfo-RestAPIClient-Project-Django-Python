from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
import requests


# Create your views here.
def index(request):
    response = requests.get('http://localhost:8080/getStudent').json()
    return render(request, 'students/index.html', {'students':response})

def addStudent(request):
    return render(request, 'students/addStudent.html')

#Fetching Student Data from ID
def editStudent(request, student_id):
    response = requests.get(f'http://localhost:8080/getStudentById/{student_id}')
    
    if response.status_code == 200:
        student_data = response.json()
        return render(request, 'students/editStudent.html', {'student_data': student_data})
    else:
        return render(request, 'students/error.html', {'message': 'Student data not found'})
    
#Functions (CRUD)
def create_student(request):
    if request.method == 'POST':
        #Getting the Value from the Form Tag
        student_id = request.POST.get('student_id', '')
        student_name = request.POST.get('student_name', '')
        course_section = request.POST.get('course_section', '')
        student_email = request.POST.get('student_email', '')
        
        students = {
            'student_id': student_id,
            'student_name': student_name, 
            'course_section': course_section, 
            'student_email': student_email
        }
        
        headers = {"Content-type": "application/json"}
        api_url = 'http://localhost:8080/addStudent'
        response = requests.post(api_url, json=students, headers = headers)
        
        if response.status_code == 200:
            messages.success(request, 'Student Added Successfully.')
            return redirect('students:index')
        else:
            messages.error(request, 'Failed to Add Students.')
            return redirect('students:index')
        
    return HttpResponse("Failed to Connect")

def update_student(request):
    if request.method == 'POST':
        #Getting the Value from the Form Tag
        student_id = request.POST.get('student_id', '')
        student_name = request.POST.get('student_name', '')
        course_section = request.POST.get('course_section', '')
        student_email = request.POST.get('student_email', '')
        
        students = {
            'student_id': student_id,
            'student_name': student_name, 
            'course_section': course_section, 
            'student_email': student_email
        }
        
        headers = {"Content-type": "application/json"}
        api_url = 'http://localhost:8080/updateStudent'
        response = requests.put(api_url, json=students, headers = headers)
        
        if response.status_code == 200:
            messages.success(request, 'Student Updated Successfully.')
            return redirect('students:index')
        else:
            messages.error(request, 'Failed to Update Students.')
            return redirect('students:index')
        
    return HttpResponse("Failed to Connect")

def delete_student(request, student_id):
    if request.method == 'POST':
    
        api_url = f'http://localhost:8080/deleteStudent/{student_id}'
        response = requests.delete(api_url)
        
        if response.status_code == 200:
            messages.success(request, 'Student Deleted Successfully.')
            return redirect('students:index')
        else:
            messages.error(request, 'Failed to Delete Students.')
            return redirect('students:index')
        
    return HttpResponse("Failed to Connect")
