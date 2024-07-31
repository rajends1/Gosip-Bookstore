# Generated by Django 3.2.16 on 2022-12-20 01:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_alter_books_options'),
        ('checkout', '0002_auto_20221220_0057'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderSet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=0)),
                ('set_total', models.DecimalField(decimal_places=2, max_digits=8)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books.books')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='checkout.order')),
            ],
        ),
    ]
