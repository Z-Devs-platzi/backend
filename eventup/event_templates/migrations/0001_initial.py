# Generated by Django 3.1 on 2020-08-30 18:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Layout',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('active', 'Active element'), ('inactive', 'Inactive element')], default='active', help_text='Status of the object base.', max_length=32, verbose_name='status')),
                ('created', models.DateTimeField(auto_now_add=True, help_text='Date time on which the object was created.', verbose_name='created at')),
                ('modified', models.DateTimeField(auto_now=True, help_text='Date time on which the object was last modified.', verbose_name='modified at')),
                ('deleted', models.DateTimeField(auto_now=True, help_text='Date time on which the object was delete.', verbose_name='deleted at')),
                ('comment', models.CharField(max_length=500)),
            ],
            options={
                'ordering': ['-status', '-created', '-modified', '-deleted'],
                'get_latest_by': 'created',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Template',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('active', 'Active element'), ('inactive', 'Inactive element')], default='active', help_text='Status of the object base.', max_length=32, verbose_name='status')),
                ('created', models.DateTimeField(auto_now_add=True, help_text='Date time on which the object was created.', verbose_name='created at')),
                ('modified', models.DateTimeField(auto_now=True, help_text='Date time on which the object was last modified.', verbose_name='modified at')),
                ('deleted', models.DateTimeField(auto_now=True, help_text='Date time on which the object was delete.', verbose_name='deleted at')),
                ('name', models.CharField(blank=True, max_length=100, unique=True)),
                ('colors', models.CharField(max_length=255)),
                ('banner', models.ImageField(blank=True, null=True, upload_to='banner/pictures/', verbose_name='banner picture')),
                ('font', models.CharField(blank=True, max_length=100)),
                ('layout', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='event_templates.layout')),
            ],
            options={
                'ordering': ['-status', '-created', '-modified', '-deleted'],
                'get_latest_by': 'created',
                'abstract': False,
            },
        ),
    ]