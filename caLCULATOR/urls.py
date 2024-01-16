"""
URL configuration for caLCULATOR project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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

# path("route","View")
# localhost:8000/hello/

from operation import views
# from operation.views import Morning

lst=[102030]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/',views.HelloWorldView.as_view()),
    path('morning/',views.Morning.as_view()),
    path('evening/',views.EveningView.as_view()),
    path('noon/',views.NoonView.as_view()),
    path('night/',views.NightView.as_view()),
    path('add/',views.AdditionView.as_view()),
    path('sub/',views.SubtractionView.as_view()),
    path('div/',views.DivisionView.as_view()),
    path('product/',views.ProductView.as_view()),
    path('cube/',views.CubeView.as_view()),
    path('leap/',views.LeapYearView.as_view()),
    path('longest/',views.LongestWordView.as_view()),
    path('repeat/',views.ReapeatCharView.as_view()),
    path('register/',views.SignUpView.as_view()),
    path('login/',views.SignInView.as_view()),
    path('emi/',views.EmiCalculatorView.as_view())
]
