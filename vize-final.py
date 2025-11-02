import tkinter as tk 

# Uygulamanın Görünümünü Oluşturma
root = tk.Tk()
root.title("Hesap Makinesi") #Pencere başlığı
root.geometry("300x400")  #Pencere boyutu

#Veri Girişi İçin
vize_label = tk.Label(root, text="Vize Notu:")
vize_label.pack()
vize_entry = tk.Entry(root)
vize_entry.pack()

final_label = tk.Label(root, text="Final Notu:")
final_label.pack()
final_entry = tk.Entry(root)
final_entry.pack()

# Hesaplama Fonksiyonu

def hesapla():
    try:
        vize=float(vize_entry.get()) # kullanıcıdan alınan veriyi hesaplamak için;
        final=float(final_entry.get())
        ortalama = (vize * 0.4) + (final * 0.6)

        # --- 1. GEÇME/KALMA DURUMUNU BELİRLE ---
        # Öncelikli kural: Final notu 50'den düşükse kalır.
        if final < 50:
            sonuc_label.config(text=f"Ortalama: {ortalama:.2f}\nFinal notu 50'den düşük olduğu için Kaldınız!", fg="red")
            harf_label.config(text="Harf Notu: FF") 
        
        elif ortalama >= 50:
            sonuc_label.config(text=f"Ortalama: {ortalama:.2f}\nGeçtiniz!", fg="green")
           
            if ortalama >= 88: harf = "AA"
            elif ortalama >= 81: harf = "BA"
            elif ortalama >= 74: harf = "BB"
            elif ortalama >= 67: harf = "CB"
            elif ortalama >= 60: harf = "CC"
            elif ortalama >= 53: harf = "DC"
            else: harf = "DD" # 50-52 arası
            harf_label.config(text=f"Harf Notu: {harf}")
        else: # ortalama < 50
            sonuc_label.config(text=f"Ortalama: {ortalama:.2f}\nKaldınız!", fg="red")
            # Ortalamadan kalınca harf notları
            if ortalama >= 46: harf = "DD"
            elif ortalama >= 39: harf = "FD"
            else: harf = "FF"
            harf_label.config(text=f"Harf Notu: {harf}")

    except ValueError:
        # Hata durumunda da aynı etiketi güncelliyoruz.
        sonuc_label.config(text="Lütfen geçerli bir sayı girin.", fg="red")
        harf_label.config(text="") # Hata durumunda harf notunu temizle

# Hesapla Butonu
hesapla_button = tk.Button(root, text="Hesapla", command=hesapla) #Def fonksiyonundan alınan verileri burada hesaplamaka için kullanılan button
hesapla_button.pack()

# Sonuç etiketini fonksiyonun dışında, başta sadece bir kere oluşturuyoruz.
sonuc_label = tk.Label(root, text="", font=("Arial", 10), pady=10)
sonuc_label.pack()
harf_label = tk.Label(root, text="", font=("Arial", 10), pady=10)
harf_label.pack()





root.mainloop()

     
