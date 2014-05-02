# -*- coding: utf-8 -*-
from django.db import models
from django.utils import timezone


class LogEntry(models.Model):
    text = models.TextField(blank=True, null=True)
    date = models.DateField(default=timezone.now)
    visible = models.BooleanField(default=True)

    class Meta:
        ordering = ['-date']
        verbose_name = 'Log Entry'
        verbose_name_plural = 'Log Entries'

    def __unicode__(self):
        return self.date.strftime('Log Entry :: %Y-%m-%d')

