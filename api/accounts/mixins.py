from django.shortcuts import get_object_or_404

from accounts.models import User


class ObjectInUserContextMixin(object):

    def validate(self, attrs):
        attrs['user'] = get_object_or_404(User, pk=self.context['view'].kwargs['user_pk'])
        return attrs
