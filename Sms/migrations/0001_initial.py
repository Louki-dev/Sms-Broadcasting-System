# Generated by Django 3.2.3 on 2021-05-28 05:09

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
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message_content', models.TextField()),
                ('message_status', models.SmallIntegerField(default='1')),
                ('message_is_sent', models.SmallIntegerField(default='0')),
                ('message_created_at', models.DateTimeField(auto_now_add=True)),
                ('message_created_by', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Sent_message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sent_message_message', models.CharField(max_length=255)),
                ('sent_message_contact', models.CharField(max_length=255)),
                ('sent_message_created_at', models.DateTimeField(auto_now_add=True)),
                ('sent_message_created_by', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Opt_in',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('opt_in_mobile_number', models.CharField(max_length=255)),
                ('opt_in_token', models.TextField()),
                ('opt_in_status', models.SmallIntegerField(default='1')),
                ('opt_in_created_at', models.DateTimeField(auto_now_add=True)),
                ('opt_in_updated_at', models.DateTimeField(blank=True, default='', null=True)),
                ('opt_out_at', models.DateTimeField(blank=True, default='', null=True)),
                ('opt_in_created_by', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='opt_in_created_by', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact_first_name', models.CharField(max_length=255, null=True)),
                ('contact_last_name', models.CharField(max_length=255, null=True)),
                ('contact_mobile_number', models.CharField(max_length=10, null=True)),
                ('contact_email', models.EmailField(max_length=255, null=True)),
                ('contact_status', models.SmallIntegerField(default='0')),
                ('contact_created_at', models.DateTimeField(auto_now_add=True)),
                ('contact_updated_at', models.DateTimeField(blank=True, default='2021-01-01 00:00:00.000000', null=True)),
                ('contact_last_joined', models.DateTimeField(blank=True, default='2021-01-01 00:00:00.000000', null=True)),
                ('contact_created_by', models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, related_name='contact_created_by', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
