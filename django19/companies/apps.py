from django.apps import AppConfig


class Users(AppConfig):
    name = 'users'

class Companies(AppConfig):
    name = 'companies'

class CompanyJobsConfig(AppConfig):
    name = 'companyjobs'

class JobsApplied(AppConfig):
    name = 'jobsapplied'