from django.db import models

from django.db.models import indexes


class Feed(models.Model):
    content = models.TextField()
    image = models.TextField()
    profile_image = models.TextField()
    nickname = models.TextField()

class Reply(models.Model):
    feed_id = models.IntegerField()
    nickname = models.TextField()
    content = models.TextField()

class Like(models.Model):
    feed_id = models.IntegerField()
    email = models.TextField()
    # 한 피드에 대해 여러번 좋아요를 누를 수 없도록 아래 메타데이터를 구성합니다.
    class Meta:
        unique_together = ('feed_id', 'email')
        # db_table = 'likes' --> Meta Data에서 이름 지정도 가능

class Bookmark(models.Model):
    feed_id = models.IntegerField()
    email = models.TextField()
    # 한 피드에 대해 여러번 좋아요를 누를 수 없도록 아래 메타데이터를 구성합니다.
    class Meta:
        unique_together = ('feed_id', 'email')