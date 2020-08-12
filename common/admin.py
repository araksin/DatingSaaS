from django.contrib import admin
from common import models as m

admin.site.register(m.Service)
admin.site.register(m.Profile)
admin.site.register(m.ProfilePhoto)
admin.site.register(m.Like)
