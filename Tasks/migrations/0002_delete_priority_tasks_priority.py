# Generated by Django 5.0 on 2023-12-16 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tasks', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Priority',
        ),
        migrations.AddField(
            model_name='tasks',
            name='priority',
            field=models.CharField(blank=True, choices=[('Low', 'Low'), ('Medium', 'Medium'), ('High', 'High')], default='Low', max_length=10, null=True),
        ),
    ]