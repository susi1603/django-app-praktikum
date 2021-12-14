from django import forms
from django.forms import widgets
from .models import Task
from django import forms

# Reordering Form and View
class PositionForm(forms.Form):
    position = forms.CharField()


class AddForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ('title', 'jobdescription',
                  'joblink', 'interview', 'rejected')

        widgets = {
           
        }

class CalendarForm(forms.Form):
    calendar_field = forms.DateTimeField()