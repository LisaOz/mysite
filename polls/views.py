from django.http import HttpResponse


# Create views here
def index(request):
    return HttpResponse("You are at the polls index.")