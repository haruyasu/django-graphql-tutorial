from django.db import models

class Post(models.Model):
  channel_name = models.CharField("チャンネル名", max_length=255)
  caption = models.TextField("説明")
  video_url = models.URLField("動画URL", max_length=255) # TODO: クラウドに保存
  music_name = models.CharField("音楽名", max_length=255)
  created_at = models.DateTimeField("作成日", auto_now_add=True)

  class Meta:
    verbose_name = "投稿"
    verbose_name_plural = "投稿"

  def __str__(self):
    return self.channel_name
