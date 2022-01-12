from django import forms
from django.contrib.auth.models import User
from .models import AdmissionUpload, AssignmentUpload
from bootstrap_datepicker_plus.widgets import DateTimePickerInput
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Row, Column
from django.contrib.auth.forms import UserCreationForm
class SignUpForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField(max_length=200)
    last_name = forms.CharField(max_length=200)
    class Meta:
        model = User
        fields = ('username','first_name','last_name','email','password1', 'password2')
        labels = {
            'username': 'Enter Username',
            'first_name': 'Enter First Name',
            'last_name': 'Enter Last Name',
            'email': 'Enter Email',
            'password1': 'Enter Password',
            'password2': 'Enter Password Again'
        }
class DateInput(forms.DateInput):
    input_type = 'date'
class AssignmentUploadForm(forms.ModelForm):
    class Meta:
        model = AssignmentUpload
        fields = '__all__'
        labels = {
            'assignment_file': 'Choose Assignment File',
            'assignment_name': 'Assignment Name',
            'date_of_posting': 'Date',
            'assignment_subject': 'Subject',
            'assignment_class': 'Assignment related to which class'
        }
        widgets = {
            'uploaded_by': forms.HiddenInput(),
            'date_of_posting': DateInput(), 
        }
class AdmissionUploadForm(forms.ModelForm):
    class Meta:
        model = AdmissionUpload
        fields = '__all__'
        labels = {
            'student_photo': 'Choose Student Picture',
            'name_of_student': 'Name of student',
            'date_of_registration':'Registration Date',
            'sr_no': 'SR No',
            'class_admission': 'Class for Admission',
            'date_of_birth': 'Date of Birth',
            'religion': 'Religion',
            'caste': 'Caste',
            'nationality': 'Nationality',
            'gender': 'Gender',
            'aadhar_number': 'Student Aadhar Number',
            'student_aadhar_front': 'Upload Student\'s Aadhar Card Front',
            'student_aadhar_back': 'Upload Student\'s Aadhar Card Back',
            'father_name': 'Father\'s name',
            'father_qualification': 'Father\'s Qualification',
            'father_occupation': 'Father\'s Occupation',
            'father_mobile': 'Father\'s Mobile Number',
            'father_address': 'Father\'s Address',
            'father_aadhar_front': 'Upload Father\'s Aadhar Card Front',
            'father_aadhar_back': 'Upload Father\'s Aadhar Card Front',
            'mother_name': 'Mother\'s Name',
            'mother_qualification': 'Mother\'s Qualification',
            'mother_occupation': 'Mother\'s Occupation',
            'mother_mobile': 'Mother\'s Mobile Number',
            'mother_address': 'Mother\'s Address',
            'mother_aadhar_front': 'Upload Mother\'s Aadhar Card Front',
            'mother_aadhar_back': 'Upload Mother\'s Aadhar Card Front',
            'medical_issue': 'Any medical /social/ psychological constraints for the child (please furnish relevant information separately if required) this information will exclusively be used for proper case study and parental care of the child in the school.',
            'last_class': 'Last Attended Class',
            'last_attended_school': 'Last Attended School',
            'session': 'Current Session',
            'email': 'Email ID',
            'birth_place': 'Place of Birth',
            'disability': 'Any disability',
            'category': 'Category',
            'father_photo': 'Father\'s Photo',
            'mother_photo': 'Mother\'s Photo',
        }
        widgets = {
            'date_of_birth': DateInput(), 
            'date_of_registration': DateInput(),
            'form_filled_by': forms.HiddenInput(),
        }
    
