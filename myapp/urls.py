from django.urls import path
from . import views
urlpatterns = [
    path('',views.index, name='index'),
    path('login/', views.login, name = 'login'),
    path('signup/', views.signup, name = 'signup'),
    path('forgot_password/',views.forgot_password,name='forgot_password'),
    path('otp_verify/',views.otp_verify,name='otp_verify'),
    path('logout/',views.logout,name='logout'),
    path('pass_form/',views.pass_form,name='pass_form'),
    path("user_pass/",views.user_pass,name="user_pass"),
    path('otp_password/',views.otp_password,name='otp_password'),
    path('user_password/',views.user_password,name = 'user_password'),

    path("render_pdf_view/",views.render_pdf_view,name="render_pdf_view"),

    path("user_update/<int:pk>",views.UserUpdateView.as_view(),name ="user_update"),
    path("pass_update/<int:pk>",views.PassUpdateView.as_view(),name="pass_update"),

    path("pass_delete/<int:pk>",views.PassDeleteView.as_view(),name = "pass_delete"),
    path("user_delete/<int:pk>",views.UserDeleteView.as_view(),name = "user_delete"),

    


]
