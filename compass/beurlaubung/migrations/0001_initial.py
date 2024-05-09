# Generated by Django 3.1.1 on 2024-05-09 14:55

import autoslug.fields
from django.db import migrations, models
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='beurlaubung',
            fields=[
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('slug', autoslug.fields.AutoSlugField(unique=True)),
                ('name', models.CharField(max_length=255, verbose_name='Name des Antragsstellers')),
                ('klasse', models.CharField(max_length=10, verbose_name='Klasse des Antragsstellers')),
                ('datum_gestellt', models.DateTimeField(auto_now_add=True)),
                ('tutor', models.CharField(max_length=3, verbose_name='Kürzel des Tuturs')),
                ('begruendung', models.CharField(max_length=1000, verbose_name='Begründung des Antrages')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]