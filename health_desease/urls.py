from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from health import views
from health.views import (
    Home, contact_view, simple_page, predict_heart_disease, save_prescription,
    get_prescriptions, CancelAppointmentView, view_prescriptions,
    chatbot_view, get_chatbot_response, Patient_Home, Doctor_Home, admin_home,
    About, contact, Gallery, Login_User, Login_admin, Signup_User, Logout,
    Change_Password, add_heartdetail, information_hub, view_search_pat,
    View_Doctor, add_doctor, View_Patient, View_Feedback, Edit_My_deatail,
    View_My_Detail, sent_feedback, error_page, book_appointment,
    admin_confirm_appointment, admin_cancel_appointment, verify_payment,
    view_receipt, upload_receipt, view_availabilities, add_availability,
    edit_availability, delete_availability, doctor_availability, delete_searched,
    delete_doctor, assign_status, delete_patient, delete_feedback,
    predict_desease, find_doctor, confirm_appointment, cancel_appointment,
    manage_appointments, patient_appointments, DoctorAvailability,
    heart_rate_view
)

from .apirep import routerep

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(routerep.urls)),

    path('', Home, name="home"),
    path('blog/', include('blog.urls')),
    path('contact/', contact_view, name='contact'),
    path('simple-page/', simple_page, name='simple_page'),
    path('predict_heart_disease/', predict_heart_disease, name='predict_heart_disease'),
    path('save_prescription/', save_prescription, name='save_prescription'),
    path('get_prescriptions/', get_prescriptions, name='get_prescriptions'),
    path('view_prescriptions/<int:patient_id>/<int:doctor_id>/', view_prescriptions, name='view_prescriptions'),

    # Appointment management
    path('book_appointment/<int:availability_id>/', book_appointment, name='book_appointment'),
    path('book_appointment/<int:doctor_id>/<int:slot_id>/', book_appointment, name='book_appointment'),
    path('book_appointment/<int:doctor_id>/', views.book_appointment_view, name='book_appointment'),
    path('appointment/confirm/<int:appointment_id>/', confirm_appointment, name='confirm_appointment'),
    path('appointment/cancel/<int:appointment_id>/', cancel_appointment, name='cancel_appointment'),
    path('appointment/admin_confirm/<int:appointment_id>/', admin_confirm_appointment, name='admin_confirm_appointment'),
    path('appointment/admin_cancel/<int:appointment_id>/', admin_cancel_appointment, name='admin_cancel_appointment'),
    path('verify_payment/<int:appointment_id>/', verify_payment, name='verify_payment'),
    path('upload_receipt/<int:appointment_id>/', upload_receipt, name='upload_receipt'),
    path('view_receipt/<int:payment_id>/', view_receipt, name='view_receipt'),
    path('patient_appointments/', patient_appointments, name='patient_appointments'),
    path('appointments/manage/', manage_appointments, name='manage_appointments'),

    # Availability
    path('availabilities/', view_availabilities, name='view_availabilities'),
    path('add_availability/', add_availability, name='add_availability'),
    path('edit_availability/<int:availability_id>/', edit_availability, name='edit_availability'),
    path('delete_availability/<int:availability_id>/', delete_availability, name='delete_availability'),
    path('doctors/<int:doctor_id>/availability/', doctor_availability, name='doctor_availability'),
    path('doctor_availability/<int:doctor_id>/', doctor_availability, name='doctor_availability'),
    path('DoctorAvailability/', DoctorAvailability, name='DoctorAvailability'),

    # Other pages
    path('patient_home', Patient_Home, name="patient_home"),
    path('doctor_home', Doctor_Home, name="doctor_home"),
    path('admin_home', admin_home, name="admin_home"),
    path('about', About, name="about"),
    path('gallery', Gallery, name="gallery"),
    path('login', Login_User, name="login"),
    path('login_admin', Login_admin, name="login_admin"),
    path('signup', Signup_User, name="signup"),
    path('logout/', Logout, name="logout"),
    path('change_password', Change_Password, name="change_password"),
    path('add_heartdetail', add_heartdetail, name="add_heartdetail"),
    path('information_hub', information_hub, name="information_hub"),

    # Doctor & Patient Management
    path('view_search_pat', view_search_pat, name="view_search_pat"),
    path('view_doctor', View_Doctor, name="view_doctor"),
    path('add_doctor', add_doctor, name="add_doctor"),
    path('change_doctor/<int:pid>/', add_doctor, name="change_doctor"),
    path('view_patient', View_Patient, name="view_patient"),
    path('view_feedback', View_Feedback, name="view_feedback"),
    path('edit_profile', Edit_My_deatail, name="edit_profile"),
    path('profile_doctor', View_My_Detail, name="profile_doctor"),
    path('sent_feedback', sent_feedback, name="sent_feedback"),

    # Admin Actions
    path('delete_searched/<int:pid>', delete_searched, name="delete_searched"),
    path('delete_doctor<int:pid>', delete_doctor, name="delete_doctor"),
    path('assign_status<int:pid>', assign_status, name="assign_status"),
    path('delete_patient<int:pid>', delete_patient, name="delete_patient"),
    path('delete_feedback<int:pid>', delete_feedback, name="delete_feedback"),

    # ML Predictions
    path('predict_desease/<str:pred>/<str:accuracy>/', predict_desease, name="predict_desease"),

    # Chatbot
    path('chatbot/', chatbot_view, name='chatbot'),
    path('chatbot_view/', chatbot_view, name='chatbot_view'),
    path('get_chatbot_response/', get_chatbot_response, name='get_chatbot_response'),

    # Error page
    path('error/<str:message>/', error_page, name='error_page'),

    # Heart rate view (new)
    path('heart-rate/', heart_rate_view, name='heart_rate'),
]

# Serve media files in development
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
