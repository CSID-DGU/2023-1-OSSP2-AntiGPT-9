# Generated by Django 4.2 on 2023-05-15 15:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_remove_answer_create_date_remove_chatroom_chatset_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChatSet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_date', models.DateTimeField()),
                ('Answer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.answer')),
                ('ChatRoom', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.chatroom')),
                ('Question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.question')),
            ],
        ),
    ]
