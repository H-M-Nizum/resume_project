from django.shortcuts import render

# Create your views here.
def skillsview(request):
    return render(request, 'skills/skill.html')