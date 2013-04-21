from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User

class Notecard(models.Model):
    owner = models.ForeignKey(User)
    deck = models.ManyToManyField("Deck")
    front = models.TextField()
    back = models.TextField()
    name = models.CharField(max_length=100)
    learned = models.BooleanField(default=False)
    times_reviewed = models.IntegerField(default=0)
    times_right = models.IntegerField(default=0)

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('card_details',
                       args=[self.id, ]
                       )


class Deck(models.Model):
    owner = models.ForeignKey(User)
    name = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('deck_details',
                       args=[self.id, ]
                       )
