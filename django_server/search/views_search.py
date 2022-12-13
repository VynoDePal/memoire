import io

from django.http import FileResponse
from django.shortcuts import render
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.pdfgen import canvas

from .models import Archive
from django.db.models import Q
# Create your views here.

def Accueil_de_recherche(request):
    recherche_archive = request.GET.get('recherche')
    if recherche_archive:
        archives = Archive.objects.filter(Q(code_archive__icontains=recherche_archive) | Q(intitulé_archive__icontains=recherche_archive) | Q(nature__icontains=recherche_archive))

    else:
    # If not searched, return default posts
    # posts = Post.objects.all()
        archives = Archive.objects.all().order_by('-date_creation')

    # if request.method == 'POST':
    #     new_img =Post(
    #      science_image = request.FILES['pic']
    #     )
    #     new_img.save()

    return render (request,'home.html', {'archives':archives},)

def index(request):
    return render(request, 'index.html')

def barred_search(request):
    recherche_archive = request.GET.get('recherche')
    if recherche_archive:
        archives = Archive.objects.filter(
            Q(code_archive__icontains=recherche_archive) | Q(intitulé_archive__icontains=recherche_archive) | Q(
                nature__icontains=recherche_archive))

    else:
        # If not searched, return default posts
        # posts = Post.objects.all()
        archives = Archive.objects.all().order_by('-date_creation')

    # if request.method == 'POST':
    #     new_img =Post(
    #      science_image = request.FILES['pic']
    #     )
    #     new_img.save()

    return render(request, 'home.html', {'archives': archives}, )