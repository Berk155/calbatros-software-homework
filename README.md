# CALBATROS YAZILIM DEPARTMANI İLK ÖDEVİ

## 👋 Arkadaşlar Hepinize Selam!

Yazılım departmanımızın ilk ödevi ile birlikteyiz. Ödevin içeriği kısaca görüntü işleme ile alakalı, detaylı bilgi metnimizin ileri kısımlarında yer alıyor olacak.

Baştan söyleyebilirim ki ödevimiz zor bir ödev. Sizin yerinize kendimi koyduğumda muhtemelen ben de kaygılı hissederdim ödevi okuduğumda. Lakin kormanıza gerek yok çünkü evvelki tecrübelerime dayanarak söyleyebilirim ki haftasonu boyunca kafa patlatırsanız ve aşağı koyduğumuz kaynakları detaylıca incelerseniz altından kalkamayacağınız türden bir görevlendirme değil.

### 🚫 Önemli Not: Yapay Zeka Kullanımı

Sizden isteğim ödevi yaparken **ChatGPT veya türevi yapay zeka modelleri kullanmamanız**. Zaten kullanmanız durumunda ben bunu tespit edebilecek tecrübe, bilgi ve araçlara sahibim, o yüzden gereksiz yere beni keklemeye çalışmayın lütfen. Yanlış anlaşılmasın araştırma yaparken kullanabilirsiniz hatta size hız ve zaman kazandırır sadece kodu yapay zekaya yazdırmayın. Mesela bir hata alırsanız ya da bir şeyi anlamazsanız yapay zeka modelleri kullanabilirsiniz.

Bu görevlendirmeyi verirken ilk görevlendirmenizdeki kursları izlediğinizi varsayıyorum. Tam sonuç alamasanız bile ben yazdığınız kodları inceleyeceğim. Sonuca ulaşmak önemli ama süreçte gösterdiğiniz **hırsınızı ve çabanızı** da göz ardı etmeyeceğimizden emin olabilirsiniz.

Şimdi ödev ile alakalı detaylı ve değerli bilgilere aşağıda değinceğim.

---

## 💻 Ödev Detayları

Ödevimiz:

1.  **Video İşleme:** `images/` dizinindeki videoyu **YoloV4** (bilgisayarınız çok güçlü değilse **YoloV4-tiny** modeli de olabilir) görüntü işleme yapay zeka modeli ile işlemeniz.
2.  **Sınırlayıcı Çerçeve (Bounding Box) Çizme:** Yapay zekanın size döndürdüğü koordinatları kullanarak nesnenin etrafına bir çerçeve (`bounding box`) çizmeniz.
3.  **Gösterge Yapma:** Bu işlemi tanımladıktan sonra size `examples/` dizininde bıraktığım örnek çıktıdaki pencerenin sol altındaki okun bir benzerini yapıp sürekli algılanmış nesneyi göstermeniz olacak.

Ben kodu kendim yazdım ve toplamda **80-90 satır** bir `.py` dosyası oldu. Kulağa geldiği kadar komplike bir proje değil.

---

## 📥 Gerekli Dosyalar ve Kaynaklar

### Yolo Model Dosyaları

* **YoloV4 Modelini indirmek için (.weights/.cfg/.names):
1. https://github.com/AlexeyAB/darknet/releases/download/yolov4/yolov4.weights
2. https://raw.githubusercontent.com/AlexeyAB/darknet/master/cfg/yolov4.cfg
3. https://raw.githubusercontent.com/AlexeyAB/darknet/master/data/coco.names

* **YoloV4-Tiny Modelini indirmek için (.weights/.cfg/.names):
1. https://github.com/AlexeyAB/darknet/releases/download/darknet_yolo_v4_pre/yolov4-tiny.weights  
2 https://raw.githubusercontent.com/AlexeyAB/darknet/master/cfg/yolov4-tiny.cfg
3. https://raw.githubusercontent.com/AlexeyAB/darknet/master/data/coco.names

### Yardımcı Olabilecek Kaynaklar

* `https://docs.ultralytics.com/tr/guides/`
* `https://docs.opencv.org/4.x/d6/d00/tutorial_py_root.html`
* `https://matplotlib.org/stable/index.html`
* `https://numpy.org/doc/`

### Projede Kullanabileceğiniz Python Kütüphaneleri

```python
matplotlib
opencv (cv2)
numpy / scipy
math
