from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=255)
    matches_won = models.PositiveIntegerField(default=0)
    matches_lost = models.PositiveIntegerField(default=0)

    @property
    def total_matches(self):
        return self.matches_won + self.matches_lost

    @property
    def win_percentage(self):
        if self.total_matches == 0:
            return 0
        return (self.matches_won / self.total_matches) * 100
