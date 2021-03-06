# Generated by Django 3.0.3 on 2020-05-19 01:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0008_auto_20200518_1425'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='profilepic',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='order',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='content.Customer'),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('OUT OF DELIVERED', 'OUT OF DELIVERED'), ('DELIVERED', 'DELIVERED'), ('PENDING', 'PENDING')], max_length=200),
        ),
    ]
