from django.conf.urls import *
from blog.views import BlogPostsListView

# place app url patterns here
urlpatterns = patterns(
    '',
    url(r'^$', BlogPostsListView.as_view(), name='blogpost-list'),
)