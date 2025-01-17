# Generated by Django 4.2.13 on 2024-08-24 07:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_img', models.ImageField(blank=True, null=True, upload_to='students/')),
                ('Admission_number', models.IntegerField(blank=True, default=0, null=True)),
                ('Roll_no', models.IntegerField(blank=True, default=0, null=True)),
                ('Name', models.CharField(max_length=100)),
                ('Age', models.IntegerField(blank=True, default=0, null=True)),
                ('Father_name', models.CharField(max_length=100, null=True)),
                ('Father_phone_Number', models.IntegerField(blank=True, default=0, null=True)),
                ('Mother_phone_Number', models.IntegerField(blank=True, default=0, null=True)),
                ('class_name', models.CharField(max_length=100, null=True)),
                ('Address', models.CharField(max_length=100, null=True)),
                ('Total_fees', models.IntegerField(blank=True, default=0, null=True)),
                ('First_term_fee', models.IntegerField(blank=True, default=0, null=True)),
                ('Second_term_fee', models.IntegerField(blank=True, default=0, null=True)),
                ('Third_term_fee', models.IntegerField(blank=True, default=0, null=True)),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='student_profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
