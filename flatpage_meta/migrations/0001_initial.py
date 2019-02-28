# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-02-28 09:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('sites', '0002_alter_domain_unique'),
        ('flatpages', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FlatPageMetaTag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=150)),
                ('flatpage', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='meta_tag_set', to='flatpages.FlatPage')),
            ],
            options={
                'verbose_name': 'Meta tag',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='MetaTagType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True)),
                ('format_string', models.CharField(max_length=100)),
                ('description', models.CharField(blank=True, max_length=150, null=True)),
                ('allow_multiple', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='SiteMetaTag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=150)),
                ('meta_tag_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='flatpage_meta_sitemetatag_related', to='flatpage_meta.MetaTagType')),
                ('site', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='meta_tag_set', to='sites.Site')),
            ],
            options={
                'verbose_name': 'Meta tag',
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='flatpagemetatag',
            name='meta_tag_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='flatpage_meta_flatpagemetatag_related', to='flatpage_meta.MetaTagType'),
        ),
    ]
