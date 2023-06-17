from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Case
from .forms import ReportingForm
# cases = [
#   {'name':'USS Nimtiz - Tic Tac Incident', 'date':'11/14/2004', 'location':'Pacific Ocean (Southern Cali)', 'description': 'Commander David Fravor was engaged by an unidentified aircraft which attempted to merge plot his aircraft. The UAP was described as a long white cylindrical object traveling at approx. 3000/mph and was able to change direction and altitude instantaneously. It is known as the Tic Tac Incident.', 'declassified': 'True', 'foia': 'https://www.theblackvault.com/documentarchive/' },
# ]
# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def cases_index(request):
  # We pass data to a template very much like we did in Express!
  cases= Case.objects.all()
  return render(request, 'cases/index.html', {
    'cases': cases
  })

def cases_detail(request, case_id):
  case = Case.objects.get(id=case_id)
  # init ReportingForm to be rendered
  reporting_form = ReportingForm()
  return render(request, 'cases/detail.html', {
     'case': case,
     'reporting_form': reporting_form
    
  })

class CaseCreate(CreateView):
  model = Case
  fields = '__all__'

class CaseUpdate(UpdateView):
  model = Case
  # Let's disallow the renaming of a cat by excluding the name field!
  fields = ['name', 'date', 'location', 'description', 'foia']

class CaseDelete(DeleteView):
  model = Case
  success_url = '/cases'

def add_report(request, case_id):
  form = ReportingForm(request.POST)
  if form.is_valid():
    new_report = form.save(commit=False)
    new_report.case_id = case_id
    new_report.save()   
  return redirect('detail', case_id=case_id)