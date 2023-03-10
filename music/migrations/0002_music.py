# Generated by Django 4.1.5 on 2023-01-31 05:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Music',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, unique=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('country', models.CharField(choices=[('KG', 'Кыргызстан'), ('KZ', 'Казахстан'), ('RU', 'Россия')], max_length=50)),
                ('duration', models.FloatField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='musics', to='music.category')),
            ],
            options={
                'db_table': 'product',
            },
        ),
    ]
