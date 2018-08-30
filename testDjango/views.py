from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def hello(request):
    context = {'hello': "Hello World! This is a new test."}
    return render(request, 'hello.html', context)
    # return HttpResponse('Hello World!')