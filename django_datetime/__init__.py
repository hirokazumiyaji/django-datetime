# coding: utf-8

import datetime as basedatetime

from django.conf import settings
from django.utils.timezone import get_default_timezone
import pytz


class datetime(basedatetime.datetime):

    @classmethod
    def now(cls, tzinfo=None):
        now = cls._timezone(tzinfo).normalize(pytz.utc.localize(cls.utcnow()))
        if hasattr(settings, 'DJANGO_SETTINGS_TIMEDELTA'):
            if isinstance(settings.DJANGO_SETTINGS_TIMEDELTA, basedatetime.timedelta):
                return now + settings.DJANGO_SETTINGS_TIMEDELTA
        return now

    @classmethod
    def _timezone(cls, tzinfo):
        return get_default_timezone() if tzinfo is None else tzinfo


date = basedatetime.date
timedelta = basedatetime.timedelta
time = basedatetime.time
tzinfo = basedatetime.tzinfo
