from factory import django


class RatingFactory(django.DjangoModelFactory):

    class Meta:
        model = 'core.Rating'
