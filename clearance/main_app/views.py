from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Case, Testimony
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
  id_list = case.testimonies.all().values_list('id')
  # init ReportingForm to be rendered
  testimonies_case_doesnt_have = Testimony.objects.exclude(id__in=id_list)
  reporting_form = ReportingForm()
  return render(request, 'cases/detail.html', {
     'case': case,
     'reporting_form': reporting_form,
     'testimonies': testimonies_case_doesnt_have
  })

def assoc_testimony(request, case_id, testimony_id):
  Case.objects.get(id=case_id).testimonies.add(testimony_id)
  return redirect('detail', case_id=case_id)


class CaseCreate(CreateView):
  model = Case
  fields = ['name', 'date', 'location', 'description', 'foia']

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

# class TestimonyList(ListView):
#   model = Testimony

# class TestimonyDetail(DetailView):
#   model = Testimony

class add_testimony(CreateView):
  model = Testimony
  fields = '__all__'

class TestimonyUpdate(UpdateView):
  model = Testimony
  fields = ['date', 'name', 'location', 'comment']

class TestimonyDelete(DeleteView):
  model = Testimony
  success_url = '/testimonies'