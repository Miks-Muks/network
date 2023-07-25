from django.contrib import admin
from .models import Profile, AddedPhoto, LinksProfile, KaifarikUser, Role, Speciality

# Register your models here.
admin.site.register(Profile)
admin.site.register(AddedPhoto)
admin.site.register(LinksProfile)
admin.site.register(Role)
admin.site.register(Speciality)


@admin.register(KaifarikUser)
class UserAdmin(admin.ModelAdmin):
    pass
