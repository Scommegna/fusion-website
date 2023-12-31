# Generated by Django 4.2.6 on 2023-10-31 13:10

from django.db import migrations, models
import django.db.models.deletion
import stdimage.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cargo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateField(auto_now_add=True, verbose_name='Created')),
                ('modified', models.DateField(auto_now=True, verbose_name='Modified')),
                ('active', models.BooleanField(default=True, verbose_name='Active')),
                ('cargo', models.CharField(max_length=100, verbose_name='Cargo')),
            ],
            options={
                'verbose_name': 'Cargo',
                'verbose_name_plural': 'Cargos',
            },
        ),
        migrations.CreateModel(
            name='Servicos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateField(auto_now_add=True, verbose_name='Created')),
                ('modified', models.DateField(auto_now=True, verbose_name='Modified')),
                ('active', models.BooleanField(default=True, verbose_name='Active')),
                ('service', models.CharField(max_length=100, verbose_name='Service')),
                ('description', models.TextField(max_length=200, verbose_name='Description')),
                ('icon', models.CharField(choices=[('lni-cog', 'Engrenagem'), ('lni-stats-up', 'Grafico'), ('lni-users', 'Usuarios'), ('lni-layers', 'Design'), ('lni-mobile', 'Mobile'), ('lni-rocket', 'Foguete')], max_length=12, verbose_name='Icon')),
            ],
            options={
                'verbose_name': 'Service',
                'verbose_name_plural': 'Services',
            },
        ),
        migrations.CreateModel(
            name='Funcionario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateField(auto_now_add=True, verbose_name='Created')),
                ('modified', models.DateField(auto_now=True, verbose_name='Modified')),
                ('active', models.BooleanField(default=True, verbose_name='Active')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('bio', models.TextField(max_length=200, verbose_name='Bio')),
                ('image', stdimage.models.StdImageField(force_min_size=False, upload_to='equipe', variations={'thumb': {'crop': True, 'height': 480, 'width': 480}}, verbose_name='Image')),
                ('facebook', models.CharField(default='#', max_length=100, verbose_name='Facebook')),
                ('twitter', models.CharField(default='#', max_length=100, verbose_name='Twitter')),
                ('instagram', models.CharField(default='#', max_length=100, verbose_name='Instagram')),
                ('cargo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.cargo', verbose_name='Cargo')),
            ],
            options={
                'verbose_name': 'Funcionario',
                'verbose_name_plural': 'Funcionarios',
            },
        ),
    ]
