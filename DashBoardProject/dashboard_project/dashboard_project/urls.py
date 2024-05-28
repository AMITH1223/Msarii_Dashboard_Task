"""
URL configuration for dashboard_project project.

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
from dashboard_app.views import ProjectListCreate,TaskListCreate,NotificationListCreate,loginLandingpage,login,adminFilteration,managerFilteration,employeeFilteration

urlpatterns = [
    path('admin/', admin.site.urls),
    path('projects/', ProjectListCreate.as_view(), name='project-list'),
    path('tasks/', TaskListCreate.as_view(), name='task-list'),
    path('Notification/', NotificationListCreate.as_view(), name='Notification-list'),
    path('', loginLandingpage),
    path('user_logins', login, name='login'),
    path('admin_filter_status/', adminFilteration, name='admin_filter_status'),
    path('manager_filter_status/', managerFilteration, name='manager_filter_status'),
    path('employee_filter_status/', employeeFilteration, name='employee_filter_status'),
]
