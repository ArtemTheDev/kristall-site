from django.urls import path
from . import views
from .views import CreatePostView

app_name = 'tasks'

urlpatterns = [
    path('', views.news, name='news'),
    path('about',views.about, name='about'),
    path('create_news', CreatePostView.as_view(), name='create_news'),
    path('profile', views.profile, name='account_profile'),
    path('<slug:post><str:id>/',
         views.NewsPostDetail, name='post_detail'),
]