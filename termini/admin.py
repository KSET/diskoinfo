# -*- coding: utf-8 -*-
from django.contrib import admin

from termini.models import Shift
from termini.utils import week_dates

class ShiftAdmin(admin.ModelAdmin):
    list_display = ('date', 'category', 'user', 'name')
    search_fields = ('name',)

    list_filter = ['date', 'category', 'user__username']
    date_hierarchy = 'date'

    actions = ['create_curr_week', 'create_next_week']

    def create_curr_week(self, request, queryset):
        for date in week_dates():
            for cat in Shift.CATEGORIES:
                Shift.objects.get_or_create(date=date, category=cat[0])
    create_curr_week.short_description = 'Create empty shifts for current week'

    def create_next_week(self, request, queryset):
        for date in week_dates(week_offset=1):
            for cat in Shift.CATEGORIES:
                Shift.objects.get_or_create(date=date, category=cat[0])
    create_next_week.short_description = 'Create empty shifts for next week'

admin.site.register(Shift, ShiftAdmin)
