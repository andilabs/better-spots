from django.conf.urls import *
from blog.views import BlogPostsListView, BlogPostDetailView

# place app url patterns here
urlpatterns = patterns(
    '',
    url(r'^$', BlogPostsListView.as_view(), name='blogpost_list'),
    url(r'^(?P<pk>\d+)/$', BlogPostDetailView.as_view(), name='blogpost_detail'),
    url(r'^(?:(?P<post_slug>[^\.]+))?/(?P<pk>\d+)$', BlogPostDetailView.as_view(), name='blogpost_detail'),
)