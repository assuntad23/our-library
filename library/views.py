from django.http import HttpResponse

def landing_page(request):
    return HttpResponse("Welcome to Our Library!")