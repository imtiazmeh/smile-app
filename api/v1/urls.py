from django.urls import path

from . import views

app_name = 'api'

urlpatterns = [
    path('createstudent/', views.create_student),
    path('specificstudent/', views.get_specific_student),
    path('student/', views.StudenAPI.as_view()),
]
