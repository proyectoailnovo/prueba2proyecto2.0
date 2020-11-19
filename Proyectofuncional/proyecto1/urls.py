from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.auth import views as auth_views
from account.views import(
	registrarse_view,
	logout_view,
	login_view,
    account_view,
    must_authenticate_view,
	)
from blog.views import(
    create_blog_view,
    home,
    comprar,
    galeriaimg,
    historiapag,
    blog,
    medio_pago,
    )
from soporte.views import(
    soporte_pag,
)

urlpatterns = [
    
    path('admin/', admin.site.urls),
    
    path('', home, name=""),

    path('blog/', include('blog.urls', 'blog')),

    path('comprar/', comprar, name='comprar-pag'),

    path('medio_pago/', medio_pago, name='medio_de_pago'),
    
    path('register/',registrarse_view, name='register'),
    
    path('logout/',logout_view, name='logout'),
    
    path('login/',login_view, name='login'),
    
    path('account/',account_view, name="account"),

    path('must_authenticate/',must_authenticate_view, name="must_authenticate"),
    
    path('galeria/',galeriaimg, name="galeriaimgp"),
    
    path('historia/', historiapag, name="historiapag1"),
    
    path('blog/', blog, name="sector_blog1"),#esto puede causar un error

    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(template_name='../templates/account/registration/password_change_done.html'), 
        name='password_change_done'),

    path('password_change/', auth_views.PasswordChangeView.as_view(template_name='../templates/account/registration/password_change.html'), 
        name='password_change'),

    path('password_reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='../templates/account/registration/password_reset_done.html'),
     name='password_reset_done'),

    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='../templates/account/registration/password_reset_confirm.html'), name='password_reset_confirm'),

    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='../templates/account/registration/password_reset_form.html'), name='password_reset'),

    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='../templates/account/registration/password_reset_complete.html'),
     name='password_reset_complete'),

    path('soporte/', soporte_pag, name='soporte'),


]
if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)