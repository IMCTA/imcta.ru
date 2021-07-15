from django.contrib import admin
from modeltranslation.admin import TabbedTranslationAdmin

from .models import Tour


class TourAdmin(TabbedTranslationAdmin):
    pass


admin.site.register(Tour, TourAdmin)
