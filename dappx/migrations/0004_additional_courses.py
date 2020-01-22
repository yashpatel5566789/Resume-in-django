# Generated by Django 3.0.2 on 2020-01-22 13:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dappx', '0003_project'),
    ]

    operations = [
        migrations.CreateModel(
            name='Additional_courses',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=5000)),
                ('resume', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='dappx.Resume')),
            ],
        ),
    ]
