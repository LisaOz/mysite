from django.http import HttpResponse


# Create views here
def index(request):
    return HttpResponse("Hello, world. You are at the polls index.")