# Generated by Django 3.0 on 2020-02-21 14:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_auto_20200220_1211'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='area',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='user.Area'),
        ),
    ]