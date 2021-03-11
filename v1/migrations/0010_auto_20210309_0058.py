# Generated by Django 3.1.7 on 2021-03-08 15:58

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('v1', '0009_auto_20210304_2322'),
    ]

    operations = [
        migrations.CreateModel(
            name='StampTotal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total', models.IntegerField()),
            ],
            options={
                'db_table': 'stamp_total',
                'managed': False,
            },
        ),
        migrations.AlterField(
            model_name='article',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 8, 15, 58, 20, 853314, tzinfo=utc), help_text='作成日'),
        ),
        migrations.AlterField(
            model_name='stamprecord',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 8, 15, 58, 20, 853314, tzinfo=utc), help_text='作成日'),
        ),
        migrations.AlterField(
            model_name='user',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 8, 15, 58, 20, 853314, tzinfo=utc), help_text='作成日'),
        ),
    ]