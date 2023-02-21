from django.shortcuts import render
# from personal.models import Question
# from account.models import Account
from blog.models import BlogPost
from blog.views import get_blog_queryset
from django.core.pagination import EmptyPage,PageNoteAnInteger,Paginator
from operator import attrgetter
# Create your views here.
BLOG_POSTS_PER_PAGE=1
def home_screen_view(request):
    context = {}
    query=""
    if request.GET:
        query=request.GET.get('q','')
        context['query']=str(query)
    # accounts=Account.objects.all()
    # # context['some_string']="this is the some string i am passing to the view"
    # # context['some_number'] = 123223
    # # questions=Question.objects.all()
    # context['accounts']=accounts
    blog_posts=sorted(BlogPost.objects.all(),key=attrgetter('date_updated'),reverse=True )
    context['blog_posts']=blog_posts
    page = request.GET.get('page',1)
    blog_posts_paginator= Paginator(blog_posts,BLOG_POSTS_PER_PAGE)
    try:
        blog_posts =blog_posts_paginator.page(page)
    except PageNoteAnInteger:
        blog_posts =blog_posts_paginator.page(BLOG_POSTS_PER_PAGE)
    except EmptyPage:
        blog_posts =blog_posts_paginator.page(blog_posts_paginator.num_pages)
    context['blog_posts']=blog_posts


    return render(request,"personal/home.html",context)
