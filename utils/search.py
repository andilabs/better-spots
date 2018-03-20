from django.contrib.postgres.search import SearchVector
from django.db.models import Func

from core.models.spots import Spot
from utils.text import get_unaccented


def spots_full_text_search(search_term):
    unaccented_search_term = get_unaccented(search_term)
    spots_vector = SearchVector(
        Func('name', function='unaccent'),
        Func('address_street', function='unaccent'),
        Func('address_city', function='unaccent'),
        'tags__text'
    )

    return Spot.objects.annotate(
        search=spots_vector
    ).filter(
        search__icontains=unaccented_search_term
    ).distinct('pk')
