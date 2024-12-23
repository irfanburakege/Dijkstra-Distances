# Metin dosyasındaki sayıları okuyup şehir adlarını elimine etme ve virgüllerle ayırarak formatlama
def process_numbers_from_text(file_path, group_size):
    try:
        # Dosyadan verileri okuma (UTF-8 ile)
        with open(file_path, 'r', encoding='utf-8') as file:
            data = file.readlines()  # Satır satır okuyoruz
    except FileNotFoundError:
        # Dosya bulunamadığında özel bir hata fırlatıyoruz
        raise Exception(f"Error: The file '{file_path}' was not found.")
    except UnicodeDecodeError:
        # Dosya okunurken karakter sorunu oluşursa bir hata veriyoruz
        raise Exception(f"Error: Could not decode the file '{file_path}' with 'utf-8' encoding.")

    numbers = []  # Sayıları saklayacak liste

    # Her satırı işlemeye başlıyoruz
    for line in data:
        # Satırdaki şehir kodunu ve adını elemek için split yapıyoruz
        # İlk iki kısmı atlayıp sadece sayıları alıyoruz
        parts = line.split()[2:]  # İlk iki öğeyi (kod ve şehir adı) atla
        numbers.extend(map(int, parts))  # Sayıları listeye ekle

    # Sonucu tutacak liste
    result = []

    # Her group_size kadar bir yeni liste oluşturup result listesine ekleme
    for i in range(0, len(numbers), group_size):
        chunk = numbers[i:i+group_size]
        result.append(f'jaggedarray['+str(i)+'] = new int[] {{ {", ".join(map(str, chunk))} }},')

    # Sonucu ekrana yazdırma
    for line in result:
        print(line+";")

# Kullandığınız dosya yolunu ve grup boyutunu girin
file_path = 'KarayoluExcel.txt'  # Sayıların ve şehir adlarının bulunduğu dosya
group_size = 81  # Her grupta kaç sayı olacağını belirtiyor

process_numbers_from_text(file_path, group_size)
