from multiprocessing import context
from django.shortcuts import render

def index(request):
    context = {
        'judul':'Kelas Terbuka',
        'subjudul':'Static File',
        'kontributor':'Fuu',
        'nav': [
            ['/','Home'],
            ['/blog','Blog'],
            ['/about','About']
        ]
    }


    return render(request,'index.html', context)