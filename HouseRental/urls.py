from django.contrib import admin
from django.urls import path,include
from HouseRental.views import *
from HouseRental.views import page_not_found
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, \
    PasswordResetCompleteView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',Home,name='home'),
    path('post',RentPost,name='post'),
    path('contact',ContactView,name='contact'),
    path('faq',FaqView,name='faq'),
    path('about',AboutView,name='about'),
    path('details/<int:id>',Details,name="details"),
    path('checkout/<int:id>',create_checkout_session,name="checkout"),
    path('success/', success, name='success'),
    path('cancel/', cancel, name='cancel'),
    path('reset-password/',
         PasswordResetView.as_view(template_name='App_Account/password_reset_form.html'), name='password_reset'),
    path('reset-password/done/',
         PasswordResetDoneView.as_view(template_name='App_Account/password_reset_done.html'), name='password_reset_done'),
    path('reset-password/confirm/<uidb64>/<token>/',
         PasswordResetConfirmView.as_view(template_name='App_Account/password_reset_confirm.html'),
         name='password_reset_confirm'),
    path('reset-password/complete/',
         PasswordResetCompleteView.as_view(template_name='App_Account/password_reset_complete.html'),
         name='password_reset_complete'),
    path('account/',include('App_Account.urls')),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
# handler404 = page_not_found