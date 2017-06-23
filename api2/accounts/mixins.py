
class ObjectInUserContextMixin(object):
    def validate(self, attrs):
        attrs['user_id'] = self.context['view'].kwargs['user_pk']
        return attrs
