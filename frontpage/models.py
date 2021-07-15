from django.db import models
from solo.models import SingletonModel


class FrontPage(SingletonModel):
    hero_header = models.CharField(max_length=127, verbose_name="Заголовок слайдера")
    hero_text = models.CharField(max_length=255, verbose_name="Текст слайдера")
    about_header = models.CharField(
        max_length=127, verbose_name="Заголовок раздела 'О нас''"
    )
    about_text = models.TextField(verbose_name="Текст раздела 'О нас'")
    about_photo = models.ImageField(
        upload_to="frontpage/", verbose_name="Фото для раздела 'О нас'"
    )
    why_us_header = models.CharField(
        max_length=127, verbose_name="Заголовок раздела 'Почему мы'"
    )
    why_us_text = models.TextField(verbose_name="Текст раздела 'Почему мы'")
    more_info_header = models.CharField(
        max_length=127, blank=True, verbose_name="Заголовок раздела 'Дополнительно''"
    )
    more_info_text = models.TextField(
        blank=True, verbose_name="Текст раздела 'Дополнительно'"
    )
    more_info_photo = models.ImageField(
        blank=True,
        upload_to="frontpage/",
        verbose_name="Фото для раздела 'Дополнительно'",
    )

    def __str__(self):
        return self.hero_header_ru
