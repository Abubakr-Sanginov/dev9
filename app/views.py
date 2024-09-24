from django.shortcuts import render

def index(request):
    data={
        'title': 'Главная страница'
    }
    return render(request, 'app/index.html', data)


def about(request):
    return render(request, 'app/about.html')

def contacts(request):
    return render(request, 'app/contacts.html')
