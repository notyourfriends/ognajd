from django.shortcuts import render

# Create your views here.
def index(request):
	context = {
	'judul':'ini adalah home page blog',
	'subjudul': 'mengatur semua isi dalam page blog',
	'banner':'img/Assets/blog.png',
	}
	return render(request, 'blog/index.html', context)