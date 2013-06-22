from django.db import models
from mezzanine.pages.models import Page
from mezzanine.core.models import RichText
from mezzanine.core import fields
from mezzanine.utils.models import upload_to

class PortfolioPage(Page, RichText):
  summary = models.CharField(max_length=1000)
  promoted = models.BooleanField(default=False)
  image = fields.FileField(upload_to=upload_to("portfolio.PortfolioPage.image",
                                               "portfolio_images"),
                           format="Image", null=True, blank=True, max_length=255)

  class Meta(Page.Meta):
    verbose_name = "Portfolio Page"
    verbose_name_plural = "Portfolio Pages"


class PortfolioPageAttachment(models.Model):
  title = models.CharField(max_length=255)
  page = models.ForeignKey(PortfolioPage, related_name='attachments')
  attachment = fields.FileField(upload_to=upload_to("portfolio.PortfolioPageAttachment.attachment",
                                                    "portfolio_attachments"),
                                null=True, blank=True, max_length=255)
