# Custom views

from django.shortcuts import render

def admin_js(request):
  return render(request, 'js/admin.js', content_type='text/javascript')
