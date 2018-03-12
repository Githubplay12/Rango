from django.http import HttpResponse

def index(request):
    return HttpResponse('Learning is never over ...')
