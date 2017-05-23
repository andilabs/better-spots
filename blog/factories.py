import factory

from blog.models import BlogPost


class InstanceFactory(factory.Factory):

    class Meta:
        model = BlogPost

