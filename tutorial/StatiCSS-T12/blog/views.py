from django.shortcuts import render

# Create your views here.
def index(request):
	context = {
		'judul':' Blog',
		'subjudul':'recent post',
		'banner': 'blog/img/blog.png',
		'app_css':'blog/css/styles.css',
	}
	return render(request, 'blog/index.html',context)