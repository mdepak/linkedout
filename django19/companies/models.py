from django.db import models


class Users(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    role = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Companies(models.Model):
    name = models.CharField(max_length=200)
    website = models.CharField(max_length=200)
    desc = models.TextField()

    def __str__(self):
        return self.name


class CompanyJobs(models.Model):
    company_id = models.ForeignKey('companies')
    title = models.CharField(max_length=200)
    role = models.CharField(max_length=200)
    desc = models.TextField()

    def __str__(self):
        return self.title


class JobsApplied(models.Model):
    user_id = models.ForeignKey('users')
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    company_id = models.ForeignKey('companies')
    company_name = models.CharField(max_length=200)
    job_id = models.ForeignKey('companyjobs')
    job_title = models.CharField(max_length=200)

    def __str__(self):
        return self.title