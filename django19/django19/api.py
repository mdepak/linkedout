from companies.models import Companies
from companies.models import CompanyJobs
from companies.models import JobsApplied
from companies.models import Users
from tastypie.constants import ALL
from tastypie.resources import ModelResource


class UsersResource(ModelResource):
    class Meta:
        queryset = Users.objects.all()
        resource_name = 'users'
        filtering = {'name': ALL}

class CompanyResource(ModelResource):
    class Meta:
        queryset = Companies.objects.all()
        resource_name = 'companies'
        filtering = {'name': ALL}

class CompanyJobsResource(ModelResource):
    class Meta:
        queryset = CompanyJobs.objects.all()
        resource_name = 'companyjobs'
        filtering = {'role': ALL}

class JobsAppliedResource(ModelResource):
    class Meta:
        queryset = JobsApplied.objects.all()
        resource_name = 'jobsapplied'
        filtering = {'role': ALL}