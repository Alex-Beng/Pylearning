import os
import time

def click(site):
    time = '50'
    cmd = 'adb shell input swipe '
    x = str(site[0])+' '
    y= str(site[1])+' '

    cmd += x+y+x+y+time
    os.system(cmd)

def main():
    plusSite = (988,1863)
    callSite = (158,1331)
    lineSite = (482,1575)
    endSite = (539,1767)
    
    while (1):
        click(plusSite)
        time.sleep(0.5)
        click(callSite)
        time.sleep(0.5)
        click(lineSite)
        time.sleep(5)
        click(endSite)

        
if __name__ == '__main__':
    main()

