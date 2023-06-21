import os
import uuid
import boto3
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Case, Testimony, Photo
from .forms import ReportingForm
# cases = [
#   {'name':'USS Nimtiz - Tic Tac Incident', 'date':'11/14/2004', 'location':'Pacific Ocean (Southern Cali)', 'description': 'Commander David Fravor was engaged by an unidentified aircraft which attempted to merge plot his aircraft. The UAP was described as a long white cylindrical object traveling at approx. 3000/mph and was able to change direction and altitude instantaneously. It is known as the Tic Tac Incident.', 'declassified': 'True', 'foia': 'https://www.theblackvault.com/documentarchive/' },
# ]
# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

@login_required
def cases_index(request):
  # We pass data to a template very much like we did in Express!
  cases= Case.objects.filter(user=request.user)
  return render(request, 'cases/index.html', {
    'cases': cases
  })

@login_required
def cases_detail(request, case_id):
  case = Case.objects.get(id=case_id)
  id_list = case.testimonies.all().values_list('id')
  # init ReportingForm to be rendered
  testimonies = Testimony.objects.all()
  print(testimonies)
  reporting_form = ReportingForm()
  return render(request, 'cases/detail.html', {
     'case': case,
     'reporting_form': reporting_form,
     'testimonies': testimonies
  })

@login_required
def assoc_testimony(request, case_id, testimony_id):
  Case.objects.get(id=case_id).testimonies.add(testimony_id)
  return redirect('detail', case_id=case_id)


class CaseCreate(LoginRequiredMixin,CreateView):
  model = Case
  fields = ['name', 'date', 'location', 'description', 'news']

  def form_valid(self, form):
    # Assign the logged in user (self.request.user)
    form.instance.user = self.request.user  # form.instance is the cat
    # Let the CreateView do its job as usual
    return super().form_valid(form)
  
class CaseUpdate(LoginRequiredMixin,UpdateView):
  model = Case
  # Let's disallow the renaming of a cat by excluding the name field!
  fields = ['name', 'date', 'location', 'description', 'foia']

class CaseDelete(LoginRequiredMixin,DeleteView):
  model = Case
  success_url = '/cases'

@login_required
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
class add_testimony(LoginRequiredMixin,CreateView):
  model = Testimony
  fields = '__all__'

class TestimonyUpdate(LoginRequiredMixin,UpdateView):
  model = Testimony
  fields = ['date', 'name', 'location', 'comment']

class TestimonyDelete(LoginRequiredMixin,DeleteView):
  model = Testimony
  success_url = '/testimonies'

@login_required
def add_photo(request, case_id):
    # photo-file will be the "name" attribute on the <input type="file">
    photo_file = request.FILES.get('photo-file', None)
    if photo_file:
        s3 = boto3.client('s3')
        # need a unique "key" for S3 / needs image file extension too
        key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
        # just in case something goes wrong
        try:
            bucket = os.environ['S3_BUCKET']
            s3.upload_fileobj(photo_file, bucket, key)
            # build the full url string
            url = f"{os.environ['S3_BASE_URL']}{bucket}/{key}"
            # we can assign to cat_id or cat (if you have a cat object)
            Photo.objects.create(url=url, case_id=case_id)
        except Exception as e:
            print('An error occurred uploading file to S3')
            print(e)
    return redirect('detail', case_id=case_id) 

def signup(request):
  error_message = ''
  if request.method == 'POST':
    # This is how to create a 'user' form object
    # that includes the data from the browser
    form = UserCreationForm(request.POST)
    if form.is_valid():
      # This will add the user to the database
      user = form.save()
      # This is how we log a user in via code
      login(request, user)
      return redirect('index')
    else:
      error_message = 'Invalid sign up - try again'
  # A bad POST or a GET request, so render signup.html with an empty form
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)