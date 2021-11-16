from django.db import models
from django.db.models.fields import DateField

class Actor(models.Model):
  id=models.AutoField(primary_key=True)
  first_name=models.CharField(max_length=45)
  last_name=models.CharField(max_length=45)
  date_of_birth=models.DateTimeField(max_length=100)

  class Meta:
    db_table="actors"

  def __str__(self):

    return self.last_name+self.first_name

class Movie(models.Model):
  id=models.AutoField(primary_key=True)
  title=models.CharField(max_length=45)
  release_date=models.DateTimeField()
  running_time=models.IntegerField(default=0)
  movieactor=models.ManyToManyField(Actor,through='Actor_Movie',through_fields=("movie","actor")),

  class Meta:
    db_table="movies"

  def __str__(self):

    return self.title

class Actor_Movie:
  id=models.AutoField(primary_key=True)
  actor=models.ForeignKey("Actor", on_delete=models.CASCADE,db_constraint="actor")
  movie=models.ForeignKey("Movie",on_delete=models.CASCADE,db_constraint="movie")

  class Meta:
    db_table="actors_movies"
# Create your models here.
