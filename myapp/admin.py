from django.contrib import admin
from .models import AdmissionUpload, AssignmentUpload
# Register your models here.
class AdmissionUploadAdmin(admin.ModelAdmin):
    list_display = ('id','name_of_student','date_of_registration','sr_no','class_admission','date_of_birth','religion','caste','nationality','gender','aadhar_number','student_aadhar_front','student_aadhar_back','father_name','father_qualification','father_occupation','father_mobile','father_address','father_aadhar_front','father_aadhar_back','mother_name','mother_qualification','mother_occupation','mother_mobile','mother_address','mother_aadhar_front','mother_aadhar_back','medical_issue','last_class','form_filled_by','student_photo','last_attended_school','session','email','birth_place','disability','category','father_photo','mother_photo')

class AssignmentUploadAdmin(admin.ModelAdmin):
    list_display = ('assignment_file','assignment_name','date_of_posting','assignment_class','assignment_subject','uploaded_by')

admin.site.register(AdmissionUpload,AdmissionUploadAdmin)
admin.site.register(AssignmentUpload,AssignmentUploadAdmin)