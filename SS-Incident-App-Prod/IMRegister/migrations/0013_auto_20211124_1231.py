# Generated by Django 3.2.7 on 2021-11-24 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('IMRegister', '0012_alter_incident_files'),
    ]

    operations = [
        migrations.RenameField(
            model_name='incident',
            old_name='files',
            new_name='file1',
        ),
        migrations.AddField(
            model_name='incident',
            name='file2',
            field=models.FileField(blank=True, null=True, upload_to='', verbose_name='Attach Pictures'),
        ),
        migrations.AddField(
            model_name='incident',
            name='file3',
            field=models.FileField(blank=True, null=True, upload_to='', verbose_name='Attach Pictures'),
        ),
        migrations.AddField(
            model_name='incident',
            name='file4',
            field=models.FileField(blank=True, null=True, upload_to='', verbose_name='Attach Pictures'),
        ),
    ]
