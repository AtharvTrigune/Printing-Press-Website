"""
URL configuration for subhadra project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from myapp import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index),
    path('register/',views.register),
    path('login/',views.ulogin),
    path('about/',views.about),
    path('service/',views.service),
    path('cat/',views.cat),
    path('cat2/',views.cat2),
    path('cat3/',views.cat3),
    path('cat4/',views.cat4),
    path('port/',views.port),
    path('contact/',views.contact_view),
    path('logout/',views.ulogout),
    path('weeding/',views.weeding),
    # path('visiting/',views.visiting),
    # path('add/<pid>/',views.addcart),
    path('pamplate/',views.pamplate),
    path('product_details/<pid>/',views.product_details),
    path('updateqty/<x>/<cid>/',views.updateqty),
    path('addtocart/<pid>/',views.addtocart),
    path('delete/<cid>/',views.deletecart),
    path('cart/',views.viewcart),
    path('payment/',views.makepayment),
    path('placeorder/',views.placeorder),
    path('email_send/',views.email_send),
   path('payment_success/', views.payment_sucess, name='payment_success')

    # path('payment/success/', views.payment_success, name='payment_success'),
   
]
urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)