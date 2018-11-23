from app.db.database import base, session
from sqlalchemy import Column, Text
import requests, json, sys
from datetime import datetime

hostName = 'http://172.31.184.60:5000/http://220.92.84.245:80/api/'
apiCode = '?code=C012170830'
areas = ['01','02','03','04','05','06','07','08','09','10','11','14','15','16','17','18','19']

class ExtOpinet(base):
    __tablename__ = 'ext_opinet'
    __table_args__ = {'schema':'collect_poi'}
    uni_id = Column(Text, primary_key=True)
    poll_div_co = Column(Text)
    gpoll_div_co = Column(Text)
    os_nm = Column(Text)
    van_adr = Column(Text)
    new_adr = Column(Text)
    tel = Column(Text)
    gis_x_coor = Column(Text)
    gis_y_coor = Column(Text)
    maint_yn = Column(Text)
    cvs_yn = Column(Text)
    car_wash_yn = Column(Text)
    kpetro_yn = Column(Text)
    self_yn = Column(Text)
    clo_yn = Column(Text)
    sido_cd = Column(Text)
    sigun_cd = Column(Text)
    lpg_yn = Column(Text)
    mdfy_dt = Column(Text)
    reg_dt = Column(Text)
    edit_dt = Column(Text)
    use_yn = Column(Text)

    def __repr__(self):
        return "<ExtOpinet(uni_id='%s', os_nm='%s')>" % (self.uni_id, self.os_nm)

def makeExtOpinet(oil):
    return ExtOpinet(uni_id=oil['UNI_ID'], poll_div_co=oil['POLL_DIV_CO'], gpoll_div_co=oil['GPOLL_DIV_CO'], os_nm=oil['OS_NM'], van_adr=oil['VAN_ADR'],new_adr=oil['NEW_ADR'],
                  tel=oil['TEL'], gis_x_coor=oil['GIS_X_COOR'], gis_y_coor=oil['GIS_Y_COOR'], maint_yn=oil['MAINT_YN'],cvs_yn=oil['CVS_YN'], car_wash_yn=oil['CAR_WASH_YN'],
                  kpetro_yn=oil['KPETRO_YN'], self_yn=oil['SELF_YN'], sido_cd=oil['SIDO_CD'], sigun_cd=oil['SIGUN_CD'],lpg_yn=oil['LPG_YN'], mdfy_dt=oil['MDFY_DT'])

def add(oil, currTime):
    extOpinet = makeExtOpinet(oil)
    extOpinet.clo_yn = 'N'
    extOpinet.reg_dt = currTime
    extOpinet.edit_dt = currTime
    extOpinet.use_yn = 'Y'
    session.add(extOpinet)

def modify(oil, currTime, useYn):
    extOpinet = makeExtOpinet(oil)
    extOpinet.clo_yn = oil['CLO_YN']
    extOpinet.edit_dt = currTime
    extOpinet.use_yn = useYn
    #session.query(ExtOpinet).filter(ExtOpinet.uni_id == extOpinet.uni_id).update(jsonify(extOpinet))
    session.query(ExtOpinet).filter(ExtOpinet.uni_id == extOpinet.uni_id).delete()
    session.add(extOpinet)

def get_osList():
    currTime = datetime.today().strftime("%Y%m%d%H%M%S")
    session.query(ExtOpinet).delete()
    for area in areas:
        jsonstr = requests.get(hostName + 'osList.do' + apiCode + '&out=json&area=' + area).content
        dict = json.loads(jsonstr)
        for oil in dict['RESULT']['OIL']:
            add(oil, currTime)
    session.commit()

def get_osModList():
    currTime = datetime.today().strftime("%Y%m%d%H%M%S")
    print('get_osModList ext : ' + currTime)
    jsonstr = requests.get(hostName + 'osModList.do' + apiCode + '&out=json').content
    dict = json.loads(jsonstr, strict=False)
    for oil in dict['RESULT']['OIL']:
        row = session.query(ExtOpinet).filter(ExtOpinet.uni_id == oil['UNI_ID']).first()
        if (row):
            use_yn = 'N'
            if (row.clo_yn == 'N'):
                use_yn = 'Y'
            modify(oil, currTime, use_yn)
        else:
            add(oil, currTime)
    session.commit()

if __name__ == '__main__':
    if(len(sys.argv) > 1 and sys.argv[1]=='all'):
        get_osList()
    else:
        get_osModList()