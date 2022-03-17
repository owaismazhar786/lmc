from django.shortcuts import render
from . models import Contact


def home(request):
    return render(request, 'main/index.html')


def about(request):
    return render(request, 'main/about.html')


def blog(request):
    return render(request, 'blog/blog.html')


def gallery(request):
    return render(request, 'main/gallery.html')


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
    return render(request, 'main/contact.html')


def privacy(request):
    return render(request, 'main/Privacypolicy.html')


def Terms(request):
    return render(request, 'main/Termsofuse.html')


def error_404(request, exception):
    return render('main/404.html')
