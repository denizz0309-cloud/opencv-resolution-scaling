# OpenCV CUDA ile Görüntü Çözünürlüğü Ölçeklendirme

Bu proje, OpenCV kullanarak görüntüleri farklı ölçeklerde yeniden boyutlandırmayı ve görüntüleme işlemini gerçekleştirmeyi amaçlamaktadır.

## Özellikler
- Görüntüleri OpenCV ile okuma.
- Görüntüleri farklı ölçeklerde yeniden boyutlandırma.
- Yeniden boyutlandırılan görüntüleri ayrı pencerelerde görüntüleme.
- CUDA destekli OpenCV ile GPU hızlandırmasını kullanmaya yönelik altyapı.

## Kullanılan Teknolojiler
- Python
- OpenCV
- NVIDIA CUDA

## Gereksinimler
- Python 3
- CUDA desteği etkinleştirilmiş OpenCV
- Uyumlu NVIDIA ekran kartı ve CUDA Toolkit

## Çalıştırma
1. Depoyu bilgisayarınıza indirin.
2. `ana.py` ve `dama tahtası.jpeg` dosyalarının aynı klasörde olduğundan emin olun.
3. Terminalde aşağıdaki komutu çalıştırın:

```bash
python ana.py
```

## Proje Durumu
Temel görüntü okuma, yeniden boyutlandırma ve görüntüleme işlemleri uygulanmıştır. CUDA hızlandırmasının çalışma ortamında ayrıca doğrulanması gerekmektedir.
