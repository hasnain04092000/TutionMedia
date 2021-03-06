# Generated by Django 3.0.8 on 2020-12-31 16:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20201215_2113'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.RemoveField(
            model_name='profile',
            name='files_url',
        ),
        migrations.AddField(
            model_name='profile',
            name='bio',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='blood_groups',
            field=models.CharField(blank=True, choices=[('A+', 'A+'), ('A-', 'A-'), ('B+', 'B+'), ('B-', 'B-'), ('AB+', 'AB+'), ('AB-', 'AB-')], max_length=5),
        ),
        migrations.AddField(
            model_name='profile',
            name='category',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('student', 'Student'), ('teacher', 'Teacher'), ('employee', 'Employee'), ('employeer', 'Employeer')], max_length=34),
        ),
        migrations.AddField(
            model_name='profile',
            name='gender',
            field=models.CharField(blank=True, choices=[('male', 'Male'), ('female', 'Female')], max_length=10),
        ),
        migrations.AddField(
            model_name='profile',
            name='marital_status',
            field=models.CharField(blank=True, choices=[('married', 'Married'), ('unmarried', 'Unmarried'), ('divorced', 'Divorced'), ('engaged', 'Engaged'), ('separated', 'Separated')], max_length=100),
        ),
        migrations.AlterField(
            model_name='profile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='vedio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vedio', models.URLField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='accounts.Profile')),
            ],
        ),
        migrations.CreateModel(
            name='TutionClassDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tution_class', multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('0', 'Nursery'), ('1', 'One'), ('2', 'Two'), ('3', 'Three'), ('4', 'Four'), ('5', 'Five')], max_length=2, null=True)),
                ('teacher_address', models.CharField(max_length=400)),
                ('tutoring_style', multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('group_tution', 'Group Tution'), ('privet_tution', 'Privet Tution')], max_length=26)),
                ('tutoring_place', multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('class_room', 'Class Room'), ('Coaching_center', 'Coaching Center'), ('home_visit', 'Home Visit'), ('my_place', 'My Place')], max_length=46)),
                ('mediam', multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('bangla_mediam', 'Bangla Mediam'), ('english_mediam', 'English Mediam')], max_length=28)),
                ('days', models.CharField(blank=True, max_length=100)),
                ('status', models.CharField(choices=[('available', 'Available'), ('busy', 'Busy')], max_length=50)),
                ('subject', models.ManyToManyField(related_name='subjects', to='accounts.Subject')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='accounts.Profile')),
            ],
        ),
    ]
