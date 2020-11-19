from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from blog.models import BlogPost, Imggal
from blog.forms import CreateBlogPostForm, UpdateBlogPostForm
from account.models import Account
from operator import attrgetter
from django.db.models import Q


def home(request):
	return render(request, 'blog/inicio/index.html')
def comprar(request):
	return render(request, 'blog/comprar/comprar.html')


def historiapag(request):
	return render(request, 'blog/historia/historia.html')
def blog(request):
	context={}
	query=""
	if request.GET:
		query = request.GET['q']
		context['query'] = str(query)

	blog_posts=sorted(get_blog_queryset(query), key=attrgetter('date_updated'), reverse=True)
	context['blog_posts'] = blog_posts
	return render (request, 'blog/blog_sector/blog_sector.html', context)

def create_blog_view(request):

	context = {}

	user = request.user

	if not user.is_authenticated:
		return redirect('must_authenticate')

	form = CreateBlogPostForm(request.POST or None, request.FILES or None)
	if form.is_valid():
		obj = form.save(commit=False)
		author = Account.objects.filter(email=user.email).first()
		obj.author = author
		obj.save()
		form = CreateBlogPostForm()
	context['form'] = form

	return render(request, 'blog/create/create_blog.html', context)

def detail_blog_view(request, slug):
	context = {}

	blog_post = get_object_or_404(BlogPost, slug=slug)
	context['blog_post'] = blog_post

	return render(request, 'blog/detail/detail_blog.html', context)

def edit_blog_view(request, slug):
	context ={}

	user = request.user
	if not user.is_authenticated:
		return redirect('must_authenticate')
	blog_post = get_object_or_404(BlogPost, slug=slug)
	if blog_post.author != user:
		return HttpResponse("No eres el autor de esta publicación.")
	if request.POST:
		form = UpdateBlogPostForm(request.POST or None, request.FILES or None, instance=blog_post)
		if form.is_valid():
			obj = form.save(commit=False)
			obj.save()
			context['success_message']="Se ha actualizado su publicación."
			blog_post = obj
	form = UpdateBlogPostForm(
		initial={
		"title": blog_post.title,
		"body": blog_post.body,
		"image": blog_post.image,
		}
	)
	context['form'] = form
	return render(request, 'blog/edit/edit_blog.html', context)

def galeriaimg(request):
	resultsdisplay=Imggal.objects.all()
	return render(request, 'blog/galeria/galeria.html',{'Imggal':resultsdisplay})

def medio_pago(request):
	return render(request, 'blog/comprar/medios_pago.html')

def get_blog_queryset(query=None):
	queryset =[]
	queries = query.split(" ") # creara una lista que dividira los términos ej:  ryzen 5600x [ryzen, 5600x], para buscarlos individualmente
	for q in queries:
		posts = BlogPost.objects.filter(
			Q(title__icontains=q)
			).distinct()
		for post in posts:
			queryset.append(post)
	return list(set(queryset))

