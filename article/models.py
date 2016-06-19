from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Article(models.Model) :
    title = models.CharField(max_length = 100)  
    category = models.CharField(max_length = 50, blank = True)  
    date_time = models.DateTimeField(auto_now_add = True)
    shortContent = models.CharField(max_length = 100,blank = True, null = True)
    content = models.TextField(blank = True, null = True)

#获取URL并转换成url的表示格式
    def get_absolute_url(self):
        path = reverse('detail', kwargs={'id':self.id})
        return "http://crazyc.cn%s" % path

    def __unicode__(self) :
        return self.title

    class Meta:  
        ordering = ['-date_time']
