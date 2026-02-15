dosya_adi = "uygulama1.txt"

try:
    with open(dosya_adi, "r", encoding="utf-8") as dosya:
        icerik = dosya.read()
        print("Dosya başarıyla okundu.")
except FileNotFoundError:
    print(f"{dosya_adi} dosyası bulunamadı.")
    exit()


noktalama = ".,;:!?\"'()[]{}-–—_/\\«»“”‘’…"
#a=string.punctuation  #string modülünü kullanarak noktalama işaretlerini alabiliriz

temiz_metin = icerik
for karakter in noktalama:
    temiz_metin = temiz_metin.replace(karakter, "")


temiz_metin = temiz_metin.lower()


kelimeler = temiz_metin.split()


kelime_sayilari = {}

for kelime in kelimeler:
    if kelime == "":
        continue  #boş kelimeleri atla
    if kelime in kelime_sayilari:
        kelime_sayilari[kelime] += 1
    else:
        kelime_sayilari[kelime] = 1


print("\nKelimelerin geçtiği sayılar (dictionary):\n")
print(kelime_sayilari)

print("\nSıralı hâli (en çoktan en aza):\n")
for kelime, adet in sorted(kelime_sayilari.items(), key=lambda x: x[1], reverse=True):
    print(f"{kelime} : {adet}")
    
print("\nEn çok tekrar eden ilk 3 kelime:\n")

sirali_liste = sorted(
    kelime_sayilari.items(),      # (kelime, adet) çiftleri
    key=lambda x: x[1],           # adete göre sırala
    reverse=True                  # büyükten küçüğe
)

ilk_uc = sirali_liste[:3]         # ilk 3 eleman

for kelime, adet in ilk_uc:
    print(f"{kelime} : {adet} kez")


print("\nUzunluğu 5'ten büyük olan kelimeler arasından en çok tekrar eden kelime:\n")


uzun_kelime_sayilari = {}

for kelime, adet in kelime_sayilari.items():
    if len(kelime) > 5:
        uzun_kelime_sayilari[kelime] = adet

if not uzun_kelime_sayilari:
    print("Uzunluğu 5'ten büyük olan hiç kelime yok.")
else:
    
    en_cok_kelime, en_cok_adet = max(
        uzun_kelime_sayilari.items(),
        key=lambda x: x[1]
    )
    print(f"Kelime: '{en_cok_kelime}'  -  Tekrar sayısı: {en_cok_adet}")
   

print("\nSadece harflerden oluşan kelimeler arasından en çok tekrar eden kelime:\n")

harf_kelimeleri = {}

for kelime, adet in kelime_sayilari.items():
   
    if kelime.isalpha():
        harf_kelimeleri[kelime] = adet

if not harf_kelimeleri:
    print("Sadece harflerden oluşan hiç kelime yok.")
else:
    en_cok_harf_kelime, en_cok_harf_adet = max(
        harf_kelimeleri.items(),
        key=lambda x: x[1]
    )
    print(f"Kelime: '{en_cok_harf_kelime}'  -  Tekrar sayısı: {en_cok_harf_adet}")