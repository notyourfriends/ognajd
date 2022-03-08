from django.shortcuts import render

def index(request):
	context = {
	'judul':'Kelas Terbuka',
	'subjudul':'Tutorial Static File dan Bootstrap',
	'banner':'img/Assets/rari.png',	
	}
	return render(request, 'index.html', context)