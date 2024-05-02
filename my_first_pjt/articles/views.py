from django.shortcuts import render
from .models import Product
from rest_framework import generics
from .models import Post
from .serializers import PostSerializer


def index(request):
    products = Product.objects.all()[:3]  # 최신 3개 상품만

    context = {
        'products': products,
    }
    return render(request, 'index.html', context)

def search(request):
    keyword = request.GET.get('keyword')
    if keyword:
        products = Product.objects.filter(name__icontains=keyword)
    else:
        products = None

    context = {
        'products': products,
        'keyword': keyword,
    }
    return render(request, 'index.html', context)

# blog/views.py

class PostList(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostDetail(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    lookup_field = 'pk'
