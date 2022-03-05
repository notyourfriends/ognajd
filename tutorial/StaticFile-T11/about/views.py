from multiprocessing import context
from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        'judul':'Kelas Terbuka',
        'subjudul':'Static File',
        'kontributor':'Fuu',
        'nav': [
            ['/','Home'],
            ['/blog','Blog'],
            ['/about','About']
        ],
        'banner':'about/img/3.png',
    }

    return render(request, 'about/index.html', context)