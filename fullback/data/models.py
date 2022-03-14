from django.db import models

# Create your models here.
#model for first graph on landing page
class Ipldata(models.Model):
    title = models.CharField(max_length = 50)
    year = models.IntegerField(unique=True)
    matches = models.IntegerField()

    def __str__(self):
        return self.title

#model for second graph on landing page
class Iplmatcheswondata(models.Model):
    title = models.CharField(max_length = 50)
    teamname = models.CharField(max_length = 40, unique = True)
    teamabbr = models.CharField(max_length = 5, unique = True)
    matcheswon = models.IntegerField()

    def __str__(self):
        return self.teamname

#model for match stats for each team i.e matches played vs matches won
class Iplmatchesplayedvswon(models.Model):
    title = models.CharField(max_length = 60)
    teamname = models.CharField(max_length = 40)
    teamabbr = models.CharField(max_length = 5)
    year = models.IntegerField()
    matchesplayed = models.IntegerField()
    matcheswon = models.IntegerField()

    def __str__(self):
        return self.teamname

#model for top economical bowlers for every season
class Ipltopeconomicalbowlers(models.Model):
    title = models.CharField(max_length = 60)
    year = models.IntegerField()
    topeconomybowler = models.CharField(max_length = 40)
    teamname = models.CharField(max_length = 4)
    matches = models.IntegerField()
    economy = models.FloatField()

    def __str__(self):
        return self.topeconomybowler

#model for extra runs conceded per season
class Iplextrarunsconcededperseason(models.Model):
    title = models.CharField(max_length = 60)
    year = models.IntegerField()
    extras = models.IntegerField()

    def __str__(self):
        return self.title