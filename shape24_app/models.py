from django.db import models

class Users(models.Model):
    user_id = models.IntegerField(primary_key=True)  # The composite primary key (user_id, email) found, that is not supported. The first column is selected.
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users'
        unique_together = (('user_id', 'email'),)
