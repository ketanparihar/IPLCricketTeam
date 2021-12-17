# Generated by Django 3.1.5 on 2021-12-17 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('IPLWebApp', '0003_auto_20211215_2358'),
    ]

    operations = [
        migrations.CreateModel(
            name='TeamSearch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team', models.CharField(max_length=20)),
                ('players', models.CharField(max_length=20)),
            ],
        ),
        migrations.AlterField(
            model_name='addteam',
            name='TeamImage',
            field=models.ImageField(upload_to='static/image'),
        ),
    ]
