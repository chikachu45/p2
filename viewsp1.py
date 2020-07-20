from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello world")#http response(HTML tag as an argument)

def home(request):
    return HttpResponse("<h1>Welcome to home page")