from django.shortcuts import render,redirect
import requests,random
from django.http import HttpResponse
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.views.generic import View
from django.core.files.storage import FileSystemStorage
from django.utils.decorators import method_decorator
from django.contrib.auth.forms import UserCreationForm
from .models import AdmissionUpload, AssignmentUpload, GalleryUpload, NoticeUpload
from .forms import AdmissionUploadForm, SignUpForm, AssignmentUploadForm, GalleryUploadForm, NoticeUploadForm
from io import BytesIO
from django.http import HttpResponse
from xhtml2pdf import pisa
from django.template.loader import get_template
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import user_passes_test
from django.contrib import messages
from io import StringIO
from io import BytesIO
from num2words import num2words

# ssl start
import ssl 

try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context
# ssl end

@login_required(login_url='handleLogin')
def CharacterCertificate_PDF(request, id) :
    CharacterCertificate = get_object_or_404(AdmissionUpload, pk=id)
    data = {'CharacterCertificate': CharacterCertificate}
    template = get_template('character.html')
    html  = template.render(data)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("UTF-8")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return HttpResponse('We had some errors<pre>%s</pre>' % escape(html))

@login_required(login_url='handleLogin')
def DOBCertificate_PDF(request, id) :
    DOBCertificate = get_object_or_404(AdmissionUpload, pk=id)
    data = {'DOBCertificate': DOBCertificate}
    template = get_template('dob_certificate.html')
    html  = template.render(data)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("UTF-8")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return HttpResponse('We had some errors<pre>%s</pre>' % escape(html))
@login_required(login_url='handleLogin')
def IDCard_PDF(request, id) :
    IDCard = get_object_or_404(AdmissionUpload, pk=id)
    data = {'IDCard': IDCard}
    template = get_template('id-card.html')
    html  = template.render(data)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("UTF-8")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return HttpResponse('We had some errors<pre>%s</pre>' % escape(html))
@login_required(login_url='handleLogin')
def TransferCertificate_PDF(request, id) :
    TransferCertificate = get_object_or_404(AdmissionUpload, pk=id)
    year_dob = num2words(TransferCertificate.date_of_birth.strftime('%Y'))
    month_dob = TransferCertificate.date_of_birth.strftime('%m')
    date_dob = num2words(TransferCertificate.date_of_birth.strftime('%d'))
    data = {'TransferCertificate': TransferCertificate,'year_dob':year_dob,'date_dob':date_dob,'month_dob':month_dob}
    template = get_template('transfer_certificate.html')
    html  = template.render(data)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("UTF-8")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return HttpResponse('We had some errors<pre>%s</pre>' % escape(html))
@login_required(login_url='handleLogin')
def Download_Admission_Form_PDF(request, id) :
    DownloadAdmissionForm = get_object_or_404(AdmissionUpload, pk=id)
    data = {'DownloadAdmissionForm': DownloadAdmissionForm}
    template = get_template('admission_form_pdf.html')
    html  = template.render(data)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("UTF-8")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return HttpResponse('We had some errors<pre>%s</pre>' % escape(html))
def main(request):
    notice = NoticeUpload.objects.all()
    return render(request, 'main.html',{'notice':notice})
@login_required(login_url='handleLogin')
def allassignments(request):
    assignment = AssignmentUpload.objects.all()
    return render(request, 'allassignments.html',{'assignment': assignment})
@login_required(login_url='handleLogin')
def updategallery(request):
    gallery = GalleryUpload.objects.all()
    return render(request, 'updategallery.html',{'gallery': gallery})

def gallery(request):
    gallery = GalleryUpload.objects.all()
    return render(request, 'gallery.html',{'gallery': gallery})
@login_required(login_url='handleLogin')
def uploadassignment(request):
    assignment = AssignmentUpload.objects.all()
    if request.method == 'POST':
        form = AssignmentUploadForm(request.POST,request.FILES)
        if form.is_valid():
            new_record = form.save(commit=False)
            new_record.uploaded_by = request.user.username
            new_record.save()
            messages.success(request, "Assignment Uploaded Successfully")
            return redirect('/assignments')
    form = AssignmentUploadForm()
    return render(request, 'uploadassignment.html',{'form': form,'assignment': assignment})
@login_required(login_url='handleLogin')
def uploadgallery(request):
    gallery = GalleryUpload.objects.all()
    if request.method == 'POST':
        form = GalleryUploadForm(request.POST,request.FILES)
        if form.is_valid():
            new_record = form.save(commit=False)
            new_record.uploaded_by = request.user.username
            new_record.save()
            messages.success(request, "Image Uploaded Successfully")
            return redirect('/gallery')
    form = GalleryUploadForm()
    return render(request, 'upload_gallery.html',{'form': form})
@login_required(login_url='handleLogin')
def uploadnotice(request):
    if request.method == 'POST':
        form = NoticeUploadForm(request.POST,request.FILES)
        if form.is_valid():
            new_record = form.save(commit=False)
            new_record.uploaded_by = request.user.username
            new_record.save()
            return redirect('/')
    form = NoticeUploadForm()
    return render(request, 'upload_notice.html',{'form': form})
def index(request):
    pi = AdmissionUpload.objects.count()
    ass = AssignmentUpload.objects.count()
    us = User.objects.count()
    users = User.objects.all()
    
    return render(request, 'index.html',{'pi':pi,'us':us,'users':users,'ass':ass})
def feesportal(request):
    return render(request, 'feesportal.html')
    
@login_required(login_url='handleLogin')
def character(request,id):
    pi = AdmissionUpload.objects.get(pk=id)
    return render(request, 'character.html',{'pi':pi})
def user_is_not_logged_in(user):
    return not user.is_authenticated
@user_passes_test(user_is_not_logged_in)
def handleLogin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user= authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            # messages.success(request, "Logged in successfully")
            return redirect('main')
        else:
            messages.error(request, "Invalid credentials")
            return redirect('handleLogin')

    return render(request, 'login.html')
def handleLogout(request):
    logout(request)
    messages.info(request, "Logged out successfully")
    return redirect('handleLogin')

def signUp(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('main')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})
@login_required(login_url='handleLogin')
def admission(request):
    if request.method == 'POST':
        form = AdmissionUploadForm(request.POST,request.FILES)
        if form.is_valid():
            new_record = form.save(commit=False)
            new_record.form_filled_by = request.user.username
            new_record.save()
            messages.info(request, "Data Inserted successfully")
            return redirect('/all-admissions')
    form = AdmissionUploadForm()
    return render(request,'admission.html',{'form':form})
@login_required(login_url='handleLogin')
def alladmission(request):
    stud =  AdmissionUpload.objects.all()
    return render(request,'alladmissions.html',{'stud':stud})


@login_required(login_url='handleLogin')
def classwise(request):
    studone =  AdmissionUpload.objects.filter(class_admission='first')
    studtwo =  AdmissionUpload.objects.filter(class_admission='second')
    studthree =  AdmissionUpload.objects.filter(class_admission='third')
    studfour =  AdmissionUpload.objects.filter(class_admission='fourth')
    studfive =  AdmissionUpload.objects.filter(class_admission='fifth')
    studsix =  AdmissionUpload.objects.filter(class_admission='sixth')
    studseven =  AdmissionUpload.objects.filter(class_admission='seventh')
    studeight =  AdmissionUpload.objects.filter(class_admission='eighth')
    studnur =  AdmissionUpload.objects.filter(class_admission='nursery')
    studlkg =  AdmissionUpload.objects.filter(class_admission='lkg')
    studukg =  AdmissionUpload.objects.filter(class_admission='ukg')
    return render(request,'classfilter.html',{'studone':studone,'studtwo':studtwo,'studthree':studthree,'studfour':studfour,'studfive':studfive,'studsix':studsix,'studseven':studseven,'studeight':studeight,'studnur':studnur,'studlkg':studlkg,'studukg':studukg})



@login_required(login_url='handleLogin')
def update_data(request,id):
    stud = AdmissionUpload.objects.get(pk=id)
    if request.method=="POST":
        pi = AdmissionUpload.objects.get(pk=id)
        fm=AdmissionUploadForm(request.POST,request.FILES, instance=pi)
        if fm.is_valid():
            fm.save()
            messages.success(request, "Data Updated successfully")
            return redirect('/all-admissions')
    else:
        pi = AdmissionUpload.objects.get(pk=id)
        fm = AdmissionUploadForm(instance=pi)
    return render(request,'updatestudent.html',{'form':fm,'stud':stud})
@login_required(login_url='handleLogin')
def delete_data(request,id):
    if request.method == 'POST':
        pi = AdmissionUpload.objects.get(pk=id)
        pi.delete()
        messages.error(request, "Data Deleted successfully")
        return redirect('/all-admissions')
@login_required(login_url='handleLogin')
def delete_gallery(request,id):
    if request.method == 'POST':
        pi = GalleryUpload.objects.get(pk=id)
        pi.delete()
        messages.error(request, "Photo Deleted successfully")
        return redirect('/updategallery')

