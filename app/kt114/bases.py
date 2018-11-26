from sqlalchemy import Column, Text, Table
from app.db.database import base, meta, conn, engine

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
    regdate = Column(Text)
    chgdate = Column(Text)

    def __repr__(self):
        return "<ExtKT114(phone_num_1='%s', phone_num_2='%s', phone_num_3='%s', poi_nm='%s')>" % (self.phone_num_1, self.phone_num_2, self.phone_num_3, self.poi_nm)

    @staticmethod
    def makeInstance(ele):
        return ExtKT114(flag=ele[0], phone_num_1=ele[1], phone_num_2=ele[2], phone_num_3=ele[3], status=ele[4],
                        poi_nm=ele[5], branch_nm=ele[6], main_num_conf=ele[7], depart_info=ele[8], cate_cd=ele[9],
                        cate_nm=ele[10], eds_dong_cd=ele[11],
                        addr_jibeon=ele[12], addr_sub=ele[13], addr_sub_bld=ele[14], b_code=ele[15], b_name=ele[16],
                        h_code=ele[17], h_name=ele[18], mt_cd=ele[19], ma_sn=ele[20], sb_sn=ele[21], x=ele[22],
                        y=ele[23], workdate=ele[24])

def createTable(tableName):
    table = Table(tableName, meta,
                  Column('flag', Text),
                  Column('phone_num_1', Text, primary_key=True),
                  Column('phone_num_2', Text, primary_key=True),
                  Column('phone_num_3', Text, primary_key=True),
                  Column('status', Text),
                  Column('poi_nm', Text),
                  Column('branch_nm', Text),
                  Column('main_num_conf', Text),
                  Column('depart_info', Text),
                  Column('cate_cd', Text),
                  Column('cate_nm', Text),
                  Column('eds_dong_cd', Text),
                  Column('addr_jibeon', Text),
                  Column('addr_sub', Text),
                  Column('addr_sub_bld', Text),
                  Column('b_code', Text),
                  Column('b_name', Text),
                  Column('h_code', Text),
                  Column('h_name', Text),
                  Column('mt_cd', Text),
                  Column('ma_sn', Text),
                  Column('sb_sn', Text),
                  Column('x', Text),
                  Column('y', Text),
                  Column('workdate', Text),
                  Column('regdate', Text),
                  Column('chgdate', Text)
            )
    table.create(engine)
    return table

def dropTable(tableName):
    conn.execute("drop table " + tableName)

def insertData(table, ele, regdate, chgdate):
    ins = table.insert().values(
        flag=ele[0], phone_num_1=ele[1], phone_num_2=ele[2], phone_num_3=ele[3], status=ele[4],
        poi_nm=ele[5], branch_nm=ele[6], main_num_conf=ele[7], depart_info=ele[8], cate_cd=ele[9],
        cate_nm=ele[10], eds_dong_cd=ele[11],
        addr_jibeon=ele[12], addr_sub=ele[13], addr_sub_bld=ele[14], b_code=ele[15], b_name=ele[16],
        h_code=ele[17], h_name=ele[18], mt_cd=ele[19], ma_sn=ele[20], sb_sn=ele[21], x=ele[22],
        y=ele[23], workdate=ele[24], regdate=regdate, chgdate=chgdate
    )
    conn.execute(ins)