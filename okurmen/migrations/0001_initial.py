# Generated by Django 4.2.7 on 2024-01-25 12:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Manager',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('responsibilities', models.TextField()),
                ('directed_students_count', models.IntegerField()),
                ('manager_number', models.CharField(max_length=17)),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('programming_type', models.CharField(choices=[('Frontend', 'Frontend'), ('Backend', 'Backend'), ('UX/UI', 'UX/UI')], max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('number', models.CharField(max_length=10)),
                ('payment', models.IntegerField()),
                ('payment_date', models.DateField(blank=True, null=True)),
                ('payment_receipt', models.ImageField(blank=True, null=True, upload_to='payment_receipts/')),
                ('manager', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='okurmen.manager')),
            ],
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('mentor', models.CharField(max_length=255)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('trainer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='okurmen.teacher')),
            ],
        ),
    ]
