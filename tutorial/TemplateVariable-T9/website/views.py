from django.shortcuts import render

def index(request):
    context = {
        'judul':'Kelas Terbuka',
        'kontributor': 'fuu',
    }
    return render(request, 'index.html', context)

