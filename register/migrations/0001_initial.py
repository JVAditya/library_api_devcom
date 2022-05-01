# Generated by Django 4.0.4 on 2022-04-27 11:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('student', '0001_initial'),
        ('book', '0004_book_student'),
    ]

    operations = [
        migrations.CreateModel(
            name='Register',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('ISD', 'ISSUED'), ('RTD', 'RETURNED')], default='ISD', max_length=10)),
                ('action_time', models.DateTimeField(auto_now_add=True)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='book.book')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='student.student')),
            ],
        ),
    ]
