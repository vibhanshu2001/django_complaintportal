from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('portal/',views.index, name="index"),
    path('',views.main, name="main"),
    path('gallery/',views.gallery, name="gallery"),
    path('updategallery/',views.updategallery, name="updategallery"),
    path('uploadnotice/',views.uploadnotice, name="uploadnotice"),
    path('admission/',views.admission, name="admission"),
    path('assignments/',views.uploadassignment, name="uploadassignment"),
    path('uploadgallery/',views.uploadgallery, name="uploadgallery"),
    path('allassignments/',views.allassignments, name="allassignments"),
    path('all-admissions/',views.alladmission, name="alladmission"),
    path('filterclass/',views.classwise, name="classwise"),
    path('login/', views.handleLogin, name='handleLogin'),
    path('logout/', views.handleLogout, name='handleLogout'),
    path('signup/', views.signUp, name='signUp'),
    path('update/<int:id>/',views.update_data,name="updatedata"),
    path('delete/<int:id>/',views.delete_data,name="deletedata"),
    path('deletegallery/<int:id>/',views.delete_gallery,name="deletegallery"),
    path('character_pdf/<int:id>',views.CharacterCertificate_PDF, name='character_pdf'),
    path('dob_pdf/<int:id>',views.DOBCertificate_PDF, name='dob_pdf'),
    path('id/<int:id>',views.IDCard_PDF, name='idcard_pdf'),
    path('transfer_pdf/<int:id>',views.TransferCertificate_PDF, name='transfer_pdf'),
    path('download_admission_form_pdf/<int:id>',views.Download_Admission_Form_PDF, name='download_admission_form_pdf'),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)