from django.db import models


class Users(models.Model):
    user_id = models.IntegerField(primary_key=True)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = "users"
        unique_together = (("user_id", "email"),)


class Projects(models.Model):
    project_id = models.IntegerField(primary_key=True)
    project_title = models.CharField(max_length=500)
    availability = models.IntegerField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    sdg = models.TextField(blank=True, null=True)
    faculty_name = models.TextField(blank=True, null=True)
    college_email = models.TextField(blank=True, null=True)
    mobile_number = models.TextField(blank=True, null=True)
    department = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "projects"
        unique_together = (("project_id", "project_title"),)


class AssignedProjects(models.Model):
    user = models.OneToOneField("Users", models.DO_NOTHING, primary_key=True)
    project = models.ForeignKey("Projects", models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = "assigned_projects"
        unique_together = (("user", "project"),)
