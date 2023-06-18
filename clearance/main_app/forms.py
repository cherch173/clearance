from django.forms import ModelForm
from .models import Reporting

class ReportingForm(ModelForm):
    class Meta:
        model = Reporting
        fields = ['date', 'report']