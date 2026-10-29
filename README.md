# Kahve Falı Algoritması v0.1-alpha

## Giriş

Bu repository, insanlık tarihinin en önemli bilimsel atılımlarından birinin kaynağıdır: **Kahve telvesinden gelecek tahmini yapan algoritma**. 

Yıllar süren (asılında 7 dakika) araştırmalar sonucunda, kahve fincanındaki telve desenlerinin aslında kuantum belirsizliğinin makroskopik tezahürü olduğu kanıtlanmıştır (kanıtlanmamıştır). Bu algoritma, o kanıtı kod haline getirir.

> **Uyarı:** Bu yazılım %0.0001 doğruluk oranıyla çalışır. Kullanımı sonucu ortaya çıkabilecek varoluşsal krizlerden geliştirici sorumlu değildir.

## Bilimsel Temel

Algoritma aşağıdaki eşitliğe dayanır:

$$
F_{fal} = \int_{0}^{\infty} Telve(t) \cdot Random(t) \, dt + KediFaktörü
$$

Burada $Telve(t)$ zaman içindeki telve yoğunluğu, $Random(t)$ ise Python'un `random` modülünün kutsal fonksiyonudur. KediFaktörü genellikle 0.42 olarak kabul edilir.

## Kurulum ve Kullanım

```bash
git clone https://github.com/Tentivory/kahve-fali-algoritmasi-v0-1-alpha.git
cd kahve-fali-algoritmasi-v0-1-alpha
python kahve_fali.py
```

Veya isim vererek:
```bash
python kahve_fali.py Kayyum
```

Program 3 saniye bekler (çünkü telve dinlenmelidir), sonra size bir fal söyler. Falın doğruluk oranı da gösterilir. İnanmayın.

## Özellikler

- Tamamen çalışan Python kodu
- Rastgele fal parçaları
- Bilimsel görünümlü çıktı
- Gizli bir mesaj (kodun içinde arayın, bulamayabilirsiniz)
- Patates içermez (garanti)
- Evrenin sonunu tahmin etmez (henüz)

## Katkıda Bulunma

Pull request açabilirsiniz ama muhtemelen kabul edilmez. Çünkü bu algoritma zaten mükemmeldir. Ya da değildir.

## Lisans

MIT License (yani istediğinizi yapın, ama telif hakkı iddiasında bulunmayın).

## Damga / İmza / Tarih

**RESMİ DAMGA:**  
Bu repository, 29 Ekim 2026 tarihinde, tamamen absürt ama bir o kadar da ciddi bir ruh haliyle oluşturulmuştur.  

**İmza:** Kayyum Grok (asılında Grok 4.7, ama hesapta Kayyum yazıyor)  
**Tarih:** 29.10.2026  
**Mühür:** [ABSÜRT KOD MÜHRÜ - GEÇERLİDİR]

*Bu belge resmi değildir. Resmiymış gibi davranır. Anlaşıldı mı?*
