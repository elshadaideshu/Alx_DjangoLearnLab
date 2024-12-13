# posts/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CommentViewSet
from .views import FeedView

router = DefaultRouter()
router.register(r'feed', FeedView, basename='feed')


router = DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'comments', CommentViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('feed/', PostFeedView.as_view(), name='post_feed'),
    path('', include(router.urls)),
]