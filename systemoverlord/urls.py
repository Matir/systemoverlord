from django.conf.urls import patterns, url

urlpatterns = patterns("systemoverlord.views",
  url("^js/admin.js$", "admin_js", name="so_admin_js"),
)
