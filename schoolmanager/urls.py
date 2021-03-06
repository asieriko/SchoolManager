from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'schoolmanager.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', TemplateView.as_view(template_name="main_index.html"), name='main_index'),
    url(r'^student_manager/', include('students_manager.urls')),
    url(r'^qms/', include('school_qms.urls')),
    url(r'^forms/', include('custom_forms.urls')),
    url(r'^timetable/', include('timetable.urls')),
    url(r'^persons/', include('orgperson.urls')),
    url(r'^groups/', include('groups.urls')),
    url(r'^enrollment/', include('enrollment.urls')),
    #url(r'^$', 'students_manager.views.home_page', name='home'),
    #url(r'^students/', 'students_manager.views.students_page', name='students'),
    #url(r'^groups/', 'students_manager.views.groups_page', name='groups'),
    #url(r'^admin/', include(admin.site.urls)),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
