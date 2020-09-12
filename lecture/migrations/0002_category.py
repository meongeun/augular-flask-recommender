# Generated by Django 3.1.1 on 2020-09-12 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lecture', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('categoryidx', models.AutoField(db_column='categoryIdx', primary_key=True, serialize=False)),
                ('categoryname', models.CharField(db_column='categoryName', max_length=20)),
            ],
            options={
                'db_table': 'category',
                'managed': False,
            },
        ),
    ]