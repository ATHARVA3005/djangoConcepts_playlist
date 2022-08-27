
from django.contrib import admin
from django.urls import path, include

from gs6.course import urls as cv
from gs6.fees import urls as fv



urlpatterns = [
    path('admin/', admin.site.urls),
    path('cor/', include(cv.urls)),
    path('fe/', include(fv.urls)),
]
