from django.db import models

class Champion(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.TextField(null=False, unique=True)
    age = models.IntegerField(null=True)
    phrase = models.TextField(null=True)
    def __str__(self):
        return self.name

class InfoAll(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE, null=False)
    statistics = models.ForeignKey('Statistics', on_delete=models.CASCADE)
    champion = models.ForeignKey('Champion', on_delete=models.CASCADE)
    season = models.IntegerField()
    class Meta:
        unique_together = ('user', 'champion', 'season')
    def __str__(self):
        return "Statistics: " + self.user.name + " | "+ self.champion.name

class Items(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.TextField(unique=True)
    desc = models.TextField()
    winrate = models.IntegerField()
    def __str__(self):
        return self.name

class ItemsChampions(models.Model):
    champion = models.ForeignKey('Champion', on_delete=models.CASCADE)
    item = models.ForeignKey('Items', on_delete=models.CASCADE)
    class Meta:
        unique_together = ('champion', 'item')

    def __str__(self):
        return self.champion.name + " | " +self.item.name

class Rating(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE, unique=True)
    rating = models.IntegerField()
    def __str__(self):
        return self.user.login

class Statistics(models.Model):
    id = models.AutoField(primary_key=True)
    avg_kills = models.IntegerField()
    winrate = models.IntegerField()
    rating = models.IntegerField()
    champions = models.ManyToManyField('Champion', through='InfoAll')

class User(models.Model):
    id = models.AutoField(primary_key=True)
    login = models.TextField(unique=True)
    email = models.EmailField()
    name = models.TextField()
    def __str__(self):
        return self.login

class Video(models.Model):
    id = models.AutoField(primary_key=True)
    champion = models.ForeignKey('Champion', on_delete=models.CASCADE)
    author = models.TextField(unique=False)
    name = models.TextField(unique=True)
    def __str__(self):
        return self.name

