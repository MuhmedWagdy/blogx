from django.shortcuts import render,redirect
from .forms import PostForm

# Create your views here.


from .models import Post


def post_list(request):

    data = Post.objects.all()

    return render(request,'post_list.html',{'post':data})


def post_detail(request,post_id):

      data = Post.objects.get(id=post_id)

      return render(request,'post_detail.html',{'post':data})



def post_new(request):
    if request.method == 'POST':         
          form = PostForm(request.POST,request.FILES)
          if form.is_valid():
              myform= form.save(commit=False)
              myform.author = request.user
              myform.save()
              return redirect('/blog')    
    else:
        form = PostForm()
    return render(request,'new_post.html',{'form':form})


def edit_post(request,post_id):
    data = Post.objects.get(id=post_id)
    if request.method == 'POST':         
          form = PostForm(request.POST,request.FILES,instance=data)
          if form.is_valid():
              myform= form.save(commit=False)
              myform.author = request.user
              myform.save()
              return redirect('/blog')        
    else:
        form = PostForm(instance=data)
    return render(request,'edit_post.html',{'form':form})

     



def delete_post(request,post_id):
     data = Post.objects.get(id=post_id)
     data.delete()
     return redirect('/blog')
     



