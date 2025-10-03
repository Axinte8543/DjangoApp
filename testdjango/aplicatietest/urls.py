from django.urls import path
from . import views

urlpatterns = [
    path('elevi/', views.elevi, name='elevi'),
    path('cursuri_student/<int:student_id>/', views.cursuri_student, name='cursuri_student'),
    path('formular/', views.formular, name='formular'),
    path('mesaj_trimis/', views.mesaj_trimis, name='mesaj_trimis'),
]