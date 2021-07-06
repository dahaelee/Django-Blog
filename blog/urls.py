from django.urls import path
from . import views


urlpatterns = [
    path('', views.post_list, name='post_list'),    # 홈 주소로 들어오면 views.post_list를 보여줌. name은 url의 이름
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
]
