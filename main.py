from com.dtmilano.android.viewclient import ViewClient
import cv2
import pytesseract
import subprocess
import os
import sys
import time
import clipboard
import csv
import numpy

print('■ - Checking files integrity...')
scrdir = ("screens")
csvdir = ("excel")
checkscr = os.path.isdir(scrdir)
checkcsv = os.path.isdir(csvdir)
if not checkscr:
    os.makedirs(scrdir)
    print('≡ - /screens folder created')
    if not checkcsv:
        os.makedirs(csvdir)
        print('≡ - /excel folder created')
elif not checkcsv:
    os.makedirs(csvdir)
    print('≡ - /excel folder created')
else:
    print('≡ - Integrity was fine')

print('■ - Checking adb devices...')
output_stream = os.popen('adb devices')
outp = output_stream.read()
outp = outp.split('\n')
outp.remove('List of devices attached')

while("" in outp):
    outp.remove("")

if len(outp) > 1:
    print(f"Your devices: {str(outp)}")
    print('X - Please make sure you only have 1 emulator opened.')
    sys.exit()

# Once we are sure there is only 1 emulator running, connect to it.
device, serialno = ViewClient.connectToDeviceOrExit()
print(f'≡ - Connected to adb device [{str(serialno)}]')

timestr = time.strftime("%Y%m%d-%H%M%S")

with open(os.getcwd()+'\excel\\'+timestr + '.csv', 'w', encoding="utf-8") as csvf:
    row = ['ID','Name','Alliance','Power','Total Killpts','T1 Killpts','T2 Killpts','T3 Killpts','T4 Killpts','T5 Killpts','Highest Power','Victory','Defeat','Dead','Scout Times','Gathered rss','Sent rss','Help times']
    wr = csv.DictWriter(csvf, fieldnames=row, lineterminator = '\n')
    wr.writeheader()

def top123(x, y, n): # whole process inside a function to do the top1-2-3 then loop over the rest.
    start_time = time.perf_counter()
    print(f'Reading profile {n}...')

    device.shell(f'input tap {str(x)} {str(y)}')
    time.sleep(0.7) #wait for GUI to load :)

    #no checks for top3 players (we assume their profiles are available)

    govgen = device.takeSnapshot(reconnect=True)
    govgen.save(os.getcwd()+'\screens\\'+str(n)+'gov.png')
    time.sleep(0.1)

    device.shell('input tap 800 340') #tap on name to copy on clipboard

    device.shell('input tap 1337 423') #tap on detailed kills
    time.sleep(0.5) #wait for GUI to load :)

    govkills = device.takeSnapshot(reconnect=True)
    govkills.save(os.getcwd()+'\screens\\'+str(n)+'govkills.png')
    time.sleep(0.1)

    device.shell('input tap 465 790') #open more info tab
    time.sleep(0.4) #wait for GUI to load :)

    govinfo = device.takeSnapshot(reconnect=True)
    govinfo.save(os.getcwd()+'\screens\\'+str(n)+'govinfo.png')
    time.sleep(0.1)

    name = clipboard.paste() #save clipboard to variable

    device.shell('input tap 1670 75') #close more info tab
    time.sleep(0.5) #wait for GUI to load :)

    device.shell('input tap 1619 140') #close governor profile
    time.sleep(0.5) #wait for GUI to load :)

    subprocess.Popen(['python', 'reader.py', str(n), name, timestr])
    #subprocess.Popen(['reader.exe', str(n), name, timestr])
    end_time = time.perf_counter()
    print(f'It took {end_time-start_time: 0.2f} second(s) to complete.')
    
def checkPlayer():
    check = device.takeSnapshot(reconnect=True) #Check if governor profile opened. If it didn't, go to next one.
    check = check.crop((1073, 401, 1181, 435))
    checkstr = pytesseract.image_to_string(check)
    checkstr = checkstr.replace('\n', ' ').strip()
    check.close()
    return checkstr
    
top123(260, 336, '1') #do top1
top123(262, 466, '2') #do top2
top123(260, 582, '3') #do top3

skippedCounter = 0

for x in range(4, 300):
    start_time = time.perf_counter()
    print(f'Reading profile {str(x)}...')

    device.shell('input tap 264 721') #tap on governor from ranking list 
    time.sleep(0.7) #wait for GUI to load :)

    checkstr = checkPlayer()

    if checkstr != 'Power':
        skippedCounter = skippedCounter + 1
        device.shell('input tap 264 846')
        time.sleep(0.7) #wait for GUI to load :)
        checkstr = checkPlayer()
    if checkstr != 'Power':
        skippedCounter = skippedCounter + 1
        device.shell('input tap 264 940')
        time.sleep(0.7) #wait for GUI to load :)

    govgen = device.takeSnapshot(reconnect=True)
    govgen.save(os.getcwd()+'\screens\\'+str(x)+'gov.png')
    time.sleep(0.1)

    device.shell('input tap 1337 423') #tap on detailed kills
    time.sleep(0.5) #wait for GUI to load :)

    device.shell('input tap 800 340') #tap on name to copy on clipboard

    govkills = device.takeSnapshot(reconnect=True)
    govkills.save(os.getcwd()+'\screens\\'+str(x)+'govkills.png')
    time.sleep(0.1)

    device.shell('input tap 465 790') #open more info tab
    time.sleep(0.4) #wait for GUI to load :)

    govinfo = device.takeSnapshot(reconnect=True)
    govinfo.save(os.getcwd()+'\screens\\'+str(x)+'govinfo.png')
    time.sleep(0.1)

    name = clipboard.paste() #save clipboard to variable

    device.shell('input tap 1670 75') #close more info tab
    time.sleep(0.5) #wait for GUI to load :)

    device.shell('input tap 1619 140') #close governor profile
    time.sleep(0.5) #wait for GUI to load :)

    subprocess.Popen(['python', 'reader.py', str(x), name, timestr])
    #subprocess.Popen(['reader.exe', str(x), name, timestr])
    end_time = time.perf_counter()
    print(f'It took {end_time-start_time: 0.2f} second(s) to complete.')

print(f'Scan finished. Skipped {str(skippedCounter)} profile/s')