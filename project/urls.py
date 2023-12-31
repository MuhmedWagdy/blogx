"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

from blog.views import post_list,post_detail,post_new,edit_post,delete_post,PostList,PostDetail,PostCreate,PostUpdate,DeletePost
from blog.views import view_history


urlpatterns = [
    path('admin/', admin.site.urls),
    # path('blog/', post_list),
    path('blog/', PostList.as_view()),
    # path('blog/new', post_new),
    path('blog/new',PostCreate.as_view()),
    path('blog/<int:post_id>', post_detail),
    path('blog/<int:pk>', PostDetail.as_view()),
    # path('blog/<int:post_id>/edit', edit_post),

    path('blog/<int:pk>/edit', PostUpdate.as_view()),
    # path('blog/<int:post_id>/delete', delete_post),
    path('blog/<int:pk>/delete', DeletePost.as_view()),
    path('summernote/', include('django_summernote.urls')),
    path('history/<int:id>/', view_history, name='view_history'),
    
    

]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
  
 


