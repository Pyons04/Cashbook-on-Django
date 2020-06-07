# coding=utf-8
from django.db import models

# Create your models here.i
class UsageMaster(models.Model):
    management_id = models.AutoField(verbose_name = "管理番号（自動付与）", primary_key = True)
    genre         = models.CharField(verbose_name = "ジャンル", null = True, blank = True, max_length = 100, unique=True)
    created_at    = models.DateTimeField(verbose_name = "作成日時", auto_now_add = True)

    class Meta: 
        verbose_name = "UsageMaster"

    def __str__(self):
        return str(self.genre)

class Usage(models.Model):
    management_id = models.AutoField(verbose_name = "管理番号（自動付与）", primary_key = True)
    date          = models.DateField(verbose_name = "支払日時", null = True, blank = True)
    genre         = models.ForeignKey(UsageMaster, verbose_name = "ジャンル", on_delete=models.PROTECT, null = False, blank = False)
    description   = models.TextField(null = False, blank = False)
    created_at    = models.DateTimeField(verbose_name = "作成日時", auto_now_add = True)
    amount        = models.IntegerField(verbose_name = "価格", null = False, blank = False, default = 0)
    class Meta:
        verbose_name = "Usage"

    def __str__(self):
        return str(self.description)


