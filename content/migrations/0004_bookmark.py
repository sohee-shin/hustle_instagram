# Generated by Django 3.2.9 on 2021-12-15 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0003_like'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bookmark',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feed_id', models.IntegerField()),
                ('email', models.TextField()),
            ],
            options={
                'unique_together': {('feed_id', 'email')},
            },
        ),
    ]