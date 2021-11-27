from django.shortcuts import render
from rest_framework import viewsets
from .serializers import EmployeeSerializer, EmployeeInitialCodeSerializer
from .serializers import SubjectSerializer, SubjectExamSerializer, SubjectReportSerializer
from .serializers import ResponsibilitySerializer
from .models import Employee, EmployeeInitialCode
from .models import Subject, SubjectExam, SubjectReport
from .models import Responsibility

import os
from django.conf import settings
import pandas as pd
from django.core.files.storage import FileSystemStorage


# Create your views here.
class EmployeeViewSet(viewsets.ModelViewSet):
    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()


class EmployeeInitialCodeViewSet(viewsets.ModelViewSet):
    serializer_class = EmployeeInitialCodeSerializer
    queryset = EmployeeInitialCode.objects.all()


class SubjectViewSet(viewsets.ModelViewSet):
    serializer_class = SubjectSerializer
    queryset = Subject.objects.all()


class SubjectExamViewSet(viewsets.ModelViewSet):
    serializer_class = SubjectExamSerializer
    queryset = SubjectExam.objects.all()


class SubjectReportViewSet(viewsets.ModelViewSet):
    serializer_class = SubjectReportSerializer
    queryset = SubjectReport.objects.all()


class ResponsibilityViewSet(viewsets.ModelViewSet):
    serializer_class = ResponsibilitySerializer
    queryset = Responsibility.objects.all()


# Import data from excel
def import_csv(request):
    print('s')
    try:
        if request.method == 'POST' and request.FILES['myfile']:

            myfile = request.FILES['myfile']
            fs = FileSystemStorage()
            filename = fs.save(myfile.name, myfile)
            uploaded_file_url = fs.url(filename)
            excel_file = uploaded_file_url
            print(excel_file)
            empexceldata = pd.read_csv("." + excel_file, encoding='utf-8')
            print(type(empexceldata))
            dbframe = empexceldata
            for dbframe in dbframe.itertuples():
                print(dbframe)

            return render(request, 'importexcel.html', {
                'uploaded_file_url': uploaded_file_url
            })
    except Exception as identifier:
        print(identifier)

    return render(request, 'importexcel.html', {})
