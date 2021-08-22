# Generated by Django 3.2 on 2021-08-21 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('covid', '0012_medicaldata_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='medicaldata',
            name='Age',
        ),
        migrations.RemoveField(
            model_name='medicaldata',
            name='Gender',
        ),
        migrations.AddField(
            model_name='medicaldata',
            name='Fits',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=50, null=True),
        ),
    ]