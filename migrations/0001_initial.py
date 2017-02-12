# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import aldryn_translation_tools.models
from django.conf import settings
import parler.models
import djangocms_text_ckeditor.fields
import filer.fields.image
import aldryn_common.admin_fields.sortedm2m
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cms', '0016_auto_20160608_1535'),
        ('filer', '0007_auto_20161016_1055'),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('address', models.TextField(verbose_name='address', blank=True)),
                ('postal_code', models.CharField(max_length=20, verbose_name='postal code', blank=True)),
                ('city', models.CharField(max_length=255, verbose_name='city', blank=True)),
                ('country', models.CharField(max_length=255, verbose_name='country', blank=True)),
                ('phone', models.CharField(blank=True, max_length=100, verbose_name='phone', null=True)),
                ('fax', models.CharField(blank=True, max_length=100, verbose_name='fax', null=True)),
                ('email', models.EmailField(default='', max_length=254, verbose_name='email', blank=True)),
                ('website', models.URLField(blank=True, verbose_name='website', null=True)),
            ],
            options={
                'verbose_name_plural': 'Affiliations',
                'verbose_name': 'Affiliation',
            },
            bases=(aldryn_translation_tools.models.TranslationHelperMixin, aldryn_translation_tools.models.TranslatedAutoSlugifyMixin, parler.models.TranslatableModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='GroupTranslation',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('language_code', models.CharField(db_index=True, max_length=15, verbose_name='Language')),
                ('name', models.CharField(max_length=255, verbose_name='name', help_text="Provide this affiliation's name.")),
                ('description', djangocms_text_ckeditor.fields.HTMLField(verbose_name='description', blank=True)),
                ('slug', models.SlugField(default='', max_length=255, verbose_name='slug', blank=True, help_text='Leave blank to auto-generate a unique slug.')),
                ('master', models.ForeignKey(to='ssrd_people.Group', null=True, editable=False, related_name='translations')),
            ],
            options={
                'verbose_name': 'Affiliation Translation',
                'db_table': 'ssrd_people_group_translation',
                'default_permissions': (),
                'managed': True,
                'db_tablespace': '',
            },
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('phone', models.CharField(blank=True, max_length=100, verbose_name='phone', null=True)),
                ('mobile', models.CharField(blank=True, max_length=100, verbose_name='mobile', null=True)),
                ('fax', models.CharField(blank=True, max_length=100, verbose_name='fax', null=True)),
                ('email', models.EmailField(default='', max_length=254, verbose_name='email', blank=True)),
                ('website', models.URLField(blank=True, verbose_name='website', null=True)),
                ('vcard_enabled', models.BooleanField(default=True, verbose_name='enable vCard download')),
                ('groups', aldryn_common.admin_fields.sortedm2m.SortedM2MModelField(default=None, related_name='people', blank=True, help_text='Choose and order the affiliation for this person, the first will be the "primary affiliation".', to='ssrd_people.Group')),
                ('user', models.OneToOneField(null=True, blank=True, related_name='persons', to=settings.AUTH_USER_MODEL)),
                ('visual', filer.fields.image.FilerImageField(default=None, null=True, blank=True, on_delete=django.db.models.deletion.SET_NULL, to='filer.Image')),
            ],
            options={
                'verbose_name_plural': 'People',
                'verbose_name': 'Person',
            },
            bases=(aldryn_translation_tools.models.TranslationHelperMixin, aldryn_translation_tools.models.TranslatedAutoSlugifyMixin, parler.models.TranslatableModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='PersonTranslation',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('language_code', models.CharField(db_index=True, max_length=15, verbose_name='Language')),
                ('name', models.CharField(default='', max_length=255, verbose_name='name', help_text="Provide this person's name.")),
                ('slug', models.SlugField(default='', max_length=255, verbose_name='unique slug', blank=True, help_text='Leave blank to auto-generate a unique slug.')),
                ('function', models.CharField(default='', max_length=255, verbose_name='role', blank=True)),
                ('description', djangocms_text_ckeditor.fields.HTMLField(default='', verbose_name='description', blank=True)),
                ('master', models.ForeignKey(to='ssrd_people.Person', null=True, editable=False, related_name='translations')),
            ],
            options={
                'verbose_name': 'Person Translation',
                'db_table': 'ssrd_people_person_translation',
                'default_permissions': (),
                'managed': True,
                'db_tablespace': '',
            },
        ),
        migrations.CreateModel(
            name='SPeoplePlugin',
            fields=[
                ('style', models.CharField(default='standard', max_length=50, verbose_name='Style', choices=[('standard', 'Standard'), ('feature', 'Feature')])),
                ('cmsplugin_ptr', models.OneToOneField(serialize=False, to='cms.CMSPlugin', parent_link=True, primary_key=True, related_name='ssrd_people_speopleplugin')),
                ('group_by_group', models.BooleanField(default=True, verbose_name='group by group', help_text='Group people by their group.')),
                ('show_ungrouped', models.BooleanField(default=False, verbose_name='show ungrouped', help_text='When using "group by group", show ungrouped people too.')),
                ('show_links', models.BooleanField(default=False, verbose_name='Show links to Detail Page')),
                ('show_vcard', models.BooleanField(default=False, verbose_name='Show links to download vCard')),
                ('people', aldryn_common.admin_fields.sortedm2m.SortedM2MModelField(blank=True, help_text='Select and arrange specific people, or, leave blank to select all.', to='ssrd_people.Person')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.AlterUniqueTogether(
            name='persontranslation',
            unique_together=set([('language_code', 'master')]),
        ),
        migrations.AlterUniqueTogether(
            name='grouptranslation',
            unique_together=set([('language_code', 'master')]),
        ),
    ]
