# Generated by Django 3.0.7 on 2021-07-12 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0002_auto_20210712_1447'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='correctAnswer',
            new_name='correct_answer',
        ),
        migrations.AlterField(
            model_name='question',
            name='topic',
            field=models.CharField(max_length=50),
        ),
    ]
