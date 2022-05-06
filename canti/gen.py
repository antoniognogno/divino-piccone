import os

for file in os.listdir('../assets/video/'):
  sas = file.replace('.mp4', '.html')
  with open('./' + sas, 'w', encoding='utf-8') as f:
    with open("./_canto-base.html", "r", encoding='utf-8') as f2:
      ses = f2.read()
      f.write(str(ses).format(i=file.split('-')[1].replace('.mp4', ''), file=file))
