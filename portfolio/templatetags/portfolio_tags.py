from portfolio import models
from mezzanine import template

register = template.Library()

@register.as_tag
def promoted_portfolio(*args):
  return list(models.PortfolioPage.objects.filter(promoted=True))
