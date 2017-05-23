from factory import django


class InstanceFactory(django.DjangoModelFactory):

    class Meta:
        model = 'core.Instance'
