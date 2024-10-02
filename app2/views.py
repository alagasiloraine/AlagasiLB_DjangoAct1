from django.shortcuts import render

# Create your views here.
def contact(request):
    return render(request, 'app2/contact.html')

def galleries(request):
    return render(request, 'app2/galleries.html')

def profile(request):
    return render(request, 'app2/profile.html')
