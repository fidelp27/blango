from django.shortcuts import render, get_object_or_404
from datetime import datetime  # Importa datetime para obtener la fecha actual
from blog.models import Post

# Create your views here.
def index(request):
  now = datetime.now()
  posts = Post.objects.filter(published_at__lte=now)
  return render(request, "blog/index.html", {"posts": posts})

def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, "blog/post-detail.html", {"post": post})

