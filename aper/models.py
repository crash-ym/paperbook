from django.db import models

# Create your models here.
class PaperUser(models.Model):
    name = models.CharField('昵称',max_length=20,default='')
    passwd = models.CharField('密码',max_length=20,default='ad123456')
    email = models.EmailField(max_length=50,verbose_name='邮箱')