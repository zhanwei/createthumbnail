import os
import sys
import commands
sourced = "/home/zhanwei/work/zhanwei-share/cached/"
sourced =  os.path.dirname(os.getcwd())+"/"

commandpart1 = "ffmpegthumbnailer  -t 50% -i "
commandpart3=" -s 800x600 -o "
commandpart5=".png"
def getfilelist(sourcedir):

    filelist = os.listdir(sourcedir)
    print type(filelist)
    print dir(filelist)
    for item in filelist:
        print type(item)
        print dir(item)
        templist = item.split('.')
        if(len(templist) !=2):
            filelist.remove(item)
        elif(templist[1]!="ts"):
            filelist.remove(item)
        print item

    return filelist

def creatthumbnail(listsrc):
    for item in listsrc:
        fullcmd=commandpart1+sourced+item+commandpart3+item.split('.')[0]+commandpart5
        print fullcmd
        print commands.getstatusoutput(fullcmd)



print sourced
print "here we go"
fl = getfilelist(sourced)
print fl
creatthumbnail(fl)


