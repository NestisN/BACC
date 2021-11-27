from django.contrib import admin
from import_export import resources, fields
from .models import Employee, EmployeeInitialCode  # add this
from .models import Subject, SubjectExam, SubjectReport
from .models import Responsibility
from import_export.admin import ImportExportModelAdmin
# Register your models here.


class EmployeeResource(resources.ModelResource):
    class Meta:
        model = Employee
        import_id_fields = ('employee_id',)
        fields = ("employee_id", "initialCode", "title", "name", "surname", "title_eng", "name_eng", "surname_eng",
                  "position", "division", "area", "responsibility",  "shift", "activeStatus")


class EmployeeAdmin(ImportExportModelAdmin):
    resource_class = EmployeeResource


class ResponsibilityResource(resources.ModelResource):

    class Meta:
        model = Responsibility
        import_id_fields = ('res_id',)
        fields = ("res_id", "name")


class ResponsibilityAdmin(ImportExportModelAdmin):
    resource_class = ResponsibilityResource


admin.site.register(Employee, EmployeeAdmin)  # add this
admin.site.register(EmployeeInitialCode)
admin.site.register(Subject)
admin.site.register(SubjectExam)
admin.site.register(SubjectReport)
admin.site.register(Responsibility, ResponsibilityAdmin)
# Register your models here.
