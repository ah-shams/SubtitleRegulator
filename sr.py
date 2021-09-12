import os
from natsort import natsorted, ns

def filefinderandsorter(path,format):
    n=0
    srtlist=[]
    os.chdir(path)
    filelist=os.listdir(path)
    srtlist=list(filter(lambda s:s[-len(format):]==format,filelist))
    srtlist = natsorted(srtlist, key=lambda y: y.lower())
    return srtlist

def preview(list,format,name):
    preview=''
    for i in range(len(list)):
        preview=preview + list[i]+'   ------------------>    '+name+str(i+1)+format+'\n'
    return preview
def reg(list,path,name,format):
    for i in range(len(list)):
        old_d = os.path.join(path,list[i])
        new_d= os.path.join(path,name+str(i+1)+format)
        os.rename(old_d,new_d)


            


