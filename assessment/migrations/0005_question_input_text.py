# Generated by Django 5.0.4 on 2024-07-31 02:17

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("assessment", "0004_alter_question_content"),
    ]

    operations = [
        migrations.AddField(
            model_name="question",
            name="input_text",
            field=models.CharField(default=7, max_length=200),
            preserve_default=False,
        ),
    ]
