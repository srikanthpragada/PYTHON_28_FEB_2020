from django.http import HttpResponse


def hello(request):
    if 'name' in request.GET:
        name = request.GET['name']
    else:
        name = "Guest"

    return HttpResponse(f"<h1 style='color:blue'>Hello {name}</h1>")
