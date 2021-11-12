# Generated by Django 3.2.3 on 2021-11-12 16:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rollingPaper', '0002_alter_rollinginfo_rolling_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rollinginfo',
            name='code',
        ),
        migrations.AddField(
            model_name='rollinginfo',
            name='comment',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='rollingPaper.comment'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='description',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='comment',
            name='password',
            field=models.IntegerField(default=''),
        ),
    ]
