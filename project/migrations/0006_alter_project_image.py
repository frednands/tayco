# Generated by Django 5.0.4 on 2024-04-13 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0005_alter_project_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.FileField(default='project/noimag.png', upload_to='project'),
        ),
    ]
