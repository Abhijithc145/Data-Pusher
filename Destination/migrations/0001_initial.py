# Generated by Django 4.1 on 2022-08-20 07:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Account', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dstinations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Destination_Url', models.URLField()),
                ('Http_method', models.CharField(choices=[('GET', 'GET'), ('PUT', 'PUT'), ('POST', 'POST'), ('PATCH', 'PATCH'), ('DELETE', 'DELETE')], default='1', max_length=50)),
                ('Header', models.JSONField()),
                ('Account_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Account.account')),
            ],
        ),
    ]
