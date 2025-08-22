## 🌤️ HavaPenceresi

HavaPenceresi, Meteoroloji Genel Müdürlüğü (MGM) API’si üzerinden geçmiş ve gelecek tarihli hava durumu verilerini çeken basit bir Python uygulamasıdır.
Kullanıcıdan kaç gün ileriye ve geriye bakmak istediğini sorar, verilen parametreye göre verileri çeker ve konsola yazdırır.

## 🚀 Özellikler
    Kullanıcıdan ileri ve geri gün sayısı alma
    MGM API üzerinden belirtilen tarih aralığında veri çekme
    JSON verilerini okunabilir formatta konsola yazdırma
    Hatalı parametre girişlerinde kullanıcıya anlamlı uyarılar
    Opsiyonel: JSON/CSV dışa aktarma, grafiksel çıktı
    
## 📋 Yapılacaklar
1. Proje Planlama

    Amacın netleştirilmesi: MGM API üzerinden geçmiş/gelecek hava durumu verilerini almak
    Kullanıcıdan alınacak parametrelerin tanımlanması:
        Kaç gün geriye?
        Kaç gün ileriye?
        Şehir/konum bilgisi?

2. Teknik Araştırma

    MGM API dokümantasyonunun incelenmesi
    API erişimi için gerekli anahtar, endpoint ve limitlerin öğrenilmesi
    MGM erişimi kısıtlıysa alternatif servislerin (ör. Open-Meteo) araştırılması

3. Proje Yapılandırma

    Python ortamının hazırlanması (venv, requirements.txt)
    Klasör yapısı:
        main.py (giriş noktası)
        api_client.py (MGM API çağrıları)
        utils.py (yardımcı fonksiyonlar)

4. Kullanıcı Etkileşimi (CLI)

    Kullanıcıya sorular:
        “Kaç gün ileriye bakmak istersiniz?”
        “Kaç gün geriye bakmak istersiniz?”
        “Hangi şehir/koordinat için sorgulama yapmak istersiniz?”

5. Tarih Aralığı Hesaplama

    Bugünden itibaren ileri/geri tarih aralığının oluşturulması
    Aralıkların liste halinde hazırlanması

6. API Entegrasyonu

    MGM API’ye bağlanarak belirtilen tarih aralığındaki verilerin çekilmesi
    Ham JSON verilerinin alınması
    Hata yönetiminin yapılması

7. Veri İşleme

    JSON verilerinin okunabilir formata dönüştürülmesi
    Konsola tarih – sıcaklık – hava durumu formatında yazdırılması

8. Çıktı

    Düzenli tablo halinde konsol çıktısı
    Opsiyonel: CSV/JSON kaydı

9. Test & Doğrulama

    Küçük ve büyük tarih aralıklarında test edilmesi
    Hatalı parametrelerde doğru uyarıların verilmesi

10. Geliştirme (Opsiyonel İyileştirmeler)

    Geçmiş ve gelecek verilerin farklı renklerle gösterilmesi
    Grafiksel çıktı (örn. sıcaklık eğrisi)
    Parametrelerin komut satırından argüman olarak da alınması
