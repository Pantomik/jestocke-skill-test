from django.utils.translation import gettext_lazy as _


MAX_SURFACE = MAX_PRICE = 1 * (10 ** 15)
FILTER_TO_FIELD = {
    'price': 'monthly_price',
    'surface': 'surface',
    'create': 'creation_date'
}


class StorageTypes:
    GARAGE_BOX = "GARAGE_BOX"
    CELLAR = "CELLAR"
    ATTIC = "ATTIC"
    ROOM = "ROOM"
    HANGAR_WAREHOUSE = "HANGAR_WAREHOUSE"
    PARKING = "PARKING"

    choices = (
        (GARAGE_BOX, _("Garage")),
        (CELLAR, _("Cellar")),
        (ATTIC, _("Attic")),
        (ROOM, _("Room")),
        (HANGAR_WAREHOUSE, _("Hangar / Warehouse")),
        (PARKING, _("parking spot")),
    )
