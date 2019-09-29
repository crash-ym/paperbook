from django.db import models

# Create your models here.
class PaperUser(models.Model):
    name = models.CharField('昵称',max_length=20,default='')
    passwd = models.CharField('密码',max_length=20,default='ad123456')
    email = models.EmailField(max_length=50,verbose_name='邮箱')

class TagBook(models.Model):
    tagId = models.BinaryField('TAGid',max_length=8,default='')
    tagBid = models.CharField('TAGBid',max_length=8,default='')
    tagName = models.CharField('标签',max_length=8,default='默认')

class Author(models.Model):
    authorName = models.CharField('作家名字',max_length=50,default='')
    contry = models.CharField('国籍',max_length=20,default='Earth')
    describ = models.CharField('描述',max_length=500,default='暂无简介')
    masterpiece = models.CharField('代表作',max_length=200,default='暂无记录')
    link = models.CharField('详细链接',max_length=100,default='暂无链接')

class BookInfo(models.Model):
    bookName = models.CharField('书名',max_length=50,default='')
    authorName = models.CharField('作者',max_length=50,default='佚名')
    bookTag = models.CharField('标签',max_length=8,default='暂无标签')
    bookLink = models.CharField('链接',max_length=200,default='暂无链接')
    bookDes = models.CharField('书籍描述',max_length=500,default='暂无描述')