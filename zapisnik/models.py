# -*- coding: utf-8 -*-
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


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


class LogComment(models.Model):
    log_entry = models.ForeignKey(LogEntry)
    comment_text = models.CharField(max_length=500)
    author = models.ForeignKey(User)

    def __unicode__(self):
        return self.author.join(" ").join(self.comment_text)
