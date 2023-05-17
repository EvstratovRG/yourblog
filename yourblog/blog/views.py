from django.views.generic import ListView
from django.shortcuts import get_object_or_404, render

from .models import Post


class PostListView(ListView):
    """Представление списка постов."""
    queryset = Post.objects.all()
    context_object_name = 'posts'
    paginate_by = 3
    template_name = 'blog/post/list.html'


def post_detail(request, year, month, day, post):
    post = get_object_or_404(
        Post,
        status=Post.Status.PUBLISHED,
        slug=post,
        publish__year=year,
        publish__month=month,
        publish__day=day
    )
    context = {'post': post}
    return render(request, 'blog/post/detail.html', context)
