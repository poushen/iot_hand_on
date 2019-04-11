import os

def cat(f):
    with open(f) as file:
        str = file.read()
        print(str)

def rm(f):
    os.remove(f)
    
def cd(directory):
    os.chdir(directory)

def run(f):
    with open(f) as file:
        str = file.read()
        exec(str, globals())

def ls(prex=None):
    s = os.statvfs(os.getcwd())
    print("current directory: {}, available size: {}KB".format(os.getcwd(), s[0] * s[4] / 1024))
    print()
    for (name, type, inode, size) in sorted(os.ilistdir()):
        if prex == None or name.startswith(prex):
            if type == 0x8000:
                print(" - {:8d} \t {}".format(size, name))
            else:
                print(" D {:8d} \t {}".format(size, name))

def ip():
    import network
    wlan = network.WLAN(network.STA_IF)

    print('ip: {}'.format(wlan.ifconfig()[0]))
