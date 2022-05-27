from django.db import models
from django.conf import settings

from django.core.exceptions import ValidationError

# Create your models here.
class Genre(models.Model):
    name = models.CharField(max_length=50)

class Movie(models.Model):
    title = models.CharField(max_length=100)
    overview = models.TextField()
    release_date = models.DateField()
    poster_path = models.TextField()
    genres = models.ManyToManyField(Genre, related_name="genres")
    vote_count = models.IntegerField()
    vote_average = models.FloatField()
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL,related_name='like_movies',blank=True)

    def __str__(self):
        return self.title

# 점수 제한 0~10
def validate_score(value):
    if (value < 0 ) | (value > 10):
        msg = "평점은 0이상 10이하로 매겨주세요"
        raise ValidationError(msg)
 
class Review(models.Model):
  user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
  movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
  score = models.FloatField(default=0, validators=[validate_score])
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)