import os
import subprocess

def userquery(text):
 s=text.split(" ")
 for i in s:
  if(i=="notepad"):
    os.system('C:\Windows\system32\notepad.exe')
  elif(i=="chrome"):
    subprocess.call('C:\Program Files (x86)\Google\Chrome\Application\chrome.exe')
  elif(i=="wmplayer"):
    subprocess.call('C:\Program Files (x86)\Windows Media Player\wmplayer.exe')
print("HEY USER WELCOME")
Print("How can i help you")
text=input()
userquery(text)
