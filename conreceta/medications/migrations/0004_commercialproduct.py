# Generated by Django 3.2.15 on 2022-09-03 19:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('medications', '0003_rename_medication_clinicalmedication'),
    ]

    operations = [
        migrations.CreateModel(
            name='CommercialProduct',
            fields=[
                ('concept_id', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('clinical_medication_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='medications.clinicalmedication')),
            ],
        ),
    ]
