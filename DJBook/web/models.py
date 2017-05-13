# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.

from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
import django.utils.timezone as timezone

import sys
reload(sys)
sys.setdefaultencoding('utf-8')


class City(models.Model):
    id = models.AutoField(primary_key=True)
    city = models.CharField(max_length=15)


class Address(models.Model):
    id = models.AutoField(primary_key=True)
    address = models.CharField(max_length=45)
    addresscol = models.CharField(max_length=45, blank=True, null=True)
    city = models.ForeignKey('City', models.DO_NOTHING)



class User(User):
    age = models.IntegerField()
    active = models.IntegerField()
    create_time = models.DateField(default=timezone.now)
    address = models.ForeignKey(Address, models.DO_NOTHING)
    sex = models.CharField(max_length=10)
    phone = models.CharField(max_length=45, blank=True, null=True)


class Shop(models.Model):
    id = models.AutoField(primary_key=True)
    shop_name = models.CharField(max_length=45)


class JdGoods(models.Model):
    name = models.CharField(max_length=25)
    comment_num = models.IntegerField(blank=True, null=True)
    goods_id = models.CharField(max_length=25)
    link = models.CharField(max_length=50)
    commentversion = models.CharField(db_column='commentVersion', max_length=25, blank=True, null=True)  # Field name made lowercase.
    score1count = models.CharField(max_length=25, blank=True, null=True)
    score2count = models.CharField(max_length=25, blank=True, null=True)
    score3count = models.CharField(max_length=25, blank=True, null=True)
    score4count = models.CharField(max_length=25, blank=True, null=True)
    score5count = models.CharField(max_length=25, blank=True, null=True)
    price = models.CharField(max_length=25)
    shop = models.ForeignKey('Shop', models.DO_NOTHING)


class Label(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=45)
    jd_goods = models.ForeignKey(JdGoods, models.DO_NOTHING)
    user = models.ForeignKey('User', models.DO_NOTHING)


class JDBookItem(models.Model):
    id = models.AutoField(primary_key=True)
    book_id = models.IntegerField(blank=True, null=True)
    title = models.CharField(max_length=125)
    url = models.CharField(max_length=125)
    keywords = models.CharField(max_length=150)
    description = models.CharField(max_length=1000)
    img = models.CharField(max_length=125)
    channel = models.CharField(max_length=125)
    tag = models.CharField(max_length=125)
    sub_tag = models.CharField(max_length=125)
    value = models.CharField(max_length=125)
    price = models.CharField(max_length=125)


class Order(models.Model):
    id = models.AutoField(primary_key=True)
    number = models.IntegerField()
    total_price = models.CharField(max_length=25)
    jd_goods = models.ForeignKey(JDBookItem, models.DO_NOTHING)
    user = models.ForeignKey('User', models.DO_NOTHING)








