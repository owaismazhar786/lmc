from django.shortcuts import render
from django.http import HttpResponse
from . models import *


def home(request):
    return render(request, 'main/index.html')


def about(request):
    return render(request, 'main/about.html')


def blog(request):
    return render(request, 'blog/blog.html')


def gallery(request):
    videos = Video.objects.all()
    context = {'videos': videos}
    return render(request, 'main/gallery.html', context)


def service(request):
    return render(request, 'main/service.html')


def contact(request):
    if request.method == 'POST':
        contact = Contact()
        name = request.POST.get('username')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('usermessage')
        contact.name = name
        contact.email = email
        contact.subject = subject
        contact.message = message
        contact.save()
        return render(request, 'main/thanks.html')
    return render(request, 'main/contact.html')

def developer(request):
    if request.method == 'POST':
        contact = Developer()
        name = request.POST.get('username')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('usermessage')
        contact.name = name
        contact.email = email
        contact.subject = subject
        contact.message = message
        contact.save()
        return render(request, 'main/thanks.html')
    return render(request, 'main/developer.html')


def privacy(request):
    return render(request, 'main/Privacypolicy.html')


def Terms(request):
    return render(request, 'main/Termsofuse.html')


def page_404(request, exception):
    return render(request,'main/404.html')
