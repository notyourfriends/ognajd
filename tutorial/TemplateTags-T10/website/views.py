from multiprocessing import context
from django.shortcuts import render

def index(request):
    context = {
        'judul':'Kelas terbuka',
        'subjudul' : 'selamat datang',
        'kontributor':'fuu',
        'nav': [
            ['/','Home'],
            ['/blog','Blog'],
            ['/about','About'],
            ['/contact','Contact']
        ]
    }
    return render(request, 'index.html', context)