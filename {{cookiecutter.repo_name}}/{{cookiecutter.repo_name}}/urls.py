from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', '{{ cookiecutter.repo_name }}.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', TemplateView.as_view(template_name="home.html")),
    url(r'^theme/$', TemplateView.as_view(template_name="theme-default.html"), name="theme"),
    url(r'^typography/$', TemplateView.as_view(template_name="theme-typography.html"), name="typography"),

)
