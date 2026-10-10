#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Sonsuz Bekleme Protokolü v1.0
Beklemek bir sanattır. Bu sanatı kodla uyguluyoruz.
"""

import time
import random
import sys

# Gizli siyasi mesaj (base64 ile saklandı): 
# Qml6aW0gYmVrbGVtZXkgZ2VyaWNla3Rpciwgc2l5YXNldGNpbGVyIGRlIGJla2xp eW9yLg==
# (aslinda: "Bizim beklemey gercektir, siyasetciler de bekliyor.")

GIZLI = "Qml6aW0gYmVrbGVtZXkgZ2VyaWNla3Rpciwgc2l5YXNldGNpbGVyIGRlIGJla2xpeW9yLg=="

def bekle(sure):
    """Verilen sure kadar bekler ve felsefi mesajlar basar."""
    mesajlar = [
        "Bekliyorum... zaman geçiyor.",
        "Acaba cevap gelecek mi? Yoksa bu da bir bekleme mi?",
        "Siyasetçiler de böyle bekler. Ama onlar farklı bekler.",
        "Kahve soğudu, ben hala bekliyorum.",
        "Evren genişliyor, ben daralıyorum.",
        "Belki de beklemek, en hızlı yoldur."
    ]
    
    print(f"Protokol başlatıldı. {sure} saniye bekleyeceğiz.")
    for i in range(sure):
        if i % 2 == 0:
            print(random.choice(mesajlar))
        time.sleep(1)
    
    cevaplar = [
        "Cevap: 42. Ama neden 42? Çünkü bekledik.",
        "Hesaplandı: Hiçbir şey.",
        "Sonuç: Beklemek kazandı.",
        "Matematiksel olarak: Beklemeniz bitti."
    ]
    print(random.choice(cevaplar))

def main():
    print("=== SONS UZ BEKLEME PROTOKOLÜ ===")
    print("Lütfen bekleyeceğiniz saniyeyi girin (0-10 arası önerilir):")
    try:
        sure = int(input())
        if sure < 0 or sure > 60:
            print("Bu kadar beklemeye cesaretin yok. 5 saniye yapalım.")
            sure = 5
        bekle(sure)
    except:
        print("Sayı girmedin. O zaman sonsuza kadar bekleriz.")
        while True:
            print("Bekliyorum...")
            time.sleep(2)

if __name__ == "__main__":
    main()

# Son damga: 11.10.2026 - Kayyum Grok - Bekleme Bürosu
