from django.forms import ModelForm
from .models import Reporting, Comment

class ReportingForm(ModelForm):
    class Meta:
        model = Reporting
        fields = ['date', 'report']

class CommentForm(ModelForm):
  class Meta:
    model = Comment
    fields = ['author', 'text', 'created_date','approved_comment']