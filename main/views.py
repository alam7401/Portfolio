from django.shortcuts import render
from .models import Skill, Project, Education, Experience

def home(request):
    skills = Skill.objects.all()
    projects = Project.objects.order_by('order', '-featured')
    education = Education.objects.all()
    experience = Experience.objects.all()

    ctx = {
        'skills': skills,
        'projects': projects,
        'education': education,
        'experience': experience,
    }
    return render(request, 'main/home.html', ctx)
