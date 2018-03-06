from django.contrib.syndication.views import Feed
from django.urls import reverse
from django.views.generic.list import ListView
from django.views.generic import DetailView

from django.conf import settings
from .models import BlogPost
from core.models.instance import Instance


class BlogPostsListView(ListView):

    model = BlogPost
    template_name = 'blog/post_list.html'
    paginate_by = 4

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(BlogPostsListView, self).get_context_data(**kwargs)
        # Add in the publisher
        context['instance'] = Instance.objects.get()
        return context

    def get_queryset(self, **kwargs):
        return BlogPost.published.all().order_by('-published_date')


class BlogPostDetailView(DetailView):

    model = BlogPost
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'


class LastBlogPostEntries(Feed):
    title = "%s blog." % (settings.SPOT_PROJECT_NAME.title())
    link = "/blog/"
    description = "The latest posts about %s friendly spots around" % (
        settings.SPOT_PROJECT_SUBJECT.lower())

    def items(self):
        return BlogPost.objects.order_by('-published_date')[:15]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.text

    def item_link(self, item):
        return reverse('blog:blogpost_detail', args=[item.post_slug, item.pk])
