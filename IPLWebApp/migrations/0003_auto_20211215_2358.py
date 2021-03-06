# Generated by Django 3.1.5 on 2021-12-15 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('IPLWebApp', '0002_addteam'),
    ]

    operations = [
        migrations.CreateModel(
            name='addNewPlayers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('player_name', models.CharField(max_length=20)),
                ('role', models.CharField(max_length=20)),
                ('price', models.CharField(max_length=20)),
                ('status', models.CharField(max_length=20)),
                ('team', models.CharField(max_length=20)),
            ],
        ),
        migrations.RenameField(
            model_name='addteam',
            old_name='player_name',
            new_name='HeadLine',
        ),
        migrations.RemoveField(
            model_name='addteam',
            name='price',
        ),
        migrations.RemoveField(
            model_name='addteam',
            name='role',
        ),
        migrations.RemoveField(
            model_name='addteam',
            name='status',
        ),
        migrations.AddField(
            model_name='addteam',
            name='TeamImage',
            field=models.ImageField(default=True, upload_to='static/image'),
        ),
    ]
