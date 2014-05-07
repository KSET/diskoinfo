# -*- coding: utf-8 -*-
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from zapisnik.models import LogEntry

@login_required
def logentry_list(request):
    entries = LogEntry.objects.filter(visible=True)
    return render(request, 'zapisnik/list.html', {
        'entries': entries,
    })
