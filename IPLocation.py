#Author Keyfin
#Waktu Coding 27/04/2021
import os,sys,time

#Warna
none = '\033[1;0m'
Black = '\033[0;30m'
Dark_Gray = '\033[1;30m'
Red = '\033[0;31m'
Light_Red = '\033[1;31m'
Green = '\033[0;32m'
Light_Green = '\033[1;32m'
Brown = '\033[0;33m'
Yellow = '\033[1;33m'
Blue = '\033[0;34m'
Light_Blue = '\033[1;34m'
Purple = '\033[0;35m'
Light_Purple = '\033[1;35m'
Cyan = '\033[0;36m'
Light_Cyan = '\033[1;36m'
Light_Gray = '\033[0;37m'
White = '\033[1;37m'
Zook = ''

logo = """
Version: 1.0.0
\033[0;36m                .';clodddolc;'.
            .,lxxxxxxxxxxxxxxxxxl,
          ,dxxxxxxxxxxxxxxxxxxxxxxxo,
        ,xxxxxxxxxxxxxxxxxxxxxxxxxxxxx.
       oxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxl
      xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
     xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxd
    ,xxxxxxxxx\033[1;33mO00000000OOk\033[0;36mx\033[1;33mOXXXXXXK0\033[0;36mkxxxxx.
    kxxxxxxxxk\033[1;33mXXXXXXXXXXX0\033[0;36mx\033[1;33mXXX0O0KXXX\033[0;36mxxxxxl
    kxxxxxxxxxxxx\033[1;33mKXX0\033[0;36mkkkkx\033[1;33mOXXK\033[0;36mxxxx\033[1;33mKXX0\033[0;36mxxxxx
    dxxxxxxxxxxxk\033[1;33mXXX\033[0;36mkxxxxx\033[1;33mKXXO\033[0;36mxxk\033[1;33m0XXK\033[0;36mkxxxxo
    ,xxxxxxxxxxx\033[1;33m0XXK\033[0;36mxxxxxk\033[1;33mXXXXXXXXX0\033[0;36mxxxxxx'
     xxxxxxxxxxx\033[1;33mXXX0\033[0;36mxxxxx\033[1;33m0XXK000O\033[0;36mkxxxxxxxx
     .xxxxxxxxxk\033[1;33mXXX\033[0;36mkxxxxx\033[1;33mXXX\033[0;36mkxxxxxxxxxxxx.
      cxxxxx\033[1;33mO0KKXXXKKKK\033[0;36mk\033[1;33mOXXK\033[0;36mxxxxxxxxxxxx;
       lxxxk\033[1;33mXXXXKKKKKK0\033[0;36mx\033[1;33mOXKO\033[0;36mxxxxxxxxxxxc
        cxxxxxxxxxxxxxxxxxxxxxxxxxxxxx:
         cxxxxxxxxxxxxxxxxxxxxxxxxxxx;
          ;xxxxxxxxxxxxxxxxxxxxxxxxx'
           .xxxxxxxxxxxxxxxxxxxxxxx.
             xxxxxxxxxxxxxxxxxxxxo
              :xxxxxxxxxxxxxxxxx,
               .xxxxxxxxxxxxxxx
                 lxxxxxxxxxxx;
                  .xxxxxxxxx
                    ;xxxxx'
                      oxc
                       "

                 \033[0;35mAuthon: \033[0;32momKeyx
        \033[0;36m[\033[0;34m=============================\033[0;36m]
	\033[0;36m|\033[0;35m>>>>\033[0;31m——[  \033[0;32mIP Location\033[0;31m  ]——\033[0;35m<<<<\033[0;36m|
	\033[0;36m[\033[0;34m=============================\033[0;36m]

"""
print(logo)

yy = 'y'
YY = 'Y'
nn = 'n'
NN = 'N'

import os
import sys
import time
import random
from datetime import datetime

try:
    import requests
except ModuleNotFoundError:
    print("Package module tidak terinstall")
    modul = str(input("Install package (Y/n)? "))
    if modul == YY:
        print("\033[0;32minstall requests\033[0;36m")
        os.system("pip install requests")
        #print("\033[0;32minstall random\033[0;m")
        #os.system("pip install ramdom")
        print("\033[1;33m[!] Kalau Error Liat Connection")
        print("\033[1;33m[!] Kalau Error Liat Connection")
        print("\033[1;33m[!] Kalau Error Liat Connection")
        print("\033[1;33m[!] Kalau Error Liat Connection")
        time.sleep(3)
        os.system("python zlcr.py")
        exit()
    elif modul == yy:
        print("\033[0;32minstall requests\033[0;36m")
        os.system("pip install requests")
        #print("\033[0;32minstall random\033[0;m")
        #os.system("pip install ramdom")
        print("\033[1;33m[!] Kalau Error Liat Connection")
        print("\033[1;33m[!] Kalau Error Liat Connection")
        print("\033[1;33m[!] Kalau Error Liat Connection")
        print("\033[1;33m[!] Kalau Error Liat Connection")
        time.sleep(3)
        os.system("python zlcr.py")
        exit()
    elif modul == NN:
        print("\033[1;91m[!] Tolong install requests untuk pakai tools ini")
        print("\033[1;91m[!] Exit")
        exit()
    elif modul == nn:
        print("\033[1;91m[!] Tolong install requests untuk pakai tools ini")
        print("\033[1;91m[!] Exit")
        exit()
    else:
        print("\033[1;91m[!] input tidak ada")
        print("\033[1;91m[!] Exit")
        exit()


clien = random.randint(10,50)

date_now = datetime.now().strftime('%d-%m-%Y  %H:%M')
print(f"\033[0;32mPengguna Tools: \033[1;33m{clien} \033[0;32morang")
sys.stdout.write("\033[0;32mWaktu: \033[1;33m" + date_now + "\n")
print("\033[0;32mIP Anda: \033[1;33m")
try:
    os.system('curl http://ident.me')
except:
    print("\033[1;91m[!] No connection")
    print("\033[1;91m[!] Exit")
print("\n")


try:
	query = input('\033[1;33mMasukan IP:\033[1;0m ')
	re = requests.get(f"http://ip-api.com/json/{query}?fields=status,message,continent,continentCode,country,countryCode,region,regionName,city,district,zip,lat,lon,timezone,offset,currency,isp,org,as,asname,reverse,mobile,proxy,hosting,query")
	if re.ok:
	    data = re.json()
	    print ("\033[0;32mIP                :", data["query"])
	    print ("Status            :", data["status"])
	    print ("Benua             :", data["continent"])
	    print ("Kode Benua        :", data["continentCode"])
	    print ("Negara            :", data["country"])
	    print ("Kode Negara       :", data["countryCode"])
	    print ("Nama Wilaya       :", data["regionName"])
	    print ("Wilaya            :", data["region"])
	    print ("Kota              :", data["city"])
	    print ("Distrik           :", data["district"])
	    print ("Zip               :", data["zip"])
	    print ("lat               :", data["lat"])
	    print ("Lon               :", data["lon"])
	    print ("Zona Waktu        :", data["timezone"])
	    print ("Offset            :", data["offset"])
	    print ("Mata Uang         :", data["currency"])
	    print ("As                :", data["as"])
	    print ("Asname            :", data["asname"])
	    print ("ISP               :", data["isp"])
	    print ("ORG               :", data["org"])
	    print ("Mobile            :", data["mobile"])
	    print ("Proxy             :", data["proxy"])
	    print ("Hosting           :", data["hosting"])
	    IPs = data["query"]
	    Sta = data["status"]
	    Ng = data["country"]
	    NW = data["regionName"]
	    Kt = data["city"]
	    lat = data["lat"]
	    lon = data["lon"]
	    ISP = data["isp"]
	    Mb = data["mobile"]
	    Px = data["proxy"]
	    Ht = data["hosting"]

except requests.exceptions.ConnectionError:
	print("\033[1;91m[!] No connection")
	print("\033[1;91m[!] Exit")
	time.sleep(1)
	exit()
except KeyError:
	print("\033[1;91m[!] IP Failed")
	print("\033[1;91m[!] Exit")
	time.sleep(1)
	exit()
except KeyboardInterrupt:
    print("\033[1;91m[!] Exit")
    time.sleep(1)
    exit()


savedat = "\n\nWaktu: {}\nIP: {}\nStatus: {}\nNegara: {}\nNama wilaya: {}\nKota: {}\nLat: {}\nLon: {}\nISP: {}\nMobile: {}\nProxy: {}\nHosting: {}".format(date_now, IPs, Sta, Ng, NW, Kt, lat, lon, ISP, Mb, Px, Ht)
file = open("history.txt", "a")
file.write(savedat)
file.close()