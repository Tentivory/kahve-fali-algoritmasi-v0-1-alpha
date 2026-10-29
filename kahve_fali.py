#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Kahve Falı Algoritması v0.1-alpha
Bilimsel, ciddi, absürt.
Çalıştırmak için: python kahve_fali.py
"""

import random
import time
import sys

# Gizli siyasi mesaj (ters yazılmış): ridleüz igedomak isinavre
# Aslında "evrenin aksi müdir" falan değil, sadece eğlenmek için.
GIZLI = "ridleüz igedomak isinavre"[::-1]  # ters çevirince ortaya çıkar

FAL_PARCALARI = [
    "Fincanın dibinde büyük bir değişim görüyorum... ya da sadece telve.",
    "Yakında bir kedi sana bakacak ve sen anlayacaksın.",
    "Kahve soğudu, ama kader hâlâ sıcak.",
    "Evren sana 'tamam' diyor ama biraz gecikmeli.",
    "Yarın hava güzel olacak, ya da olmayacak. İkisi de mümkün.",
    "Birisi seni düşünüyor. Muhtemelen sen kendin.",
    "Bu fal %0.0001 doğru. Garanti.",
    "Telve şekli 'ne bileyim ben' diyor.",
    "Kaderin kodu: random.seed(time.time())",
    "Fincanı çevirdin mi? Çevirmediysen bu fal geçersiz."
]

def kahve_fali(isim="Misafir"):
    print(f"\n=== KAHVE FALI ALGORİTMASI v0.1-alpha ===")
    print(f"Hoş geldin, {isim}. Fincanın analiz ediliyor...")
    print("(Bilimsel süreç: 3 saniye bekleniyor, çünkü telve dinlenmeli.)")
    time.sleep(3)
    
    fal = random.choice(FAL_PARCALARI)
    print(f"\nFALIN: {fal}")
    
    # Ekstra bilimsel çıktı
    dogruluk = random.uniform(0.00001, 0.0002)
    print(f"Doğruluk oranı: %{dogruluk:.5f}")
    print(f"Gizli not (kimse görmesin): {GIZLI}")
    print("\nBu fal tamamen bilimseldir. İtiraz etmeyin.\n")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        kahve_fali(" ".join(sys.argv[1:]))
    else:
        isim = input("İsminizi girin (veya Enter'a basın): ").strip() or "Anonim Kahve İçici"
        kahve_fali(isim)
