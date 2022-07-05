import ftplib
import os
from datetime import datetime, timedelta
from datetime import datetime
from datetime import timezone


d = (datetime.utcnow()+timedelta(days=0)).strftime("%d")
m = datetime.utcnow().strftime("%m") 	
y = datetime.utcnow().strftime("%Y")
h = (datetime.utcnow()+timedelta(hours=-1)).strftime("%H")
path = '/himawari_vol/himawari4/HIMAWARI-8/DATA/image/Indonesia/'+y+'/'+m+'/'+d+'/'
tt00 = '00'
tt01 = '10'
tt02 = '20'
tt03 = '30'
tt04 = '40'
tt05 = '50'

ftp = ftplib.FTP("202.90.199.64","kspdc","kspdc!@#")
ftp.cwd(path)
dataloc=os.getcwd()+'\\data\\'


H00='H08_ET_Indonesia_'+y+''+m+''+d+''+h+''+tt00+'.png'
proses=ftp.retrbinary("RETR " + H00 ,open('D:/xampp/htdocs/prakicuindo/image/H08_ET_Indonesia_'+y+''+m+''+d+''+h+''+tt00+'.png', 'wb').write)
H01='H08_ET_Indonesia_'+y+''+m+''+d+''+h+''+tt01+'.png'
proses=ftp.retrbinary("RETR " + H01 ,open('D:/xampp/htdocs/prakicuindo/image/H08_ET_Indonesia_'+y+''+m+''+d+''+h+''+tt01+'.png', 'wb').write)
H02='H08_ET_Indonesia_'+y+''+m+''+d+''+h+''+tt02+'.png'
proses=ftp.retrbinary("RETR " + H02 ,open('D:/xampp/htdocs/prakicuindo/image/H08_ET_Indonesia_'+y+''+m+''+d+''+h+''+tt02+'.png', 'wb').write)
H03='H08_ET_Indonesia_'+y+''+m+''+d+''+h+''+tt03+'.png'
proses=ftp.retrbinary("RETR " + H03 ,open('D:/xampp/htdocs/prakicuindo/image/H08_ET_Indonesia_'+y+''+m+''+d+''+h+''+tt03+'.png', 'wb').write)
H04='H08_ET_Indonesia_'+y+''+m+''+d+''+h+''+tt04+'.png'
proses=ftp.retrbinary("RETR " + H04 ,open('D:/xampp/htdocs/prakicuindo/image/H08_ET_Indonesia_'+y+''+m+''+d+''+h+''+tt04+'.png', 'wb').write)
H05='H08_ET_Indonesia_'+y+''+m+''+d+''+h+''+tt05+'.png'
proses=ftp.retrbinary("RETR " + H05 ,open('D:/xampp/htdocs/prakicuindo/image/H08_ET_Indonesia_'+y+''+m+''+d+''+h+''+tt05+'.png', 'wb').write)

