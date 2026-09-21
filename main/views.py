from django.shortcuts import render
from django.http import FileResponse, Http404
from django.conf import settings
from .models import Skill, Project, Education, Experience
import os

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

def resume_download(request):
    """Serve the resume PDF as a downloadable file."""
    resume_path = os.path.join(settings.MEDIA_ROOT, 'resume', 'Tauqeer_Alam_Resume.pdf')
    if not os.path.exists(resume_path):
        resume_path = os.path.join(settings.STATIC_ROOT or settings.STATICFILES_DIRS[0], 'resume', 'Tauqeer_Alam_Resume.pdf')
    if not os.path.exists(resume_path):
        raise Http404("Resume not found")
    response = FileResponse(open(resume_path, 'rb'), content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="Tauqeer_Alam_Resume.pdf"'
    return response
