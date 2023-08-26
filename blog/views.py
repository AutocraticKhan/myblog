from django.shortcuts import render, get_object_or_404
from blog.models import Post
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger

# Create your views here.

def post_list(request):
    posts_queryset = Post.published.all()
    # Pagination with 3 posts per page
    paginator = Paginator(posts_queryset, 2)
    page_number = request.GET.get('page', 1)

    try:
        posts = paginator.page(page_number)

    except PageNotAnInteger:
        # If page_number is not an integer deliver the first page
        posts = paginator.page(1)


    except EmptyPage:
        # If page_number is out of range deliver last page of results
        posts = paginator.page(paginator.num_pages)

    return  render(request,
                         'blog/post/list.html',
                         {'posts': posts})

def post_details(request, year, month, day, post):
    post = get_object_or_404(Post,
                             status = Post.Status.PUBLISHED,
                             slug=post,
                             publish__year=year,
                             publish__month=month,
                             publish__day=day)
    return render(request,
                  'blog/post/details.html',
                         {'post': post})

