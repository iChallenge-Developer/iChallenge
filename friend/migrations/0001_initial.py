<<<<<<< Updated upstream
# Generated by Django 3.1.6 on 2021-02-08 15:54
=======
# Generated by Django 3.1.5 on 2021-02-09 04:47
>>>>>>> Stashed changes

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Friendship',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('accepted', models.BooleanField(default=False)),
            ],
        ),
    ]
