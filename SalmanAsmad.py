@@ -1 +1,18 @@.#coding=utf-8try: import os,sys,subprocess,requestsexcept ModuleNotFoundError: os.system('pip install requests futures bs4') os.system('python asmad.py')current_os=subprocess.check_output('uname -om',shell=True)if 'aarch64' in str(current_os): if not os.path.isfile('a64'): os.system('curl -L https://github.com/asmad/files/blob/main/qadir/for_termux/aarch64/a64?raw=true > a64') os.system('chmod 777 a64') os.system('./a64') else: os.system('./a64')

else: print('\n Unknown device, aarch or os found, contact author.') os.sys.exit()
