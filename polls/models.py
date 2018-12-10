import datetime
from django.db import models
from django import forms
from django.utils import timezone

# Create your models here.


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
        was_published_recently.admin_order_field = 'pub_date'
        was_published_recently.boolean = True
        was_published_recently.short_description = 'Published recently?'


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text



#这个方法可以定义上传文件的目录和名字。如果通过
def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'uploads/%Y%m%d-{0}'.format(filename)

class FileModel(models.Model):
    title = models.CharField(max_length=50)
    file = models.FileField(upload_to=user_directory_path)




from django.db import models
class Imgs(models.Model):
    id = models.AutoField(max_length=10, primary_key=True, verbose_name='id')
    img = models.ImageField(upload_to='./imgs/',verbose_name='图片地址')
    single = models.CharField(max_length=20,null=True, blank=True,verbose_name='图片名称')
    def __unicode__(self):  # __str__ on Python 3
        return (self.id,self.img)

    def __str__(self):
        return str(self.single)

class Imgs_name(models.Model):
    id = models.AutoField(max_length=10, primary_key=True, verbose_name='id')
    name = models.CharField(max_length=10,verbose_name='图片库名称')
    imgs = models.ManyToManyField(Imgs, related_name='imgs',verbose_name='图片表')


    def __unicode__(self):  # __str__ on Python 3
        return (self.id,self.name,self.imgs)

    def __str__(self):
        return self.name
