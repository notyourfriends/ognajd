from django.shortcuts import render

def index(request):
	context = {
		'judul':'Kelas Terbuka',
		'subjudul': 'Static File + CSS',
		'kontri':'Fuu',
		'banner':'static/img/home.png',

	}
	return render(request, 'index.html', context)