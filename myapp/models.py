import uuid
from django.db import models
from django.contrib.auth.models import User
import datetime
from django.utils.translation import gettext as _

CLASS_CHOICES = (
    ('---','---'),
    ('nursery', 'NURSERY'),
    ('lkg','LKG'),
    ('ukg','UKG'),
    ('first','FIRST'),
    ('second','SECOND'),
    ('third','THIRD'),
    ('fourth','FOURTH'),
    ('fifth','FIFTH'),
    ('sixth','SIXTH'),
    ('seventh','SEVENTH'),
    ('eighth','EIGHTH'),
)
GENDER_CHOICES = (
    ('---','---'),
    ('male', 'MALE'),
    ('female','FEMALE'),
    ('others', 'OTHERS'),
)
SUBJECT_CHOICES = (
    ('---','---'),
    ('english', 'ENGLISH'),
    ('hindi','HINDI'),
    ('maths', 'MATHS'),
    ('social science', 'SOCIAL SCIENCE'),
    ('science', 'SCIENCE'),
    ('general knowledge', 'GENERAL KNOWLEDGE'),
    ('hindi grammar', 'HINDI GRAMMAR'),
    ('english grammar', 'ENGLISH GRAMMAR'),
    ('drawing', 'DRAWING'),
)
DISABILITY_CHOICES = (
    ('---','---'),
    ('yes', 'YES'),
    ('no','NO'),
)
CATEGORY_CHOICES = (
    ('---','---'),
    ('general', 'GENERAL'),
    ('obc','OBC'),
    ('sc','SC'),
)
RELIGION_CHOICES = (
    ('---','---'),
    ('hinduism', 'HINDUISM'),
    ('islam','ISLAM'),
    ('budhism','BUDHISM'),
    ('sikhism','SIKHISM'),
    ('jainism','JAINISM'),
)
year_dropdown = []
for y in range(2008, (datetime.datetime.now().year+1)):
    year_dropdown.append((y, y))
# Create your models here.
class AdmissionUpload(models.Model):
    student_photo = models.FileField(upload_to='images/')
    name_of_student = models.CharField(max_length=50, blank=True, null=True)
    date_of_registration = models.DateTimeField()
    sr_no = models.CharField(max_length=50, blank=True, null=True)
    class_admission = models.CharField(max_length=20, choices=CLASS_CHOICES, default='---')
    date_of_birth = models.DateTimeField()
    religion = models.CharField(max_length=20, choices=RELIGION_CHOICES, default='---')
    caste = models.CharField(max_length=50, blank=True, null=True)
    nationality = models.CharField(max_length=50, blank=True, null=True)
    gender = models.CharField(max_length=20, choices=GENDER_CHOICES, default='---')
    aadhar_number = models.CharField(max_length=12, blank=True, null=True)
    student_aadhar_front = models.FileField(upload_to='images/')
    student_aadhar_back = models.FileField(upload_to='images/')
    father_name = models.CharField(max_length=50, blank=True, null=True)
    father_qualification = models.CharField(max_length=50, blank=True, null=True)
    father_occupation = models.CharField(max_length=50, blank=True, null=True)
    father_mobile = models.CharField(max_length=50, blank=True, null=True)
    father_address = models.CharField(max_length=50, blank=True, null=True)
    father_aadhar_front = models.FileField(upload_to='images/')
    father_aadhar_back = models.FileField(upload_to='images/')
    mother_name = models.CharField(max_length=50, blank=True, null=True)
    mother_qualification = models.CharField(max_length=50, blank=True, null=True)
    mother_occupation = models.CharField(max_length=50, blank=True, null=True)
    mother_mobile = models.CharField(max_length=50, blank=True, null=True)
    mother_address = models.CharField(max_length=50, blank=True, null=True)
    mother_aadhar_front = models.FileField(upload_to='images/')
    mother_aadhar_back = models.FileField(upload_to='images/')
    medical_issue = models.CharField(max_length=100, blank=True, null=True)
    last_class = models.CharField(max_length=20, choices=CLASS_CHOICES, default='---')
    form_filled_by = models.CharField(max_length=100, blank=True, null=True)
    last_attended_school = models.CharField(max_length=100, blank=True, null=True)
    session = models.IntegerField(_('year'), max_length=4, choices=year_dropdown, default=datetime.datetime.now().year)
    email = models.CharField(max_length=100, blank=True, null=True)
    birth_place = models.CharField(max_length=100, blank=True, null=True)
    disability = models.CharField(max_length=20, choices=DISABILITY_CHOICES, default='---')
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='---')
    father_photo = models.FileField(upload_to='images/')
    mother_photo = models.FileField(upload_to='images/')
    # to be filled by uploading pdf
    sealed_admission_doc = models.FileField(upload_to='admissionforms/', blank=True, null=True)
    # TC details
    school_last_attended_with_result = models.CharField(max_length=100, blank=True, null=True)
    subjects_studied = models.CharField(max_length=100, blank=True, null=True)
    qualified_for_promotion = models.CharField(max_length=100, blank=True, null=True)
    months_school_dues_paid = models.CharField(max_length=100, blank=True, null=True)
    total_working_days = models.CharField(max_length=100, blank=True, null=True)
    total_days_present = models.CharField(max_length=100, blank=True, null=True)
    extra_curricular_activity = models.CharField(max_length=100, blank=True, null=True)
    character_of_student = models.CharField(max_length=100, blank=True, null=True)
    general_conduct = models.CharField(max_length=100, blank=True, null=True)
    date_of_application_of_tc = models.CharField(max_length=100, blank=True, null=True)
    reason_of_leaving = models.CharField(max_length=100, blank=True, null=True)
    date_of_issuance_tc = models.CharField(max_length=100, blank=True, null=True)
    tc_prepared_by = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name_of_student
class AssignmentUpload(models.Model):
    assignment_file = models.FileField(upload_to='assignment/')
    assignment_name = models.CharField(max_length=50, blank=True, null=True)
    date_of_posting = models.DateTimeField()
    assignment_class = models.CharField(max_length=20, choices=CLASS_CHOICES, default='---')
    assignment_subject = models.CharField(max_length=40, choices=SUBJECT_CHOICES, default='---')
    uploaded_by = models.CharField(max_length=100, blank=True, null=True)
    def __str__(self):
        return self.assignment_name
class GalleryUpload(models.Model):
    gallery_file = models.FileField(upload_to='gallery/')
    uploaded_by = models.CharField(max_length=100, blank=True, null=True)
    def __str__(self):
        return self.uploaded_by
class NoticeUpload(models.Model):
    notice_desc = models.CharField(max_length=500, blank=True, null=True)
    notice_file = models.FileField(upload_to='notices/')
    date_of_posting = models.DateTimeField()
    uploaded_by = models.CharField(max_length=100, blank=True, null=True)
    def __str__(self):
        return self.notice_desc
        