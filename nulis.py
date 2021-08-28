# Jangan Di Recode Anjing
# Izin Dlu Kontol
# Emang ya kalau di kasih hati malah minta dada

import requests
import shutil
import os, time
import json
url="https://fdz-app.herokuapp.com/api/tulis?nama="
logo="""
╲╲╲╲╲┏━━━┓╱╱╱╱╱
╲┏━━━┻━━━┻━━━┓╱         Bot Nulis
╲┃╭━╮┏━━━┓╭━╮┃╱   =====================
╱┃┃╳┃┣◯-◯┫┃╳┃┃╲
╱┃╰━╯┣━━━┫╰━╯┃╲   Author : FERDIZ-AFK
╱┃┈▊▊▊▊┈▂▃▅▇┈┃╲   WhatsApp : wa.me//6287877173955 
╱┗━━━━━━━━━━━┛╲   Github : www.github.com/FERDIZ-afk


PASTIKAN DATA SELULER PERANGKAT ANDA MENYALA
MAKE SURE YOUR DEVICE CELLULAR DATA ON

PASTIKAN JIKA tidak terisi minimal anda 
menggunakan spasi agar tidak error
"""

def biasa():
    nama=input("masukan nama: ")
    print('')
    nomor=input("masukan nomor: ")
    print('')
    kelas=input("masukan kelas: ")
    print('')
    tulis=input("masukan tulisan: ")

    r = requests.get(url+nama+"&no="+nomor+"&kelas="+kelas+"&text="+tulis, stream = True)
    if r.status_code == 200:
        r.raw.decode_content = True
        with open('tulis.jpg','wb') as f:
            shutil.copyfileobj(r.raw, f)
            print('')
            print('tunggu sebentar bos')
            time.sleep(3)
            print('')
            print('Berhasil, nama file:','tulis.jpg')
    else:
        print('Terjadi Kesalahan')


if __name__=="__main__":
    os.system("clear")
    print(logo)
    print("1. Tulis")
    print("0. Kembali / enter")
    print('')
    pil=input("Metode berdasarkan nomor => ")
    if pil == "1":
        biasa()
    else:
        print(pil, "tidak ada")
