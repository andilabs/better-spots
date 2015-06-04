from django.contrib.syndication.views import Feed
from django.core.urlresolvers import reverse
from django.views.generic.list import ListView
from django.views.generic import DetailView

from django.conf import settings
from .models import Post
from core.models import Instance


class BlogPostsListView(ListView):

    model = Post
    template_name = 'blog/post_list.html'
    paginate_by = 4

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(BlogPostsListView, self).get_context_data(**kwargs)
        # Add in the publisher
        context['instance'] = Instance.objects.get()
        return context

    def get_queryset(self, **kwargs):
        return Post.published.all().order_by('-published_date')


class BlogPostDetailView(DetailView):

    model = Post
    template_name = 'blog/post_detail.html'


class LastBlogPostEntries(Feed):
    title = "Dogspot blog."
    link = "/blog/"
    description = "The latest posts about %s friednly spots in Warsaw" % (
        settings.SPOT_PROJECT_SUBJECT.lower())

    def items(self):
        return Post.objects.order_by('-published_date')[:15]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.text

    def item_link(self, item):
        return reverse('blogpost_detail', args=[item.post_slug, item.pk])
