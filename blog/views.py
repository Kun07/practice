from django.shortcuts import render


posts= [

		{

		'author': 'kunal',
		'title' : 'Blog post 1',
		'content': 'First post content',
		'date_posted': 'Mar 23, 2021'

		},

		{

		'author': 'corey',
		'title' : 'Blog post 2',
		'content': 'second post content',
		'date_posted': 'Mar 24, 2021'

		}

]

def home(request):
	context = {
		'posts' : posts
	}
	return render(request, 'blog/home.html', context)

def about(request):
	return render(request, 'blog/about.html', {'title': 'about'})