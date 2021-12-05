import urllib
from django.db import models
import os
from django.core.files import File
from urllib.request import urlopen
from tempfile import NamedTemporaryFile


class Results(models.Model):

    objects = models.Manager()

    name = models.CharField(max_length=64, verbose_name="이름")
    image = models.ImageField(upload_to='static/images/',blank=True, null=True, verbose_name="이미지")
    created_at = models.DateTimeField(blank=True, auto_now_add=True)
    updated_at = models.DateTimeField(blank=True, auto_now=True)

    class Meta:
        db_table = 'result'
        verbose_name = '결과 목록'
        verbose_name_plural = '결과 목록'

    def __str__(self):
        return self.name


class Photos(models.Model):

    objects = models.Manager()

    cat_image = models.ImageField(upload_to='static/images/' , verbose_name="이미지")
    image_url = models.URLField()
    created_at = models.DateTimeField(blank=True, auto_now_add=True)
    updated_at = models.DateTimeField(blank=True, auto_now=True)

    class Meta:
        db_table = 'photo'
        verbose_name = '이미지 목록'
        verbose_name_plural = '이미지 목록'

    def save(self, *args, **kwargs):
        if self.image_url and not self.cat_image:
            img_temp = NamedTemporaryFile(delete=True)
            img_temp.write(urlopen(self.image_url).read())
            img_temp.flush()
            self.cat_image.save(f"image_{self.pk}", File(img_temp))
        super(Photos, self).save(*args, **kwargs)
