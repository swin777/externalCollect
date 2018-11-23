#-*- coding: utf-8 -*-
import urllib
from app.db.database import base, session
from sqlalchemy import Column, Text
import requests, json, sys

#urllib.urlretrieve('https://tile.gis.kt.com/20180406/base.default/11/3264/3062.png', 'D:\\test.png')

class ExtKT114(base):
    __tablename__ = 'ext_kt_114'
    #__table_args__ = {'schema': 'collect_poi'}
    flag = Column(Text)
    phone_num_1 = Column(Text, primary_key=True)
    phone_num_2 = Column(Text, primary_key=True)
    phone_num_3 = Column(Text, primary_key=True)
    status = Column(Text)
    poi_nm = Column(Text)
    branch_nm = Column(Text)
    main_num_conf = Column(Text)
    depart_info = Column(Text)
    cate_cd = Column(Text)
    cate_nm = Column(Text)
    eds_dong_cd = Column(Text)
    addr_jibeon = Column(Text)
    addr_sub = Column(Text)
    addr_sub_bld = Column(Text)
    b_code = Column(Text)
    b_name = Column(Text)
    h_code = Column(Text)
    h_name = Column(Text)
    mt_cd = Column(Text)
    ma_sn = Column(Text)
    sb_sn = Column(Text)
    x = Column(Text)
    y = Column(Text)
    workdate = Column(Text)

    def __repr__(self):
        return "<ExtKT114(phone_num_1='%s', phone_num_2='%s', phone_num_3='%s', poi_nm='%s')>" % (self.phone_num_1, self.phone_num_2, self.phone_num_3, self.poi_nm)

def makeExtKT114(ele):
    return ExtKT114(flag=ele[0], phone_num_1=ele[1], phone_num_2=ele[2], phone_num_3=ele[3], status=ele[4],poi_nm=ele[5], branch_nm=ele[6], main_num_conf=ele[7], depart_info=ele[8], cate_cd=ele[9], cate_nm=ele[10], eds_dong_cd=ele[11],
                     addr_jibeon=ele[12], addr_sub=ele[13], addr_sub_bld=ele[14], b_code=ele[15], b_name=ele[16], h_code=ele[17], h_name=ele[18], mt_cd=ele[19], ma_sn=ele[20], sb_sn=ele[21], x=ele[22], y=ele[23], workdate=ele[24])

def makeExtKT114_Arr(str):
    rows = str.split("\n")
    for row in rows:
        if(row!=''):
            extKT114 = makeExtKT114(row.split("|"))
            session.add(extKT114)
    session.commit()

def getAll():
    print("getAll")

def getPart():
    teststr = 'U|032|876|0703|0|(주)알이엠||3||369012|기계부속품제조|12020100|인천-미추홀-도화-818-8|||2817710400|인천광역시-미추홀구-도화동|2817760000|인천광역시-미추홀구-도화1동|01|818|8|282012.8|542684.7|20181115 \n' \
              + 'D|055|299|4209|0|창원보건소건강증진센터||2|팩스|963312|보건소|75033100|경남-창원-의창-팔용-121-1|||4812112900|경상남도-창원시의창구-팔용동|4812152000|경상남도-창원시의창구-팔룡동|01|121|1|456004.3|295534.4|20171022 \n' \
              + 'I|070|4123|0304|0|제주하우스||3||803005|부동산컨설팅|86020400|제주-서귀포-동홍-965-2|||5013010500|제주특별자치도-서귀포시-동홍동|5013057000|제주특별자치도-서귀포시-동홍동|01|965|2|266843.0|75855.0|20181118 \n'
    makeExtKT114_Arr(teststr)

if __name__ == '__main__':
    if(len(sys.argv) > 1 and sys.argv[1]=='all'):
        getAll()
    else:
        getPart()