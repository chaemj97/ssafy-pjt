from django.contrib import admin

from movies.models import Actor, Movie, Review

# Register your models here.
class ActorAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name')

class MovieAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'release_date', 'poster_path')

class ReviewAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'content')

admin.site.register(Actor, ActorAdmin)
admin.site.register(Movie, MovieAdmin)
admin.site.register(Review, ReviewAdmin)