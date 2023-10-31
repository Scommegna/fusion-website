import uuid

from django.db import models

from stdimage.models import StdImageField

def get_file_path(_instance, filename):
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'
    
    return filename

class Base(models.Model):
    created = models.DateField('Created', auto_now_add=True)
    modified = models.DateField('Modified', auto_now=True)
    active = models.BooleanField('Active', default=True)
    
    class Meta:
        abstract = True
        
class Servicos(Base):
    ICONS_CHOICES = (
        ('lni-cog', 'Engrenagem'),
        ('lni-stats-up', 'Grafico'),
        ('lni-users', 'Usuarios'),
        ('lni-layers', 'Design'),
        ('lni-mobile', 'Mobile'),
        ('lni-rocket', 'Foguete'),
    )
    service = models.CharField('Service', max_length=100)
    description = models.TextField('Description', max_length=200)
    icon = models.CharField('Icon', max_length=12, choices=ICONS_CHOICES)
    
    class Meta:
        verbose_name = 'Service'
        verbose_name_plural = 'Services'
        
    def __str__(self):
        return self.service
    
    
class Cargo(Base):
    cargo = models.CharField('Cargo', max_length=100)
    
    class Meta:
        verbose_name = 'Cargo'
        verbose_name_plural = 'Cargos'
        
    def __str__(self):
        return self.cargo
    
class Funcionario(Base):
    name = models.CharField('Name', max_length=100)
    cargo = models.ForeignKey('core.Cargo', verbose_name='Cargo', on_delete=models.CASCADE)
    bio = models.TextField('Bio', max_length=200)
    image = StdImageField('Image', upload_to=get_file_path, variations={'thumb': {'width': 480, 'height': 480, 'crop': True}})
    facebook = models.CharField('Facebook', max_length=100, default='#')
    twitter = models.CharField('Twitter', max_length=100, default='#')
    instagram = models.CharField('Instagram', max_length=100, default='#')

    class Meta:
        verbose_name = 'Funcionario'
        verbose_name_plural = 'Funcionarios'
        
    def __str__(self):
        return self.name