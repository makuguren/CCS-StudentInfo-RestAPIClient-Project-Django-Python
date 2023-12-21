from django.urls import path
from django.conf import settings
from . import views

app_name = 'students'
urlpatterns = [
    #Views
    path('', views.index, name='index'),
    path('addStudent', views.addStudent, name='addStudent'),
    path('editStudent/<str:student_id>', views.editStudent, name='editStudent'),

    #Functions (CRUD)
    path('addStudent/', views.create_student, name='create_student'),
    path('editStudent/', views.update_student, name='update_student'),
    path('delete_student/<str:student_id>', views.delete_student, name='delete_student'),
]