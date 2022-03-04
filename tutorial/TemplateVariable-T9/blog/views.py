from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        'judul':'blog',
        'kontributor': 'nii',
    }
    return render(request, 'blog/index.html', context)

from django.shortcuts import render

# Create your views here.
def news(request):
    context = {
        'judul':'news',
        'kontributor': 'rein',
    }
    return render(request, 'blog/index.html', context)


from django.shortcuts import render

# Create your views here.
def cerita(request):
    context = {
        'judul':'cerita',
        'kontributor': 'roni',
    }
    return render(request, 'blog/index.html', context)