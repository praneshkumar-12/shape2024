from django.db import models


class Users(models.Model):
    user_id = models.IntegerField(primary_key=True)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'users'


class Projects(models.Model):
    project_id = models.IntegerField(primary_key=True)
    project_title = models.CharField(max_length=500)
    availability = models.IntegerField()
    description = models.TextField(blank=True, null=True)
    sdg = models.TextField(blank=True, null=True)
    faculty_name = models.TextField()
    college_email = models.TextField(blank=True, null=True)
    mobile_number = models.TextField(blank=True, null=True)
    department = models.TextField()

    class Meta:
        managed = False
        db_table = 'projects'


class AssignedProjects(models.Model):
    user = models.ForeignKey('Users', models.DO_NOTHING, primary_key=True)
    project = models.ForeignKey('Projects', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'assigned_projects'
        unique_together = (('shape24.dbo.user', 'shape24.dbo.project'),)
