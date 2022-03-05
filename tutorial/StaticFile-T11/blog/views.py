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
        'banner':'blog/img/2.png',
    }
    return render(request, 'blog/index.html', context)