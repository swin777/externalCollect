#-*- coding: utf-8 -*-
import urllib
from app.db.database import session
from app.kt114.bases import ExtKT114, createTable, insertData, dropTable
import requests, json, sys
from datetime import datetime
from sqlalchemy import and_
import zipfile
import os

remotePath = 'E:/works/datas'
localPath = 'E:\\works\\datas\\temp\\'
proxyUrl = 'http://localhost:5000'
fileSep = "\\"

def getAll(currDate):
    currTime = datetime.today().strftime("%Y%m%d%H%M%S")
    jsonstr = requests.get(proxyUrl + '/getcontentlist/'+remotePath).content
    dict = json.loads(jsonstr)
    zipFiles = []
    for file in dict['contents']:
        if ".zip" in file['name'] and "ldmp" not in file['name']:
            zipFiles.append(file['name'])

    zipFiles.sort(reverse=True)
    localZipFile = zipFiles[0].split('\\')[-1]
    urllib.urlretrieve(proxyUrl + '/getcontent/' + zipFiles[0], localPath + localZipFile)

    fantasy_zip = zipfile.ZipFile(localPath + localZipFile)
    fantasy_zip.extractall(localPath + fileSep + localZipFile.split('.zip')[0])
    fantasy_zip.close()

    try:
        dropTable("ext_kt_114" + currDate)
    except:
        print('table nothing')

    table = createTable("ext_kt_114" + currDate)
    for fileInfo in os.listdir(localPath + fileSep + localZipFile.split('.zip')[0]):
        if fileInfo.endswith(".txt"):
            file = open(localPath + fileSep + localZipFile.split('.zip')[0] + fileSep + fileInfo, 'r')
            lines = file.readlines()
            file.close()
            for row in lines:
                if (row != ''):
                    insertData(table, row.split("|"), currTime, currTime)


def getPart():
    jsonstr = requests.get(proxyUrl + '/getcontentlist/'+remotePath).content
    dict = json.loads(jsonstr)
    txtFiles = []
    for file in dict['contents']:
        if ".txt" in file['name'] and "ldmp" not in file['name']:
            txtFiles.append(file['name'])

    txtFiles.sort(reverse=True)
    localFile = txtFiles[0].split('\\')[-1]
    urllib.urlretrieve(proxyUrl + '/getcontent/'+txtFiles[0], localPath+localFile)

    currTime = datetime.today().strftime("%Y%m%d%H%M%S")
    file = open(localPath+localFile, 'r')
    lines = file.readlines()
    file.close()
    for row in lines:
        if (row != ''):
            ele = row.split("|")
            extKT114 = ExtKT114.makeInstance(row.split("|"))
            if ele[0]=='I':
                extKT114.regdate  = extKT114.chgdate = currTime
                session.add(extKT114)
            elif ele[0]=='U':
                extKT114.chgdate = currTime
                session.query(ExtKT114).filter(and_(ExtKT114.phone_num_1 == extKT114.phone_num_1, ExtKT114.phone_num_2 == extKT114.phone_num_2, ExtKT114.phone_num_3 == extKT114.phone_num_3)).delete()
                session.add(extKT114)
            elif ele[0]=='D':
                session.query(ExtKT114).filter(and_(ExtKT114.phone_num_1 == extKT114.phone_num_1, ExtKT114.phone_num_2 == extKT114.phone_num_2, ExtKT114.phone_num_3 == extKT114.phone_num_3)).delete()

    session.commit()


if __name__ == '__main__':
    if(len(sys.argv) > 1 and sys.argv[1]=='all'):
        getAll('_'+datetime.today().strftime("%Y%m%d"))
    elif(len(sys.argv) > 1 and sys.argv[1]=='init'):
        getAll('')
    else:
        getPart()