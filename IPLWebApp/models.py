from django.db import models

# Create your models here.

class addTeam(models.Model):
    TeamImage = models.ImageField(upload_to='static/image')
    Team_name = models.CharField(max_length=20)
    HeadLine = models.CharField(max_length=20)

    def __str__(self):
        return self.Team_name


class addNewPlayers(models.Model):
    player_name = models.CharField(max_length=20)
    role = models.CharField(max_length=20)
    price = models.CharField(max_length=20)
    status = models.CharField(max_length=20)
    team = models.CharField(max_length=20)

    def __str__(self):
        return self.player_name




class Banglore(models.Model):
    player_name = models.CharField(max_length=20)
    role = models.CharField(max_length=20)
    price = models.CharField(max_length=20)
    status = models.CharField(max_length=20)
    team = models.CharField(max_length=20)

    def __str__(self):
        return self.player_name


class chennai(models.Model):
    player_name = models.CharField(max_length=20)
    role = models.CharField(max_length=20)
    price = models.CharField(max_length=20)
    status = models.CharField(max_length=20)
    team = models.CharField(max_length=20)

    def __str__(self):
        return self.player_name


class mumbai(models.Model):
    player_name = models.CharField(max_length=20)
    role = models.CharField(max_length=20)
    price = models.CharField(max_length=20)
    status = models.CharField(max_length=20)
    team = models.CharField(max_length=20)

    def __str__(self):
        return self.player_name


class delhi(models.Model):
    player_name = models.CharField(max_length=20)
    role = models.CharField(max_length=20)
    price = models.CharField(max_length=20)
    status = models.CharField(max_length=20)
    team = models.CharField(max_length=20)

    def __str__(self):
        return self.player_name


class kolkata(models.Model):
    player_name = models.CharField(max_length=20)
    role = models.CharField(max_length=20)
    price = models.CharField(max_length=20)
    status = models.CharField(max_length=20)
    team = models.CharField(max_length=20)

    def __str__(self):
        return self.player_name


class punjab(models.Model):
    player_name = models.CharField(max_length=20)
    role = models.CharField(max_length=20)
    price = models.CharField(max_length=20)
    status = models.CharField(max_length=20)
    team = models.CharField(max_length=20)

    def __str__(self):
        return self.player_name


class rajasthan(models.Model):
    player_name = models.CharField(max_length=20)
    role = models.CharField(max_length=20)
    price = models.CharField(max_length=20)
    status = models.CharField(max_length=20)
    team = models.CharField(max_length=20)

    def __str__(self):
        return self.player_name


class hyderabad(models.Model):
    player_name = models.CharField(max_length=20)
    role = models.CharField(max_length=20)
    price = models.CharField(max_length=20)
    status = models.CharField(max_length=20)
    team = models.CharField(max_length=20)

    def __str__(self):
        return self.player_name


class TeamSearch(models.Model):
    team = models.CharField(max_length=20)
    players= models.CharField(max_length=20)

    def __str__(self):
        return self.players



