from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post, Project, Category, Profile

def handler404(request, exception):
    return render(request, 'blog/404.html', status=404)

def handler500(request):
    return render(request, 'blog/500.html', status=500)

def home(request):
    featured_post = Post.objects.filter(is_published=True).order_by('-created_at').first()
    recent_posts = Post.objects.filter(is_published=True).order_by('-created_at')[1:3]
    featured_projects = Project.objects.filter(is_featured=True)[:3]
    categories = Category.objects.all()
    
    context = {
        'featured_post': featured_post,
        'recent_posts': recent_posts,
        'featured_projects': featured_projects,
        'categories': categories,
    }
    return render(request, 'blog/home.html', context)

class ArticleListView(ListView):
    model = Post
    template_name = 'blog/articles.html'
    context_object_name = 'posts'
    paginate_by = 6

    def get_queryset(self):
        queryset = Post.objects.filter(is_published=True)
        category_slug = self.kwargs.get('category_slug')
        if category_slug:
            queryset = queryset.filter(category__slug=category_slug)
        return queryset.order_by('-created_at')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context

class ArticleDetailView(DetailView):
    model = Post
    template_name = 'blog/article_detail.html'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['related_posts'] = Post.objects.filter(
            category=self.object.category,
            is_published=True
        ).exclude(id=self.object.id)[:3]
        return context

class ProjectListView(ListView):
    model = Project
    template_name = 'blog/projects.html'
    context_object_name = 'projects'
    paginate_by = 6

    def get_queryset(self):
        return Project.objects.all().order_by('-created_at')

def about(request):
    profile = Profile.objects.first()
    return render(request, 'blog/about.html', {'profile': profile})
