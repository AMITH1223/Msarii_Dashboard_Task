from django.contrib import admin
from .models import Role,UserProfile,Project,Task,Notification

admin.site.register(Role)
admin.site.register(UserProfile)
admin.site.register(Project)
admin.site.register(Task)
admin.site.register(Notification)