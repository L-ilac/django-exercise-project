from django.db import models

from users.models import User
# Create your models here.

# 이건 고정


class Article(models.Model):
    title = models.CharField(max_length=30)
    text = models.TextField()

    def __str__(self) -> str:
        return f"{self.title} : {self.text}"


class Post(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    pub_date = models.DateTimeField('date pubilshed', auto_now_add=True)
    lastly_edited_date = models.DateTimeField(
        'date last edited', auto_now=True)
    article = models.OneToOneField(Article, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.article.__str__()
