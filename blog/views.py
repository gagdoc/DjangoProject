from django.shortcuts import render
from django.views.generic import ListView
from .models import Post

# Create your views here.

class PostList(ListView): #ListView를 확장해서(상속)
    model = Post # 모델을 선택 , Post 라는 모델을 선택하고
    ordering = '-pk' #내림 차순으로 정렬



# def index(request):
#     posts = Post.objects.all().order_by('-pk');
#     return render (
#         request,
#         'blog/index.html',
#         {
#             'posts' : posts,
#         }
#     )

def single_post_page(request,pk):
    post=Post.objects.get(pk=pk)
    return render(
        request,
        'blog/single_page.html',
        {
            'post' : post,
        }
    )
