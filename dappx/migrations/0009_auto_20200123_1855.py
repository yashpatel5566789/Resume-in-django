# Generated by Django 3.0.2 on 2020-01-23 13:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dappx', '0008_auto_20200123_1853'),
    ]

    operations = [
        migrations.AlterField(
            model_name='achievement',
            name='resume',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='dappx.Resume'),
        ),
        migrations.AlterField(
            model_name='additional_courses',
            name='resume',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='dappx.Resume'),
        ),
        migrations.AlterField(
            model_name='career',
            name='resume',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='dappx.Resume'),
        ),
        migrations.AlterField(
            model_name='certification',
            name='resume',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='dappx.Resume'),
        ),
        migrations.AlterField(
            model_name='hobbies',
            name='resume',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='dappx.Resume'),
        ),
        migrations.AlterField(
            model_name='internship',
            name='resume',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='dappx.Resume'),
        ),
        migrations.AlterField(
            model_name='project',
            name='resume',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='dappx.Resume'),
        ),
        migrations.AlterField(
            model_name='workexperience',
            name='resume',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='dappx.Resume'),
        ),
    ]
