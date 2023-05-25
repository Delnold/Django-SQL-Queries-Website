from django.contrib import admin
from .models import Champion, InfoAll, Items, ItemsChampions, Rating, Statistics, User, Video

@admin.register(Champion)
class ChampionAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'phrase')

@admin.register(InfoAll)
class InfoAllAdmin(admin.ModelAdmin):
    list_display = ('user', 'statistics', 'champion', 'season')

@admin.register(Items)
class ItemsAdmin(admin.ModelAdmin):
    list_display = ('name', 'desc', 'winrate')

@admin.register(ItemsChampions)
class ItemsChampionsAdmin(admin.ModelAdmin):
    list_display = ('champion', 'item')

@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = ('user', 'rating')

@admin.register(Statistics)
class StatisticsAdmin(admin.ModelAdmin):
    list_display = ('avg_kills', 'winrate', 'rating')

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('login', 'email', 'name')

@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ('champion', 'author', 'name')
