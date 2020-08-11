from django.db import models
class Blog(models.Model):
    title = models.CharField(unique = True, max_length = 50, verbose_name = 'Title') #最多255字
    content = models.TextField(verbose_name = 'Content') #沒有限制字數
    editTime = models.DateTimeField(auto_now = True, verbose_name = 'Edit Time') # auto_now=true是自動記錄更新當下的時間
# Create your models here.
