# -*- coding: utf-8 -*-
from django.shortcuts import render
from zapisnik.models import LogEntry


def logentry_list(request):
    entries = LogEntry.objects.filter(visible=True)
    return render(request, 'zapisnik/list.html', {
        'entries': entries,
    })
