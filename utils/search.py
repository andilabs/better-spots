from django.contrib.postgres.search import SearchVector, TrigramSimilarity
from django.db.models import Func, Q

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
        search=spots_vector,
        similarity=TrigramSimilarity(Func('name', function='unaccent'), unaccented_search_term)
    ).filter(
        Q(search__icontains=unaccented_search_term) |
        Q(similarity__gt=0.2)
    ).order_by('pk', '-similarity').distinct('pk')
