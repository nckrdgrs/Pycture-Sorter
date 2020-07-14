import os
import shutil
from datetime import datetime
import time

# only chnage original and destination locations
# only the original("ori") location needs to exist
ori = r'Y:\location\location'
# the destination location will be auto created by the script if it does not exist
dest = r'Y:\location\location'

if not os.path.exists(dest):
     os.makedirs(dest)


for root, subdirs, files in os.walk(ori):
     for file in files:
         path = os.path.join(root, file)
         #         print ('Path:    ', path)
#         print ('File:    ', file)
         epocTime = (os.path.getmtime(path))
         modTimeYR = time.strftime('%Y', time.localtime(epocTime))
         modTimeMN = time.strftime('%m', time.localtime(epocTime))

         if os.path.exists(dest + '\\' + modTimeYR + '\\' + modTimeMN + '\\' + 'Thumbs.db'):
                   os.remove(dest + '\\' + modTimeYR + '\\' + modTimeMN + '\\' + 'Thumbs.db')
#                   print ("Thumbs.db file removed.")

         if os.path.exists(dest + '\\' + modTimeYR + '\\' + modTimeMN + '\\' + file):
              try:
                  if not os.path.exists(dest + '\\' + 'Dupes'):
                       os.makedirs(dest + '\\' + 'Dupes')
                  dupes = (dest + '\\' + 'Dupes')
                  shutil.move(path, dupes + '\\' + file)
#                   print ("Moved to:", dupes + '\\' + file)
              except:
                   print("Dupe failure.", path)



         if not os.path.exists(dest + '\\' + modTimeYR + '\\' + modTimeMN):
              os.makedirs(dest + '\\' + modTimeYR + '\\' + modTimeMN)
#              print ("Made:    ", dest + '\\' + modTimeYR + '\\' + modTimeMN)
              shutil.move(path, dest + '\\' + modTimeYR + '\\' + modTimeMN)
#              print ("Moved to:", dest + '\\' + modTimeYR + '\\' + modTimeMN)

         if os.path.exists(dest + '\\' + modTimeYR + '\\' + modTimeMN):
              try:
                   shutil.move(path, dest + '\\' + modTimeYR + '\\' + modTimeMN)
#                   print ("Moved to:", dest + '\\' + modTimeYR + '\\' + modTimeMN)
              except:
                   print("Original failure.", path)

print("Finished")
