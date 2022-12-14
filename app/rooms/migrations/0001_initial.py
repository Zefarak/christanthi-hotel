# Generated by Django 3.2.7 on 2022-11-21 08:06

from django.db import migrations, models
import django.db.models.deletion
import rooms.models
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CharacteristicsCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField(default=True)),
                ('title', models.CharField(max_length=200, unique=True, verbose_name='ΤΙΤΛΟΣ')),
                ('title_eng', models.CharField(max_length=200, unique=True, verbose_name='ΤΙΤΛΟΣ ENG')),
            ],
            options={
                'verbose_name': 'ΚΑΤΗΓΟΡΙΑ',
                'verbose_name_plural': 'ΚΑΤΗΓΟΡΙΑ ΧΑΡΑΚΤΗΡΙΣΤΙΚΩΝ',
            },
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField(default=True, verbose_name='ΚΑΤΑΣΤΑΣΗ')),
                ('title', models.CharField(max_length=200, unique=True, verbose_name='ΤΙΤΛΟΣ')),
                ('description', tinymce.models.HTMLField(blank=True, verbose_name='ΠΕΡΙΓΡΑΦΗ')),
                ('room_size', models.IntegerField(blank=True, verbose_name='ΜΕΓΕΘΟΣ ΔΩΜΑΤΙΟΥ')),
                ('bed_size', models.CharField(choices=[('1', '1 ΔΙΠΛΟ ΚΡΕΒΑΤΙ'), ('2', 'ΜΟΝΟ ΚΡΕΒΑΤΙ'), ('3', '1 ΔΙΠΛΟ ΚΡΕΒΑΤΙ-ΚΑΝΑΠΕΣ ΚΡΕΒΑΤΙ')], default='1', max_length=1, verbose_name='ΠΕΡΙΓΡΑΦΗ ΚΡΕΒΑΤΙΩΝ')),
                ('maximum_people', models.IntegerField(default=1, verbose_name='ΜΕΓΙΣΤΗ ΧΩΡΗΤΙΚΟΤΗΤΑ')),
                ('maximum_little_people', models.IntegerField(default=0, verbose_name='ΠΑΙΔΙΑ')),
                ('title_eng', models.CharField(max_length=200, null=True, unique=True, verbose_name='ΤΙΤΛΟΣ ENG')),
                ('description_eng', tinymce.models.HTMLField(blank=True, verbose_name='ΠΕΡΙΓΡΑΦΗ ENG')),
                ('bed_size_eng', models.CharField(choices=[('1', '1 DOUBLE BED'), ('2', 'SINGLE BED'), ('3', '1 DOUBLE BED -SOFA BED')], default='1', max_length=1, verbose_name='ΠΕΡΙΓΡΑΦΗ ΚΡΕΒΑΤΙΩΝ ENG')),
                ('webatelier_link', models.URLField(blank=True)),
                ('slug', models.SlugField(allow_unicode=True, blank=True, max_length=240, null=True)),
            ],
            options={
                'verbose_name': 'ΔΩΜΑΤΙΟ',
                'verbose_name_plural': 'ΔΩΜΑΤΙΑ',
            },
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_primary', models.BooleanField(default=False, verbose_name='ΒΑΣΙΚΗ PHOTO')),
                ('image', models.ImageField(help_text='445*445', upload_to=rooms.models.upload_photo, verbose_name='PHOTO')),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='rooms.room')),
            ],
        ),
        migrations.CreateModel(
            name='CharTitle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, unique=True, verbose_name='ΤΙΤΛΟΣ')),
                ('title_eng', models.CharField(max_length=200, unique=True, verbose_name='ΤΙΤΛΟΣ')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='rooms.characteristicscategory', verbose_name='ΚΑΤΗΓΟΡΙΑ')),
            ],
            options={
                'verbose_name': 'ΧΑΡΑΚΤΗΡΙΣΤΙΚΟ',
                'verbose_name_plural': 'ΧΑΡΑΚΤΗΡΙΣΤΙΚΑ',
            },
        ),
        migrations.CreateModel(
            name='Characteristic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rooms', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='rooms.room', verbose_name='ΔΩΜΑΤΙΟ')),
                ('title', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rooms.chartitle', verbose_name='ΤΙΤΛΟΣ')),
            ],
            options={
                'verbose_name': 'ΧΑΡΑΚΤΗΡΙΣΤΙΚΟ',
                'verbose_name_plural': 'ΧΑΡΑΚΤΗΡΙΣΤΙΚΑ ΠΡΟΪΌΝΤΟΣ',
            },
        ),
    ]
