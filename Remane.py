import os 
import shutil
place="/storage/emulated/0/Nm"
dist=place[:len(place)-2]+"NM-final"
os.makedirs(dist)
def rename(name):
  dis1=dist+'/'+name
  os.makedirs(dis1)
  for file in os.listdir(place):
      # file=file[:len(file)-4]
      shutil.copy(place+"/"+file,dis1)
      os.rename(dis1+"/"+file,dis1+"/"+f"{file[:len(file)-4]}-{name}(CSBS).pdf")
  
  #shutil.copytree(place,place[:len(place)-2])

for names in ['Santhosh M K ','Ranjith P','Prakash S','Aman']:
  rename(names)