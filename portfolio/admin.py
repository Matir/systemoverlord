from django.contrib import admin
from mezzanine.pages.admin import PageAdmin
from mezzanine.core import admin as mezzanine_admin
import models


class PortfolioPageAttachmentAdmin(mezzanine_admin.TabularDynamicInlineAdmin):
  model = models.PortfolioPageAttachment

class PortfolioPageAdmin(PageAdmin):
  inlines = PageAdmin.inlines + [PortfolioPageAttachmentAdmin]

admin.site.register(models.PortfolioPage, PortfolioPageAdmin)
