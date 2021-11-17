from django.db import models
from django.db.models import Q
from django.conf import settings
from sqlalchemy import create_engine
import pandas as pd

class Meibo(models.Model):
    simei = models.CharField(max_length=50, verbose_name="氏名")
    simei_kana= models.CharField(max_length=50)
    email_addr = models.CharField(max_length=50)
    seibetu = models.CharField(max_length=10)
    tanjo_bi = models.DateField()
    blood_gata = models.CharField(max_length=5)
    chiiki = models.CharField(max_length=50)
    phone_bango = models.CharField(max_length=10)

    def __str__(self):
        return self.simei

    @classmethod
    def get_kensaku(cls, str):
        def kensaku(s):
            q = Q(simei__regex = s)
            q |= Q(simei_kana__regex = s)
            q |= Q(seibetu__regex = s)
            q |= Q(blood_gata__regex = s)
            q |= Q(chiiki__regex = s)
            return q

        q = Q() if str else Q(simei__regex = "^$")
        if str:
            for s in str.replace('\u3000',' ').split(' '):
                q &= kensaku(s)

        return q

    # CSVファイルを読み込んでモデルに挿入
    @classmethod
    def from_csv(cls, filename):
        fields = [f.name for f in cls._meta.fields] # モデルの列名を取得
        fields.remove('id') # id 列を削除
        cls.objects.all().delete()
        db_table = cls.objects.model._meta.db_table
        con = create_engine("sqlite:///" + settings.DATABASES['default']['NAME'])
        df = pd.read_csv(filename, header=None, names=fields, encoding='cp932', skiprows=1)
        df.tanjo_bi.replace('\/', r'-', regex=True, inplace=True)
        df.to_sql(db_table, con, if_exists='append', index=False)
