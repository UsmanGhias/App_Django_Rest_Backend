
from django.contrib.gis import admin
from django.contrib.gis.admin.widgets import OSMWidget
from .models import Profile, Photo, Group, Match, VerificationCode

class CustomOSMGeoAdmin(admin.OSMGeoAdmin):
    map_widget = OSMWidget

admin.site.register(Profile, CustomOSMGeoAdmin)
admin.site.register(Photo, CustomOSMGeoAdmin)
admin.site.register(Match, CustomOSMGeoAdmin)
admin.site.register(Group, CustomOSMGeoAdmin)
admin.site.register(VerificationCode, CustomOSMGeoAdmin)








# --------------------------
# # from django.contrib.gis import admin
# # from .models import Profile, Photo, Group, Match, VerificationCode
# #
# # # Register your models here.
# # #admin.site.register(Profile, admin.OSMGeoAdmin)
# # admin.site.register(Photo, admin.OSMGeoAdmin)
# # admin.site.register(Match, admin.OSMGeoAdmin)
# # admin.site.register(Group, admin.OSMGeoAdmin)
# # admin.site.register(VerificationCode, admin.OSMGeoAdmin)
# from django.contrib.gis import admin
# from django.contrib.gis.db import models
# from django.contrib.admin.widgets import OpenLayersWidget  # Import the appropriate widget
#
# from .models import Profile, Photo, Group, Match, VerificationCode
#
# class CustomOSMGeoAdmin(admin.OSMGeoAdmin):  # You can also use admin.ModelAdmin if needed
#     map_widget = OpenLayersWidget  # Use the OpenLayersWidget or LeafletWidget
#
# admin.site.register(Profile, CustomOSMGeoAdmin)
# admin.site.register(Photo, CustomOSMGeoAdmin)
# admin.site.register(Match, CustomOSMGeoAdmin)
# admin.site.register(Group, CustomOSMGeoAdmin)
# admin.site.register(VerificationCode, CustomOSMGeoAdmin)
