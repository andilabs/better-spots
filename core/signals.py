# from core.models.spots import SPOT_TYPE_CHOICES, Spot
from utils.geocoding import reverse_geocoding

# from django.db.models.signals import post_save
# from django.dispatch import receiver
from django.template.defaultfilters import slugify


# @receiver(post_save, sender='core.Spot')
def fill_address_based_on_reverse_geocoding(sender, instance, created, **kwargs):
    longitude, latitude = instance.location.coords
    address_info = reverse_geocoding(latitude=latitude, longitude=longitude)
    sender.objects.filter(
        pk=instance.pk
    ).update(
        address_number=address_info.get('address_number'),
        address_street=address_info.get('address_street'),
        address_city=address_info.get('address_city'),
        address_country=address_info.get('address_country'),
        spot_slug=slugify(
            "{} {} {} {}".format(
                name=instance.name,
                # spot_type=dict(SPOT_TYPE_CHOICES)[instance.spot_type],
                city=address_info.get('address_city'),
                street=address_info.get('address_street'),
                address_number=address_info.get('address_number')
            )
        )
    )
