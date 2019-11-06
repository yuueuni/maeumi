# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.contrib.auth.models import User


class Child(models.Model):
    chi_num = models.IntegerField(primary_key=True)
    chi_name = models.CharField(max_length=30)
    chi_gen = models.CharField(max_length=10)
    chi_birth = models.CharField(max_length=30)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        managed = False
        db_table = 'child'


class House(models.Model):
    hou_num = models.IntegerField(primary_key=True)
    hou_img = models.ImageField()
    hou_lan = models.TextField()

    class Meta:
        managed = False
        db_table = 'house'


class Person(models.Model):
    per_num = models.IntegerField(primary_key=True)
    per_img = models.ImageField()
    per_lan = models.TextField()

    class Meta:
        managed = False
        db_table = 'person'


class Record(models.Model):
    record_num = models.IntegerField(primary_key=True)
    record_con = models.TextField(blank=True, null=True)
    record_time = models.DateTimeField()
    chi_num = models.ForeignKey(Child, models.DO_NOTHING, db_column='chi_num')
    tree_num = models.ForeignKey('Tree', models.DO_NOTHING, db_column='tree_num')
    hou_num = models.ForeignKey(House, models.DO_NOTHING, db_column='hou_num')
    per_num = models.ForeignKey(Person, models.DO_NOTHING, db_column='per_num')

    class Meta:
        managed = False
        db_table = 'record'


class Tree(models.Model):
    tree_num = models.IntegerField(primary_key=True)
    tree_img = models.ImageField()
    tree_lan = models.TextField()

    class Meta:
        managed = False
        db_table = 'tree'

