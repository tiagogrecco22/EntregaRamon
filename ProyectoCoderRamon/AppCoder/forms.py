from django import forms

class ActFormulario(forms.Form):

    Actividad = forms.CharField()
    Grupo = forms.IntegerField()
    Repeticiones_Semanales = forms.IntegerField()