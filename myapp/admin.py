from django.contrib import admin
from .models import AdmissionUpload, AssignmentUpload, GalleryUpload, NoticeUpload
# Register your models here.
class AdmissionUploadAdmin(admin.ModelAdmin):
    list_display = ('id','name_of_student','date_of_registration','sr_no','class_admission','date_of_birth','religion','caste','nationality','gender','aadhar_number','student_aadhar_front','student_aadhar_back','father_name','father_qualification','father_occupation','father_mobile','father_address','father_aadhar_front','father_aadhar_back','mother_name','mother_qualification','mother_occupation','mother_mobile','mother_address','mother_aadhar_front','mother_aadhar_back','medical_issue','last_class','form_filled_by','student_photo','last_attended_school','session','email','birth_place','disability','category','father_photo','mother_photo','sealed_admission_doc','school_last_attended_with_result','subjects_studied','qualified_for_promotion','months_school_dues_paid','total_working_days','total_days_present','extra_curricular_activity','character_of_student','general_conduct','date_of_application_of_tc','reason_of_leaving','date_of_issuance_tc','tc_prepared_by')

class AssignmentUploadAdmin(admin.ModelAdmin):
    list_display = ('assignment_file','assignment_name','date_of_posting','assignment_class','assignment_subject','uploaded_by')
class GalleryUploadAdmin(admin.ModelAdmin):
    list_display = ('gallery_file','uploaded_by')
class NoticeUploadAdmin(admin.ModelAdmin):
    list_display = ('notice_desc','date_of_posting','uploaded_by')

admin.site.register(AdmissionUpload,AdmissionUploadAdmin)
admin.site.register(AssignmentUpload,AssignmentUploadAdmin)
admin.site.register(GalleryUpload,GalleryUploadAdmin)
admin.site.register(NoticeUpload,NoticeUploadAdmin)