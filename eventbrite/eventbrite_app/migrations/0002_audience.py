# Generated by Django 4.1.6 on 2023-02-24 05:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('eventbrite_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Audience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('branch', models.CharField(choices=[('Computer', 'Computer'), ('AIML', 'AIML'), ('Data Science', 'Data Science'), ('IOT', 'IOT')], max_length=50)),
                ('semester', models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8')], max_length=50)),
                ('rollNumber', models.PositiveIntegerField()),
                ('erp', models.PositiveBigIntegerField()),
                ('isAudience', models.BooleanField(default=False)),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('updatedAt', models.DateTimeField(auto_now=True)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eventbrite_app.event')),
            ],
        ),
    ]
