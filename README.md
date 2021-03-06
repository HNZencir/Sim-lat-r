# Yerçekimi Simülatörü
## Nasıl kullanılır?
Python kodunu çalıştırın. Terminal ekranında simülasyonunuz hakkında birkaç bilgi girmeniz gerekmektedir.
* Top sayısı: Buraya yazdığınız sayı kadar top oluşacaktır.
* Sol duvarın X eksenindeki konumu: Simülatör, ekrana çıkacak olan topların sekeceği bir kutu çizer. Ekranın tam ortası (0,0) noktasıdır. X ekseninde sola doğru giderken X sayısı küçülür. Sağa doğru giderken ise X artar. Denemek için bu sayıyı -200 girmenizi öneririz.
* Sağ duvarın X eksenindeki konumu: Denemek için bu sayıyı 200 girmenizi öneririz.
* Duvarların Y koordinatı: Ekranda yukarıya doğru gittikçe Y artar, aşağıya doğru gittikçe Y azalır. Bu değer çizilecek olan kutunun en üst kısmıdır. Denemek için bu sayıyı 200 öneririm.
* Duvarların uzunluğu: Bu değer kutunun yüksekliğidir. Bu değeri 400 girmenizi öneririz.
* Duvarların yansıttığı enerji: Yere attığınız top sekerken hep aynı yüksekliğe ulaşmaz. Yüksekliği gittikçe azalır çünkü yer (cisim her nereye çarpıyorsa) topun enerjisinin bir kısmını emer. Buraya gireceğiniz değer duvarın emdiği enerjiden ne kadar kaldığıdır. Bu değeri 1 den küçük girmeniz en doğrusu olacaktır. Bu değeri 0.9 veya 0.8 girmenizi öneririz.

Tüm bu bilgileri girdikten sonra simülasyonunuz çalışacaktır.
