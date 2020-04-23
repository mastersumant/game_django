

from django.db import models
from django.db.models import Q
from django.contrib.auth.models import User
GAME_STATUS_CHOICES=(
    ('F','first player to move'),
    ('S','second player to move'),
    ('W','first player to win'),
    ('L','second player to win'),
    ('D','draw'),
)
class GamesQuerySet(models.QuerySet):
    def game_for_user(self,user):
        return self.filter(
            Q(first_player=user) | Q(Second_player=user)
        )
    def active(self):
        return self.filter(
            Q(status='F') | Q(status='S')
        ) 

class Game (models.Model):
    first_player=models.ForeignKey(User,related_name="games_first_player",on_delete=models.CASCADE)
    Second_player=models.ForeignKey(User,related_name="games_second_player",on_delete=models.CASCADE)

    start_time=models.DateTimeField(auto_now_add=True)
    last_active=models.DateTimeField(auto_now_add=True)
    status=models.CharField(max_length=1,default='F',choices=GAME_STATUS_CHOICES)
    objects=GamesQuerySet.as_manager()

def __str__(self):
    return "{0} vs {1}".format(self.first_player,self.Second_player)

class Move(models.Model):
    x=models.IntegerField()
    y=models.IntegerField()
    comments=models.CharField(max_length=300,blank=True)
    by_first_player=models.BooleanField()
    game=models.ForeignKey(Game,on_delete=models.CASCADE)
