from factory import django


class OpinionFactory(django.DjangoModelFactory):

    class Meta:
        model = 'core.Opinion'
