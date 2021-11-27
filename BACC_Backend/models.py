import datetime

from django.db import models


TITLE_TH = (
        ('นาย', 'นาย'),
        ('นาง', 'นาง'),
        ('นางสาว', 'นางสาว'),
        ('ว่าที่ ร.ต.', 'ว่าที่ ร.ต.'),
        ('ร.ต.', 'ร.ต.'),
    )
TITLE_EN = (
        ('MR', 'MR'),
        ('MRS', 'MRS'),
        ('MISS', 'MISS'),
        ('Acting Sub.Lt. ', '่Acting Sub.Lt. '),
        ('Plt.Off.', 'Plt.Off.'),
        ('Sub.Lt.', 'Sub.Lt.')
    )

AREA = (
        ('North', 'North'),
        ('South', 'South'),
        ('Day-work', 'Day-work')
    )

RESPONSIBILITY = (
        ('FD', 'FD'),
        ('ICC', 'ICC'),
        ('CTRL1', 'CTRL1'),
        ('CTRL2', 'CTRL2'),
        ('DAY-WORK', 'DAY-WORK'),
        ('A/FIR', 'A/FIR')
    )

POSITION = (
        ('ผู้อำนวยการฝ่ายบริหารศูนย์ควบคุมจราจรทางอากาศเส้นทางบินกรุงเทพ',
         'ผู้อำนวยการฝ่ายบริหารศูนย์ควบคุมจราจรทางอากาศเส้นทางบินกรุงเทพ')
        ,
        ('ผู้อำนวยการศูนย์ควบคุมจราจรทางอากาศเส้นทางบินกรุงเทพ',
         'ผู้อำนวยการศูนย์ควบคุมจราจรทางอากาศเส้นทางบินกรุงเทพ')
        ,
        ('ผู้อำนวยการสนับสนุนศูนย์ควบคุมจราจรทางอากาศเส้นทางบินกรุงเทพ',
         'ผู้อำนวยการสนับสนุนศูนย์ควบคุมจราจรทางอากาศเส้นทางบินกรุงเทพ')
        ,
        ('ผู้จัดการงานควบคุมจราจรทางอากาศ (ศูนย์ควบคุมจราจรทางอากาศเส้นทางบินกรุงเทพ)',
         'ผู้จัดการงานควบคุมจราจรทางอากาศ (ศูนย์ควบคุมจราจรทางอากาศเส้นทางบินกรุงเทพ)')
        ,
        ('ผู้จัดการงานบริหารทั่วไป', 'ผู้จัดการงานบริหารทั่วไป')
        ,
        ('เจ้าหน้าที่ควบคุมจราจรทางอากาศ 2 (ศูนย์ควบคุมจราจรทางอากาศเส้นทางบินกรุงเทพ)',
         'เจ้าหน้าที่ควบคุมจราจรทางอากาศ 2 (ศูนย์ควบคุมจราจรทางอากาศเส้นทางบินกรุงเทพ)')
        ,
        ('ผู้ช่วยเจ้าหน้าที่ควบคุมจราจรทางอากาศ', 'ผู้ช่วยเจ้าหน้าที่ควบคุมจราจรทางอากาศ')
        ,
        ('เจ้าหน้าที่ควบคุมจราจรทางอากาศ 1 (ศูนย์ควบคุมจราจรทางอากาศเส้นทางบินกรุงเทพ)',
         'เจ้าหน้าที่ควบคุมจราจรทางอากาศ 1 (ศูนย์ควบคุมจราจรทางอากาศเส้นทางบินกรุงเทพ)')
        ,
        ('ผู้ช่วยเจ้าหน้าที่ควบคุมจราจรทางอากาศ', 'ผู้ช่วยเจ้าหน้าที่ควบคุมจราจรทางอากาศ')
        ,
        ('เจ้าหน้าที่บริหารงานทั่วไปอาวุโส', 'เจ้าหน้าที่บริหารงานทั่วไปอาวุโส')
        ,
        ('เจ้าหน้าที่ฝึกหัดควบคุมจราจรทางอากาศ (ศูนย์ควบคุมจราจรทางอากาศเส้นทางบินกรุงเทพ)',
         'เจ้าหน้าที่ฝึกหัดควบคุมจราจรทางอากาศ (ศูนย์ควบคุมจราจรทางอากาศเส้นทางบินกรุงเทพ)')
        ,
        ('เจ้าหน้าที่บริหารทั่วไป', 'เจ้าหน้าที่บริหารทั่วไป')
        ,
        ('นักเรียนฝึกหัดควบคุมจราจรทางอากาศ', 'นักเรียนฝึกหัดควบคุมจราจรทางอากาศ')
    )

DIVISION = (
        ('สจ.ศจ.', 'สจ.ศจ.'),
        ('คจ.ศจ.', 'ศจ.ศจ.')
    )


# Create your models here.
class Responsibility(models.Model):

    res_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)

    def __str_(self):
        return "Responsibility details of {}".format(self.name)


class Subject(models.Model):

    subject_id = models.AutoField(primary_key=True)
    code = models.CharField(max_length=255)
    name = models.IntegerField()
    startDate = models.DateField(default=datetime.date.today)
    endDate = models.DateField(default=datetime.date.today)
    responsibility = models.ManyToManyField(Responsibility)
    activeStatus = models.BooleanField(default=True)

    def __str_(self):
        return "Subject details of {}".format(self.name)


class EmployeeInitialCode(models.Model):

    emInit_id = models.AutoField(primary_key=True)
    initialCode = models.CharField(max_length=2)
    employee_id = models.IntegerField()
    activeStatus = models.BooleanField(default=False)
    isLock = models.BooleanField(default=False)

    def __str_(self):
        return "Initial Code number {}".format(self.initialCode)

# End One to One Relation table


# Many to Many of Employee and Subject to record employee score after they finish course (Pass / Fail)
class SubjectReport(models.Model):

    subReport_id = models.AutoField(primary_key=True)
    subject_id = models.IntegerField()
    employee_id = models.IntegerField()
    trainYear = models.IntegerField()
    score = models.IntegerField()
    score_pass = models.IntegerField()
    instructor = models.CharField(max_length=255)
    remark = models.TextField()

    def __str_(self):
        return "SubjectReport for employee id {}".format(self.employee_id)


# Many to Many of Employee and Subject to record Exam Score of them
class SubjectExam(models.Model):

    exam_id = models.AutoField(primary_key=True)
    subject_id = models.IntegerField()
    employee_id = models.IntegerField()
    year = models.IntegerField()
    date = models.DateField(default=datetime.date.today)
    investigator = models.CharField(max_length=255)
    score = models.IntegerField()
    remark = models.TextField()

    def __str_(self):
        return "Exam Score of employee id {}".format(self.employee_id)


class Employee(models.Model):

    employee_id = models.AutoField(primary_key=True)
    initialCode = models.CharField(max_length=2)
    title = models.CharField(choices=TITLE_TH, max_length=50)
    code = models.IntegerField()
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    title_eng = models.CharField(max_length=50)
    name_eng = models.CharField(max_length=255)
    surname_eng = models.CharField(max_length=255)
    position = models.CharField(choices=POSITION, max_length=255)
    division = models.CharField(choices=DIVISION, max_length=255)
    area = models.CharField(choices=AREA, max_length=50)
    responsibility = models.ManyToManyField(Responsibility)
    shift = models.CharField(max_length=10)
    activeStatus = models.BooleanField(default=True)

    def __str_(self):
        return "Employee details of {}".format(self.name)
