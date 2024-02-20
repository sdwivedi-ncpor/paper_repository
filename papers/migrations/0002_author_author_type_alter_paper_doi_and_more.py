# Generated by Django 5.0.2 on 2024-02-20 04:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('papers', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='author_type',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='paper',
            name='doi',
            field=models.CharField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='paper',
            name='publication',
            field=models.CharField(),
        ),
    ]