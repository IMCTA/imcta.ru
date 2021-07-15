from django.contrib import admin
from modeltranslation.admin import TabbedTranslationAdmin
from solo.admin import SingletonModelAdmin

from .models import FrontPage


class FrontPageAdmin(TabbedTranslationAdmin, SingletonModelAdmin):
    pass


admin.site.register(FrontPage, FrontPageAdmin)
