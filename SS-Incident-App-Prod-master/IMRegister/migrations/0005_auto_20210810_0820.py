# Generated by Django 3.2.6 on 2021-08-10 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('IMRegister', '0004_auto_20210809_1902'),
    ]

    operations = [
        migrations.AlterField(
            model_name='incident',
            name='date_reported',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Report Date'),
        ),
        migrations.AlterField(
            model_name='incident',
            name='direct_cause',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Direct Cause of Incident'),
        ),
        migrations.AlterField(
            model_name='incident',
            name='files',
            field=models.FileField(blank=True, null=True, upload_to='', verbose_name='Attach Pictures'),
        ),
        migrations.AlterField(
            model_name='incident',
            name='imme_action',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Immediate action taken'),
        ),
        migrations.AlterField(
            model_name='incident',
            name='imme_action_when',
            field=models.DateTimeField(blank=True, null=True, verbose_name='When'),
        ),
        migrations.AlterField(
            model_name='incident',
            name='imme_action_whom',
            field=models.CharField(blank=True, max_length=60, null=True, verbose_name='By whom'),
        ),
        migrations.AlterField(
            model_name='incident',
            name='incident_area',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Incident Area'),
        ),
        migrations.AlterField(
            model_name='incident',
            name='incident_area_detail',
            field=models.CharField(blank=True, max_length=250, null=True, verbose_name='Incident Area description'),
        ),
        migrations.AlterField(
            model_name='incident',
            name='incident_date',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Incident Date'),
        ),
        migrations.AlterField(
            model_name='incident',
            name='incident_description',
            field=models.CharField(max_length=2220, verbose_name='Incident Description (Full Details'),
        ),
        migrations.AlterField(
            model_name='incident',
            name='incident_time',
            field=models.TimeField(blank=True, null=True, verbose_name='Incident Time'),
        ),
        migrations.AlterField(
            model_name='incident',
            name='incident_type',
            field=models.CharField(max_length=200, verbose_name='Incident Type'),
        ),
        migrations.AlterField(
            model_name='incident',
            name='job_role',
            field=models.CharField(max_length=90, verbose_name='Job Role'),
        ),
        migrations.AlterField(
            model_name='incident',
            name='lessons',
            field=models.CharField(blank=True, max_length=2220, null=True, verbose_name='Lesson(s) learned from Incident'),
        ),
        migrations.AlterField(
            model_name='incident',
            name='long_action',
            field=models.CharField(blank=True, max_length=600, null=True, verbose_name='Long term action taken'),
        ),
        migrations.AlterField(
            model_name='incident',
            name='long_action_when',
            field=models.DateTimeField(blank=True, null=True, verbose_name='When'),
        ),
        migrations.AlterField(
            model_name='incident',
            name='long_action_whom',
            field=models.CharField(blank=True, max_length=60, null=True, verbose_name='By whom'),
        ),
        migrations.AlterField(
            model_name='incident',
            name='loss',
            field=models.CharField(blank=True, max_length=220, null=True, verbose_name='Material/Equipment Loss (if any)'),
        ),
        migrations.AlterField(
            model_name='incident',
            name='lost_hr',
            field=models.IntegerField(blank=True, null=True, verbose_name='Lost Hour'),
        ),
        migrations.AlterField(
            model_name='incident',
            name='name',
            field=models.CharField(max_length=150, verbose_name='Name (Surname First)'),
        ),
        migrations.AlterField(
            model_name='incident',
            name='person_involved',
            field=models.CharField(max_length=220, verbose_name='Person(s) involved in Incident'),
        ),
        migrations.AlterField(
            model_name='incident',
            name='report_method',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Report Method'),
        ),
        migrations.AlterField(
            model_name='incident',
            name='reported_to',
            field=models.CharField(blank=True, max_length=80, null=True, verbose_name='Reported to (if it has been unofficially reported)'),
        ),
        migrations.AlterField(
            model_name='incident',
            name='root_cause',
            field=models.CharField(blank=True, max_length=400, null=True, verbose_name='Root Cause of Incident'),
        ),
        migrations.AlterField(
            model_name='incident',
            name='site_name',
            field=models.CharField(max_length=50, verbose_name='Site (Incident Location) Name'),
        ),
        migrations.AlterField(
            model_name='incident',
            name='witness',
            field=models.CharField(blank=True, max_length=220, null=True, verbose_name='Witness (if any)'),
        ),
    ]