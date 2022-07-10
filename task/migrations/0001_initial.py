# Generated by Django 4.0.5 on 2022-06-28 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=255)),
                ('status', models.CharField(choices=[('Todo', 'Todo'), ('Done', 'Done')], default='Todo', max_length=10)),
            ],
        ),
    ]
