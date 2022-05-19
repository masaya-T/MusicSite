from django.db import models
from django.utils import timezone

class musicData(models.Model):
    album  =models.TextField()
    title  =models.TextField()
    artist =models.TextField()
    tracknumber=models.TextField()
    genre=models.TextField()
    date =models.TextField()
    path=models.TextField()

    class Meta:
        db_table = 'music_info'        # テーブル名を指定
