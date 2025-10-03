from django.shortcuts import render,redirect
from .models import Student,Curs
from .forms import CursForm
from django.http import HttpResponse
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404

def elevi(request):
    studenti = Student.objects.all()
    return render(request, 'aplicatietest/studenti.html', {'studenti': studenti})

def cursuri_student(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    cursuri = Curs.objects.filter(student=student)
    return render(request, 'aplicatietest/cursuri_student.html', {'student': student, 'cursuri': cursuri})

def formular(request):
    if request.method == 'POST':
        form = CursForm(request.POST)
        if form.is_valid():
            form.save()
            send_mail(
                subject='Curs nou',
                message=form.cleaned_data['denumire'] + ' a fost adaugat cu succes' + ' numarul total de cursuri pentru student este: ' + str(Curs.objects.filter(student=form.cleaned_data['student']).count()),
                from_email='iniminiminimo3@gmail.com',
                recipient_list=[form.cleaned_data['student'].email],
                fail_silently=False
            )
            return redirect('mesaj_trimis')
    else:
        form = CursForm()
    return render(request, 'aplicatietest/formular.html', {'form': form})

def mesaj_trimis(request):
    return HttpResponse("Mesaj trimis cu succes!")