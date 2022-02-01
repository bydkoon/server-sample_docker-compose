from django.conf.urls import include
from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import (
    ArticleViewSet, ArticlesFavoriteAPIView, ArticlesFeedAPIView,
    CommentsListCreateAPIView, CommentsDestroyAPIView, TagListAPIView
)

router = DefaultRouter(trailing_slash=False)
router.register(r'articles', ArticleViewSet)

urlpatterns = [
    path(r'^', include(router.urls)),

    path(r'^articles/feed/?$', ArticlesFeedAPIView.as_view()),

    path(r'^articles/(?P<article_slug>[-\w]+)/favorite/?$',
        ArticlesFavoriteAPIView.as_view()),

    path(r'^articles/(?P<article_slug>[-\w]+)/comments/?$',
        CommentsListCreateAPIView.as_view()),

    path(r'^articles/(?P<article_slug>[-\w]+)/comments/(?P<comment_pk>[\d]+)/?$',
        CommentsDestroyAPIView.as_view()),

    path(r'^tags/?$', TagListAPIView.as_view()),
]