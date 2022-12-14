# Generated by Django 3.2.12 on 2022-08-27 12:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('school_name', models.CharField(max_length=120)),
                ('email', models.EmailField(max_length=254, null=True, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_name', models.CharField(max_length=120)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('address', models.CharField(max_length=120)),
                ('school_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app3.school')),
            ],
        ),
    ]
