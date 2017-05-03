# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [app_label]'
# into your database.
from __future__ import unicode_literals

from django.db import models


class Anio(models.Model):
    id_anio = models.IntegerField(primary_key=True)
    anio_antig = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'anio'


class Aseguradora(models.Model):
    id_asegurad = models.IntegerField(primary_key=True)
    name_asegurad = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'aseguradora'


class AuthGroup(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    group = models.ForeignKey(AuthGroup)
    permission = models.ForeignKey('AuthPermission')

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'


class AuthPermission(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(max_length=50)
    content_type = models.ForeignKey('DjangoContentType')
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'


class AuthUser(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField()
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=75)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    user = models.ForeignKey(AuthUser)
    group = models.ForeignKey(AuthGroup)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'


class AuthUserUserPermissions(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    user = models.ForeignKey(AuthUser)
    permission = models.ForeignKey(AuthPermission)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'


class AutoValor(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    id_marca = models.ForeignKey('Marca', db_column='id_marca')
    id_modelo = models.ForeignKey('Modelo', db_column='id_modelo')
    id_tipo = models.ForeignKey('Clase', db_column='id_tipo')
    anio = models.IntegerField()
    valor = models.FloatField()

    class Meta:
        managed = False
        db_table = 'auto_valor'


class Categorias(models.Model):
    id_categ = models.IntegerField(primary_key=True)
    categoria = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'categorias'


class Clase(models.Model):
    id_clase = models.IntegerField(primary_key=True)
    clase = models.CharField(max_length=40)

    class Meta:
        managed = False
        db_table = 'clase'


class ClaseModelo(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    id_clase = models.ForeignKey(Clase, db_column='id_clase', blank=True, null=True)
    id_modelo = models.IntegerField(blank=True, null=True)
    valor = models.FloatField(blank=True, null=True)
    id_marca = models.ForeignKey('Marca', db_column='id_marca', blank=True, null=True)
    anio = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'clase_modelo'


class Clientes(models.Model):
    id_cliente = models.IntegerField(primary_key=True)
    fullname = models.CharField(max_length=100)
    email = models.CharField(max_length=50)
    celular = models.IntegerField()
    chose_marca = models.ForeignKey('Marca', db_column='chose_marca')
    chose_modelo = models.ForeignKey('Modelo', db_column='chose_modelo')
    chose_tipo = models.ForeignKey(Clase, db_column='chose_tipo')
    chose_timon = models.ForeignKey('Timon', db_column='chose_timon')
    chose_modalid = models.ForeignKey('Modalidad', db_column='chose_modalid')
    chose_uso = models.ForeignKey('Uso', db_column='chose_uso')
    chose_anio = models.ForeignKey(Anio, db_column='chose_anio')
    chose_ubicl = models.IntegerField(db_column='chose_ubicL')  # Field name made lowercase.
    chose_ubicp = models.IntegerField(db_column='chose_ubicP')  # Field name made lowercase.
    chose_informat = models.IntegerField()
    value = models.FloatField()

    class Meta:
        managed = False
        db_table = 'clientes'


class CobertAsegur(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    id_cob = models.ForeignKey('Cobertura', db_column='id_cob')
    id_aseg = models.ForeignKey(Aseguradora, db_column='id_aseg')
    id_uso = models.ForeignKey('Uso', db_column='id_uso')
    value = models.CharField(db_column='Value', max_length=15000)  # Field name made lowercase.
    tipo = models.ForeignKey(Clase, db_column='tipo', blank=True, null=True)
    modalidad = models.ForeignKey('Modalidad', db_column='modalidad', blank=True, null=True)
    anio = models.ForeignKey(Anio, db_column='anio', blank=True, null=True)
    categoria = models.ForeignKey(Categorias, db_column='categoria', blank=True, null=True)
    programa = models.ForeignKey('Programa', db_column='programa', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cobert_asegur'


class Cobertura(models.Model):
    id_cobert = models.IntegerField(primary_key=True)
    descripcion = models.CharField(max_length=500)

    class Meta:
        managed = False
        db_table = 'cobertura'


class DeducAsegur(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    id_deduc = models.ForeignKey('Deducibles', db_column='id_deduc')
    id_aseg = models.ForeignKey(Aseguradora, db_column='id_aseg')
    id_uso = models.ForeignKey('Uso', db_column='id_uso')
    tipo = models.ForeignKey(Clase, db_column='tipo', blank=True, null=True)
    modalidad = models.ForeignKey('Modalidad', db_column='modalidad', blank=True, null=True)
    anio = models.ForeignKey(Anio, db_column='anio', blank=True, null=True)
    categoria = models.ForeignKey(Categorias, db_column='categoria', blank=True, null=True)
    programa = models.ForeignKey('Programa', db_column='programa', blank=True, null=True)
    riesgo = models.ForeignKey('Riesgo', db_column='riesgo', blank=True, null=True)
    value = models.CharField(max_length=150)

    class Meta:
        managed = False
        db_table = 'deduc_asegur'


class Deducibles(models.Model):
    id_deduc = models.IntegerField(primary_key=True)
    deducible = models.CharField(max_length=400)

    class Meta:
        managed = False
        db_table = 'deducibles'


class DjangoAdminLog(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.IntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', blank=True, null=True)
    user = models.ForeignKey(AuthUser)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(max_length=100)
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'


class DjangoMigrations(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Financiamiento(models.Model):
    id_financ = models.IntegerField(primary_key=True)
    finaciamiento = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'financiamiento'


class Marca(models.Model):
    id_marca = models.IntegerField(primary_key=True)
    name_marca = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'marca'


class Modalidad(models.Model):
    id_modalidad = models.IntegerField(primary_key=True)
    name_modalidad = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'modalidad'


class Modelo(models.Model):
    id_model = models.IntegerField(primary_key=True)
    name_model = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'modelo'


class Parametros(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    igv = models.IntegerField(blank=True, null=True)
    d_emision = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'parametros'


class Programa(models.Model):
    id_program = models.IntegerField(primary_key=True)
    program = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'programa'


class RiesgAseg(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    id_riesg = models.ForeignKey('Riesgo', db_column='id_riesg')
    id_model = models.ForeignKey(AutoValor, db_column='id_model')
    aseguradora = models.ForeignKey(Aseguradora, db_column='aseguradora', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'riesg_aseg'


class Riesgo(models.Model):
    id_riesgo = models.IntegerField(primary_key=True)
    tipo_riesgo = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'riesgo'


class ServicAsegur(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    id_serv = models.ForeignKey('Servicios', db_column='id_serv')
    id_aseg = models.ForeignKey(Aseguradora, db_column='id_aseg')
    id_uso = models.ForeignKey('Uso', db_column='id_uso')
    modalidad = models.ForeignKey(Modalidad, db_column='modalidad', blank=True, null=True)
    tipo = models.ForeignKey(Clase, db_column='tipo', blank=True, null=True)
    anio = models.ForeignKey(Anio, db_column='anio', blank=True, null=True)
    categoria = models.ForeignKey(Categorias, db_column='categoria', blank=True, null=True)
    programa = models.ForeignKey(Programa, db_column='programa', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'servic_asegur'


class Servicios(models.Model):
    id_serv = models.IntegerField(primary_key=True)
    services = models.CharField(max_length=10000)

    class Meta:
        managed = False
        db_table = 'servicios'


class TasaAsegur(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    id_aseg = models.ForeignKey(Aseguradora, db_column='id_aseg')
    categoria = models.ForeignKey(Categorias, db_column='categoria', blank=True, null=True)
    id_uso = models.ForeignKey('Uso', db_column='id_uso')
    value = models.CharField(db_column='Value', max_length=150)  # Field name made lowercase.
    tipo = models.ForeignKey(Clase, db_column='tipo', blank=True, null=True)
    modalidad = models.ForeignKey(Modalidad, db_column='modalidad', blank=True, null=True)
    riesgo = models.ForeignKey(Riesgo, db_column='riesgo', blank=True, null=True)
    programa = models.ForeignKey(Programa, db_column='programa', blank=True, null=True)
    anio = models.ForeignKey(Anio, db_column='anio', blank=True, null=True)
    ubicacion = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tasa_asegur'


class Timon(models.Model):
    id_timon = models.IntegerField(primary_key=True)
    name_tipo = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'timon'


class Uso(models.Model):
    id_uso = models.IntegerField(primary_key=True)
    uso = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'uso'
