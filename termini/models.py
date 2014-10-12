# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class Shift(models.Model):
    CATEGORIES  = ((1, u'Prvi'), (2, u'Drugi'), (3, u'Treći'), (4, u'Večernji'))

    name = models.CharField(max_length=100, default='', blank=True, null=True)
    date = models.DateField(default=timezone.now)
    category = models.IntegerField(choices=CATEGORIES)
    user = models.ManyToManyField(User, related_name='shifts', blank=True, null=True)
    usernum = models.IntegerField(default=1)

    class Meta:
        unique_together = ['date', 'category']
        ordering = ['-date', 'category']
        verbose_name = 'Shift'
        verbose_name_plural = 'Shifts'

    def get_users(self):
        return "<br />".join([usr.username for usr in self.user.all()])
    get_users.allow_tags = True

    def __unicode__(self):
        return self.date.strftime('Shift :: %Y-%m-%d') + ' %s :: %s' % (self.get_category_display(), self.user)
