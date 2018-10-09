from django.urls import path
from . import views


app_name = 'blogs'

urlpatterns = [
    path('', views.blogs, name='index'),
    path('blog/<int:blog_id>', views.blog, name='blog'),
    path('new_blog/', views.new_blog, name='new_blog'),
    path('edit_blog/<int:edit_id>/', views.edit_blog, name='edit_blog'),
]