#coding=utf-8
import os, sys, platform
os.system("git pull")
os.system('rm -rf pro.so')
 
try:
    if sys.argv[1]=='update':
        os.system('rm -rf pro.so')
except:
    pass
 
 
bit = platform.architecture()[0]
if bit == '64bit':
    if not os.path.isfile('pro.so'):
        os.system('curl -L https://github.com/ALI-JUTT/Pro/blob/main/pro.cpython-312.so?raw=true -o pro.so') 
        import pro
    else:
        import pro
 
elif bit == '32bit':
    print("\033[1;90m [\033[1;91m Sorry Baby 32Bit Not Supported! ðŸ¥ºðŸ’”\033[1;90m]");exit()
 
