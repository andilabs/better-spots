from django.conf.urls import url
from blog.views import (
    BlogPostsListView, BlogPostDetailView, LastBlogPostEntries
)


urlpatterns = [

    url(r'^$', BlogPostsListView.as_view(), name='blogpost_list'),

    url(r'^(?P<pk>\d+)/$', BlogPostDetailView.as_view(), name='blogpost_detail'),

    url(r'^(?:(?P<post_slug>[^\.]+))?/(?P<pk>\d+)/$', BlogPostDetailView.as_view(), name='blogpost_detail'),

    url(r'^latest/feed/$', LastBlogPostEntries(), name='blog_rss'),
]
