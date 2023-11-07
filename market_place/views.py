
from datetime import date

from django.shortcuts import render
from django.core.exceptions import BadRequest

from market_place.models import StorageBox
from market_place.constants import MAX_PRICE, MAX_SURFACE, FILTER_TO_FIELD


def available_boxes(request):
    try:
        since = request.GET.get('since', None)
        if since is not None:
            since = date.fromisoformat(since)
        until = request.GET.get('until', None)
        if until is not None:
            until = date.fromisoformat(until)
        max_price = int(request.GET.get('max-price', MAX_PRICE))
        min_price = int(request.GET.get('min-price', 0))
        max_surface = int(request.GET.get('max-surface', MAX_SURFACE))
        min_surface = int(request.GET.get('min-surface', 0))
        if min_price > max_price or min_surface > max_surface:
            raise ValueError
        sorting = request.GET.get('sort', None)
        ordering = request.GET.get('order', 'asc') != 'desc'
        if sorting is not None:
            if (sorting := FILTER_TO_FIELD.get(sorting, None)) is None:
                raise ValueError
    except ValueError:
        raise BadRequest
    if since is None:
        boxes = StorageBox.objects.all()
    else:
        boxes = StorageBox.get_available(since, until)
    boxes.filter(monthly_price__gte=min_price, monthly_price__lte=max_price,
                 surface__gte=min_surface, surface__lte=max_surface)
    if sorting is not None:
        if not ordering:
            sorting = f'-{sorting}'
        boxes = boxes.order_by(sorting)
    return render(request, 'available.html', context={'boxes': boxes})
