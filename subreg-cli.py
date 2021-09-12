import os
import sr

path=''
while (True) :
    print("Please specify a directory (type \"here\" to select the directory you are in)")
    a1 = input()
    if a1 == 'here' : 
        path=os.getcwd()
        break
    else :
        err=True
        try:
            os.chdir(a1)
        except:
            err=False
    if(err):
        path = a1
        break 
name = input("Please enter the name of the series : \n")
season = input("Please enter  season number of the series \n")
filename = name+'S'+season+'E'
format = '.'+input('Please enter the file format(ex : mkv,srt) : \n')
filelist = sr.filefinderandsorter(path,format)
print(sr.preview(filelist,format,filename))
sure = input("are you sure (y)?")
if(sure != 'y' and sure != 'Y'):
    exit()
else : 
    try: 
        sr.reg(filelist,path,filename,format)
    except:
        print('Unable to rename files')



