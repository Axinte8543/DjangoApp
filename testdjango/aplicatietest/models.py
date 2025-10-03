from django.db import models

class Student(models.Model):
    nume=models.CharField(max_length=100)
    prenume=models.CharField(max_length=100)
    email=models.EmailField()
    anul_inscrierii=models.DateTimeField()
    
class Curs(models.Model):
    denumire=models.CharField(max_length=100)
    numar_credite=models.PositiveIntegerField()
    student=models.ForeignKey(Student, on_delete=models.CASCADE)