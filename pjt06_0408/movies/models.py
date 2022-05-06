from django.db import models

# Create your models here.

class Movie(models.Model):
    title=models.CharField(max_length=20)
    audience=models.IntegerField(null=True)
    release_date=models.DateField(null=True)
    genre=models.CharField(max_length=30,null=True)
    score=models.FloatField(null=True)
    poster_url=models.TextField(null=True)
    description=models.TextField(null=True)

    # class가 admin 페이지에서 어떻게 출력되는지 정의해주는 역할
    def __str__(self):
        return self.title