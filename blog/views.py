from django.contrib.syndication.views import Feed
from django.core.urlresolvers import reverse
from django.views.generic.list import ListView
from django.views.generic import DetailView

from .models import Post


class BlogPostsListView(ListView):

    model = Post
    template_name = 'post_list.html'
    paginate_by = 2

    def get_queryset(self):
        return Post.published.all().order_by('-published_date')


class BlogPostDetailView(DetailView):

    model = Post
    template_name = 'post_detail.html'


class LastBlogPostEntries(Feed):
    title = "Dogspot blog."
    link = "/blog/"
    description = "The latest posts about dog friednly spots in Warsaw"

    def items(self):
        return Post.objects.order_by('-published_date')[:15]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.text

    def item_link(self, item):
        return reverse('blogpost_detail', args=[item.post_slug, item.pk])
