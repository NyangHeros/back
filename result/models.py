from django.db import models

class Results(models.Model):

    objects = models.Manager()

    name = models.CharField(max_length=64, verbose_name="이름")
    image = models.ImageField(verbose_name="이미지")
    created_at = models.DateTimeField(blank=True, auto_now_add=True)
    updated_at = models.DateTimeField(blank=True, auto_now=True)

    class Meta:
        db_table = 'result'
        verbose_name = '결과 목록'
        verbose_name_plural = '결과 목록'

    def __str__(self):
        return self.name
