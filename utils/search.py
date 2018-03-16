from django.contrib.postgres.search import SearchQuery, SearchRank, SearchVector, TrigramSimilarity
# spots config
from core.models.spots import Spot


def spots_full_text_search(search_term):
    # weights D, C, B, A. By default, these weights refer to the numbers 0.1, 0.2, 0.4, and 1.0,
    # TODO https://docs.djangoproject.com/en/2.0/ref/contrib/postgres/search/
    # TODO read these https://czep.net/17/full-text-search.html and improve
    spots_vector = SearchVector('name', weight='A') + SearchVector('address_street', weight='B') + \
                   SearchVector('address_city', weight='B') + SearchVector('tags__text', weight='C')

    spots_query = SearchQuery(search_term)

    return Spot.objects.annotate(
        rank=SearchRank(spots_vector, spots_query),
    ).filter(
        rank__gte=0.3,
    ).order_by(
        'pk',
        'spot_type',
        '-rank'
    ).distinct('pk')
