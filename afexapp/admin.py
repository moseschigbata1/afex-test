from django.contrib import admin

# Register your models here.


from django.contrib import admin
from afexapp.models import UserProfile, User, Tasks
# Register your models here.
admin.site.register(UserProfile)
admin.site.register(Tasks)