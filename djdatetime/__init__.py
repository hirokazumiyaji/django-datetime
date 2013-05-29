# coding: utf-8

import datetime as basedatetime

from django.conf import settings


class datetime(basedatetime):

    @classmethod
    def now(cls, tz=None):
        now = basedatetime.datetime.now()
        if hasattr(settings, 'DJANGO_SETTINGS_TIMEDELTA'):
            if isinstance(settings.DJANGO_SETTINGS_TIMEDELTA, basedatetime.timedelta):
                return now + settings.DJANGO_SETTINGS_TIMEDELTA
        return now


timedelta = basedatetime.timedelta
time = basedatetime.time
tzinfo = basedatetime.tzinfo
