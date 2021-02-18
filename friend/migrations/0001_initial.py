<<<<<<< HEAD
<<<<<<< HEAD
# Generated by Django 3.1.5 on 2021-02-16 05:25
=======
# Generated by Django 3.1.5 on 2021-02-15 16:08
>>>>>>> jihyun
=======
# Generated by Django 3.1.5 on 2021-02-15 16:08
>>>>>>> jihyun

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Motivation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.PositiveIntegerField(default=1)),
                ('friend', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='motivation_friend_set', to=settings.AUTH_USER_MODEL)),
                ('me', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='motivation_me_set', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Friendship',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('accepted', models.BooleanField(default=False)),
                ('friend', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='friend_set', to=settings.AUTH_USER_MODEL)),
                ('me', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='self_set', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('me', 'friend')},
            },
        ),
    ]
