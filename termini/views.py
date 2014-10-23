# -*- coding: utf-8 -*-
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.shortcuts import render, redirect, get_object_or_404
from termini.models import Shift
from termini.utils import week_dates


@login_required
def shift_week(request):
    shifts = Shift.objects.filter(date__in=week_dates()).order_by('date', 'category')
    rows_curr = []
    for cat in Shift.CATEGORIES:
        row = [cat[1]] + [shifts.filter(category=cat[0])]
        rows_curr.append(row)

    shifts = Shift.objects.filter(date__in=week_dates(week_offset=1)).order_by('date', 'category')
    rows_next = []
    if len(shifts):
        for cat in Shift.CATEGORIES:
            row = [cat[1]] + [shifts.filter(category=cat[0])]
            rows_next.append(row)

    return render(request, 'termini/week.html', {
        'rows_curr': rows_curr,
        'rows_next': rows_next,
    })


@login_required
def shift_add_remove(request, shift_id):
    shift = get_object_or_404(Shift, id=shift_id)

    if shift.user.count() == shift.usernum and not shift.user.filter(username=request.user).exists():
        raise PermissionDenied
    elif shift.user.filter(username=request.user).exists():
        shift.user.remove(request.user)
    else:
        shift.user.add(request.user)

    shift.save()
    return redirect('termini:shift_week')
