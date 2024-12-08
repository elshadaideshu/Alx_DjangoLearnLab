# blog/urls.py
from django.urls import path
from .views import register, user_login, user_logout, profile
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, comment_edit, comment_delete



urlpatterns = [
    path('', PostListView.as_view(), name='post-list'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('comment/<int:comment_id>/edit/', comment_edit, name='comment-edit'),  # Edit comment
    path('comment/<int:comment_id>/delete/', comment_delete, name='comment-delete'),  # Delete comment
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('profile/', profile, name='profile'),
]