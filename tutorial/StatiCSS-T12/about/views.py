from django.shortcuts import render

# Create your views here.
def index(request):
	context = {
		'judul':'Tentang Kami',
		'kontributor': 'Fuu',
		'banner':'about/img/about.png',
		'app_css':'about/css/styles.css',
	}
	return render(request, 'about/index.html', context)