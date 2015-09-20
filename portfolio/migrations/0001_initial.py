# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import mezzanine.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_auto_20150527_1555'),
    ]

    operations = [
        migrations.CreateModel(
            name='PortfolioPage',
            fields=[
                ('page_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='pages.Page')),
                ('content', mezzanine.core.fields.RichTextField(verbose_name='Content')),
                ('summary', models.CharField(max_length=1000)),
                ('promoted', models.BooleanField(default=False)),
                ('image', mezzanine.core.fields.FileField(max_length=255, null=True, blank=True)),
            ],
            options={
                'ordering': ('_order',),
                'abstract': False,
                'verbose_name': 'Portfolio Page',
                'verbose_name_plural': 'Portfolio Pages',
            },
            bases=('pages.page', models.Model),
        ),
        migrations.CreateModel(
            name='PortfolioPageAttachment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255)),
                ('attachment', mezzanine.core.fields.FileField(max_length=255, null=True, blank=True)),
                ('page', models.ForeignKey(related_name='attachments', to='portfolio.PortfolioPage')),
            ],
        ),
    ]
