# Generated by Django 3.2.8 on 2021-11-01 05:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('forum', '0003_forumpost_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='forumpost',
            name='description',
            field=models.TextField(),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('author', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('parentForum', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='forum.forumpost')),
            ],
        ),
    ]
