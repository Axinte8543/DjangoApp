import django.forms as forms
from .models import Curs

class CursForm(forms.ModelForm):
    class Meta:
        model = Curs
        fields = ['denumire', 'numar_credite', 'student']
        labels = {
            'denumire': 'Denumire',
            'numar_credite': 'Numar credite',
            'student': 'Student'
        }

    def clean_numar_credite(self):
        data = self.cleaned_data['numar_credite']
        if data < 1 or data > 10:
            raise forms.ValidationError("Numarul de credite trebuie să fie intre 1 si 10")
        return data

    def clean_denumire(self):
        data = self.cleaned_data['denumire']
        if Curs.objects.filter(denumire=data).exists():
            raise forms.ValidationError("Denumirea cursului trebuie sa fie unica")
        return data