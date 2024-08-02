from django.db import models
from django.utils import timezone

# Create your models here.


class Comunicados(models.Model):
    titulo = models.CharField(max_length=40)

class Persona(models.Model):
    username = models.IntegerField()
    vista = models.CharField(max_length=30)

class Student(models.Model):
    dni = models.CharField(max_length=30)
    nroCarnet = models.CharField(max_length=30)
    username = models.IntegerField()

class Responsible(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    dni = models.CharField(max_length=30)
    telefono = models.CharField(max_length=30)

class ResponsibleOf:
    fk_id_student = models.IntegerField()
    fk_id_responsible = models.IntegerField()
    created_at = models.DateField(auto_now_add=True)
    deleted_at = models.DateField()

class Preceptor(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    dni = models.CharField(max_length=30)

class Profesor(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)

class Materia(models.Model):
    nombre = models.CharField(max_length=30)
    horario = models.DateTimeField() 
    fk_id_profesor = models.IntegerField()

class Curso(models.Model):
    anio = models.CharField(max_length=30)
    division = models.CharField(max_length=30)
    fk_id_prece = models.IntegerField()

class CursoMateria(models.Model):
    fk_id_materia = models.IntegerField()
    fk_id_curso = models.IntegerField()

class CicloLectivo(models.Model):
    ciclo = models.CharField(max_length=50)
    fk_id_curso =  models.IntegerField()
    fk_id_student = models.IntegerField()