from django.shortcuts import render

# Create your views here.


from .models import Post


def post_list(request):

    data = Post.objects.all()

    return render(request,'post_list.html',{'post':data})


def post_detail(request,post_id):

      data = Post.objects.get(id=post_id)

      return render(request,'post_detail.html',{'post':data})
