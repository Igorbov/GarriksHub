from django.db import models
 
class News(models.Model):
    id_news = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)
    link = models.CharField(max_length=100)
    rate = models.IntegerField()
    author = models.CharField(max_length=15)
    date = models.DateField()
    comm_count = models.IntegerField()

class Comment(models.Model):
    id_comment = models.AutoField(primary_key=True)
    text = models.CharField(max_length=255)
    id_child = models.ForeignKey('self', null = True, on_delete = models.CASCADE)
    id_news = models.ForeignKey(News, on_delete = models.CASCADE)