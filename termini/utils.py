# -*- coding: utf-8 -*-
from django.utils import timezone
from datetime import timedelta

def week_dates(day=None, week_offset=0):
    if day is None:
        day = timezone.now().date()
    monday = day + timedelta(days=-day.weekday(), weeks=week_offset)
    dates = [monday + timedelta(days=x) for x in range(0, 7)]
    return dates
