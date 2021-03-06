# Generated by Django 3.2.3 on 2021-06-04 11:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Agent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('surname', models.CharField(max_length=64)),
                ('phoneNum', models.IntegerField(max_length=64)),
                ('email', models.EmailField(max_length=254)),
                ('birthDate', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField(max_length=400)),
                ('agentID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='AgentID', to='website.agent')),
            ],
        ),
    ]
