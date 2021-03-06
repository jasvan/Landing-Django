from django.shortcuts import render
from .models import Project

# Create your views here.
def all_projects(request):
    projects = Project.objects.all()
    filtered = ProjectFilter(request.GET, queryset=projects)
    projects = filtered.qs

    context = {
        'projects':projects,
        'filtered':filtered
    }
    return render(request, 'all_projects.html', context)

def project_detail(request, project_id):
    project = get_object_or_404(Project, id=project_id)

    context = {
        'project':project
    }
    return render(request, 'project_detail.html', context)