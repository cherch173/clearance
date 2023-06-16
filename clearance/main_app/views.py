from django.shortcuts import render

cases = [
  {'name':'USS Nimtiz - Tic Tac Incident', 'date':'11/14/2004', 'location':'Pacific Ocean (Southern Cali)', 'description': 'Commander David Fravor was engaged by an unidentified aircraft which attempted to merge plot his aircraft. The UAP was described as a long white cylindrical object traveling at approx. 3000/mph and was able to change direction and altitude instantaneously. It is known as the Tic Tac Incident.', 'declassified': 'True', 'foia': 'https://www.theblackvault.com/documentarchive/' },
]
# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def cases_index(request):
  # We pass data to a template very much like we did in Express!
  return render(request, 'cases/index.html', {
    'cases': cases
  })