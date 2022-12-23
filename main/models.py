from django.db import models

class Section(models.Model):
    theme = models.CharField('Theme', max_length=50)
    sub_theme = models.CharField('Subtheme', max_length=50)
    image = models.ImageField(upload_to='images/', null=True, blank=True)

    def __str__(self):
        return self.theme

    class Meta:
        verbose_name = 'Section'
        verbose_name_plural = 'Sections'


class Themes(models.Model):
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    heading = models.CharField('Heading', max_length=50)
    main_text = models.TextField('Main text', max_length=10000)

    def __str__(self):
        return self.heading

class Sport(Themes):
    class Meta:
        verbose_name = 'Sport'
        verbose_name_plural = 'Sport'

class Architecture(Themes):
    class Meta:
        verbose_name = 'Architecture'
        verbose_name_plural = 'Architecture'

class Music(Themes):
    class Meta:
        verbose_name = 'Music'
        verbose_name_plural = 'Music'

class Politics(Themes):
    class Meta:
        verbose_name = 'Politics'
        verbose_name_plural = 'Politics'

class Tech(Themes):
    class Meta:
        verbose_name = 'Technology'
        verbose_name_plural = 'Technology'