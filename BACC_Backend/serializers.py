from rest_framework import serializers
from .models import Employee, EmployeeInitialCode
from .models import Subject, SubjectReport, SubjectExam
from .models import Responsibility


class ResponsibilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Responsibility
        fields = ("res_id", "name")


class EmployeeInitialCodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeInitialCode
        fields = ("emInit_id", "initialCode", "employee_id", "activeStatus", "isLock")


class SubjectSerializer(serializers.ModelSerializer):
    responsibility = ResponsibilitySerializer(many=True)

    class Meta:
        model = Subject
        fields = ("subject_id", "code", "name", "startDate", "endDate", "responsibility", "activeStatus")


class SubjectReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubjectReport
        fields = ("subReport_id", "subject_id", "employee_id", "trainYear", "score", "score_pass", "instructor",
                  "remark")


class SubjectExamSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubjectExam
        fields = ("exam_id", "subject_id", "employee_id", "year", "date", "investigator", "score", "remark")


class EmployeeSerializer(serializers.ModelSerializer):
    responsibility = ResponsibilitySerializer(many=True)

    class Meta:
        model = Employee
        fields = ("employee_id", "initialCode", "title", "name", "name_eng", "surname", "surname_eng",
                  "position", "division", "area", "responsibility",  "shift", "activeStatus")

