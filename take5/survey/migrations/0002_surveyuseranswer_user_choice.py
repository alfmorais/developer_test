# Generated by Django 3.2.6 on 2021-08-28 20:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='surveyuseranswer',
            name='user_choice',
            field=models.CharField(choices=[('a)', 'FIRST ALTERNATIVE'), ('b)', 'SECOND ALTERNATIVE'), ('c)', 'THIRD ALTERNATIVE')], default=1, max_length=255),
            preserve_default=False,
        ),
    ]
