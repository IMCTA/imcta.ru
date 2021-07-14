from django.contrib import admin
from modeltranslation.admin import TabbedTranslationAdmin

from .models import LandingPage


class LandingPageAdmin(TabbedTranslationAdmin):
    pass


admin.site.register(LandingPage, LandingPageAdmin)
