from django.db import models

class Notecard(models.Model):
    front = models.TextField()
    back = models.TextField()
    name = models.CharField(max_length=100)
    learned = models.BooleanField(default=False)
    times_reviewed = models.IntegerField(default=0)
    times_right = models.IntegerField(default=0)

    # def Review(self):
    #   self.times_reviewed += 1
    #   self.save()

    # def mark_right(self):
    #   self.times_right += 1
    #   self.save()

    #def get_absolute_url(self):

    def __unicode__(self):
        return self.name 


