from modeltranslation.translator import TranslationOptions, register

from .models import FrontPage


@register(FrontPage)
class FrontPageTranslationOptions(TranslationOptions):
    fields = (
        "hero_header",
        "hero_text",
        "about_header",
        "about_text",
        "why_us_header",
        "why_us_text",
        "more_info_header",
        "more_info_text",
    )
