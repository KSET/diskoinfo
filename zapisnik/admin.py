# -*- coding: utf-8 -*-
from django import forms
from django.contrib import admin
from django.core.urlresolvers import reverse
from django.template.defaultfilters import truncatewords
from tinymce.widgets import TinyMCE
from zapisnik.models import LogEntry

class LogEntryAdmin(admin.ModelAdmin):
    def formfield_for_dbfield(self, db_field, **kwargs):
        if db_field.name == 'text':
            return forms.CharField(label=db_field.name.title(), widget=TinyMCE(
                mce_attrs={'external_link_list_url': reverse('tinymce.views.flatpages_link_list')},
            ))
        return super(LogEntryAdmin, self).formfield_for_dbfield(db_field, **kwargs)

    def text_preview(self, obj):
        return truncatewords(obj.text, 20)
    text_preview.allow_tags = True
    text_preview.short_description = 'Text'
    text_preview.admin_order_field  = 'text'

    list_display = ('date', 'text_preview', 'visible')
    search_fields = ('text',)

    list_filter = ['date', 'visible',]
    date_hierarchy = 'date'

    actions = ['make_visible', 'make_invisible']

    def make_visible(self, request, queryset):
        queryset.update(visible=True)
    make_visible.short_description = 'Set selected log entries as Visible'

    def make_invisible(self, request, queryset):
        queryset.update(visible=False)
    make_invisible.short_description = 'Set selected log entries as Not Visible'

admin.site.register(LogEntry, LogEntryAdmin)
