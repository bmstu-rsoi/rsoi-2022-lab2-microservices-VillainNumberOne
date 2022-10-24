from django.db import models

class Person(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=100)
    stars = models.IntegerField(null=True)

    class Meta:
        constraints = [
            models.CheckConstraint(
                name="%(app_label)s_%(class)s_stars_range",
                check=models.Q(stars__range=(1, 100)),
            ),
        ]
