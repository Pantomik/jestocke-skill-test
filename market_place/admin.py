
from django.contrib import admin

from market_place.models import StorageBox
from booking.models import Booking
from rangefilter.filters import DateRangeFilter, NumericRangeFilter


class BookingInline(admin.TabularInline):
    model = Booking
    fk_name = 'storage_box'

    def get_queryset(self, request):
        print(request)
        super().get_queryset(request)


class StorageBoxViewer(admin.ModelAdmin):
    list_filter = [('surface', NumericRangeFilter),
                   ('booking__start_date', DateRangeFilter),
                   ('booking__end_date', DateRangeFilter)]

    ordering = ('-creation_date',)
    inlines = [BookingInline]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        print(db_field, request, kwargs)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


admin.site.register(StorageBox, StorageBoxViewer)
