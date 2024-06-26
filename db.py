# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AssignedProjects(models.Model):
    user = models.ForeignKey('Users', models.DO_NOTHING, primary_key=True)
    project = models.ForeignKey('Projects', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'assigned_projects'
        unique_together = (('user', 'project'),)


class Projects(models.Model):
    project_id = models.IntegerField(primary_key=True)
    project_title = models.CharField(max_length=500)
    availability = models.IntegerField()
    description = models.TextField(blank=True, null=True)  # This field type is a guess.
    sdg = models.TextField(blank=True, null=True)  # This field type is a guess.
    faculty_name = models.TextField()  # This field type is a guess.
    college_email = models.TextField(blank=True, null=True)  # This field type is a guess.
    mobile_number = models.TextField(blank=True, null=True)  # This field type is a guess.
    department = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'projects'


class Users(models.Model):
    user_id = models.IntegerField(primary_key=True)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'users'
