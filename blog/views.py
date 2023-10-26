from django.shortcuts import render,redirect
from .forms import PostForm,CommentForm
# Create your views here.
from .models import Post,Comment

from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView

from django.contrib.auth.mixins import LoginRequiredMixin

  


def post_list(request):
    
    data = Post.objects.all()
    return render(request,'post_list.html',{'post':data})


class PostList(ListView):
     model = Post
# ===============================================================================================================================================================

def post_detail(request,post_id):
      
      data = Post.objects.get(id=post_id)
      post_comment = Comment.objects.filter(post=data)
      if request.method == "POST":
           form=CommentForm(request.POST)
           if form.is_valid():            
                myform = form.save(commit=False)
                myform.user = request.user
                myform.post = data
                myform.save()
      else:         
        form = CommentForm()
      return render(request,'blog/post_detail.html',{'post':data,'form': form,'post_comment':post_comment})


class PostDetail(DetailView):
     model = Post
     

#===================================================================================================================================================================

def view_history(request, id):
    my_model_instance = Post.objects.get(id=id)
    history = my_model_instance.history.all()
    return render(request, 'blog/history.html', {'history': history,'my_model_instance':my_model_instance})




# ===================================================================================================================================================================
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


class PostCreate(CreateView):
     model = Post
     fields = ['title','content','created_date','draft','tags','author','image']

     success_url = '/blog'



#===========================================================================================================================================================
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




class PostUpdate(UpdateView):
     model = Post
     fields = ['title','content','created_date','draft','tags','author','image']
     success_url = '/blog'

     template_name='blog/edit_post.html'
#============================================================================================================================================================================

def delete_post(request,post_id):
     data = Post.objects.get(id=post_id)
     data.delete()
     return redirect('/blog')


class DeletePost(DeleteView):
     model = Post
     success_url = '/blog'

     



