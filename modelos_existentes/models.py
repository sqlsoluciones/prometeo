from __future__ import unicode_literals

from django.db import models
from datetime import datetime
from django.utils import timezone
from django.utils.timezone import activate
from django.conf import settings
activate(settings.TIME_ZONE)

# Usuario
class Usuario_Web(models.Model):
    email_usrio = models.CharField(primary_key=True , max_length=80 , null= False)
    clve_accso = models.CharField(max_length=10 , null= False)
    nmbre_usrio = models.CharField(max_length=60, null=True)
    email_altrntvo = models.CharField(max_length=80, null=True)
    tlno_fjo = models.CharField(max_length=20, null=True)
    tlfno_mvil = models.CharField(max_length=20, null=True)
    cdgo_prfil = models.IntegerField(null=True)
    nit_tcro_ascdo = models.CharField(max_length=13)
    estdo_usrio = models.IntegerField(null=False, default= 0)
    fcha_crcion = models.DateField(default=datetime.now, null=True)
    actvo = models.IntegerField(null=False, default= 0)

    def __str__(self):
        return self.email_usrio

    class Meta:
        verbose_name_plural= u'Usuarios_Web'
        db_table = 'usrios_web'


class Usuario_Web_Vinculacion_Empresa(models.Model):
    email_usrio = models.ForeignKey(Usuario_Web, db_column='email_usrio' , null=False)
    id_emprsa = models.IntegerField(primary_key=True)
    fcha_crcion = models.DateTimeField( default=timezone.now)
    actvo = models.IntegerField(null=False, default=1)

    class Meta:
        verbose_name_plural= u'Usuarios_Web_Vinculacion_Empresas'
        db_table = 'usrios_web_vnclcnes_emprsas'

    def __str__(self):
        return '%s - %s'  %(self.email_usrio, self.id_emprsa)

class Empresa(models.Model):
    id_clnte = models.BigIntegerField()
    id_emprsa = models.BigIntegerField(primary_key=True)
    nmbre_rzon_scial = models.CharField(max_length=80)
    cdgo_pais = models.IntegerField(default=57)
    cdgo_dpto = models.IntegerField(null=True)
    cdgo_mncpio = models.IntegerField(null=True)
    cdgo_pstal = models.CharField(max_length=6, null=True)
    drccion = models.CharField(max_length=50)
    web_site = models.CharField(max_length=100 , null=True)
    lgtpo_emprsa = models.ImageField(upload_to='logosEmpresas/', null=True)
    fcha_crcion = models.DateField(default=datetime.now, null=True)
    actvo = models.IntegerField(default=1)


    def __str__(self):
        return self.nmbre_rzon_scial

    class Meta:
        verbose_name_plural=u'Empresas'
        db_table = 'emprsas'
        unique_together = (('id_clnte', 'id_emprsa'),)

