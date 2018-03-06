from factory import django


class TagFactory(django.DjangoModelFactory):

    class Meta:
        model = 'utils.Tag'
