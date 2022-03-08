from django.shortcuts import render

# Create your views here.
def index(request):
	context = {
	'judul':'ini adalah home page about',
	'subjudul': 'mengatur semua isi dalam page about',
	'banner':'img/Assets/about.png',
	}
	return render(request, 'about/', context)