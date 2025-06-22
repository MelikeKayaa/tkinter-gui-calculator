## arayüz kullanarak yapılan hesap makinesi

# tkinter modülü ve hata mesajları için messagebox içe aktarılır.
import tkinter as tk
from tkinter import messagebox

# Toplama işlemi fonksiyonu
def topla():
    try:
        sayi1 = float(entry1.get()) # Kullanıcıdan alınan sayı ondalıklı sayıya dönüştürülür.
        sayi2 = float(entry2.get())
        sonuc = sayi1 + sayi2 # Toplama işlemi yapılır.
        label_sonuc.config(text=f"Sonuç: {sonuc:.3f}") # Sonuç değeri güncellenir. Virgülden sonraki 3 basamak gösterilir sadece
    except ValueError:
        messagebox.showerror("Hata", "Lütfen geçerli sayılar girin!") # Eğer kullanıcı sayı yerine başka bir şey (harf) girerse hata mesajı yazdırılır.

# Çıkartma işlemi fonksiyonu
def cikar():
    try:
        sayi1 = float(entry1.get())
        sayi2 = float(entry2.get())
        sonuc = sayi1 - sayi2
        label_sonuc.config(text=f'Sonuç: {sonuc:.3f}')
    except ValueError:
        messagebox.showerror('Hata', 'Lütfen geçerli bir sayı girin !')

# Çarpma işlemi fonksiyonu
def carp():
    try:
        sayi1 = float(entry1.get())
        sayi2 = float(entry2.get())
        sonuc = sayi1 * sayi2
        label_sonuc.config(text=f'Sonuç: {sonuc:.3f}')
    except ValueError:
        messagebox.showerror('Hata ', 'Lütfen geçerli bir sayı girin !')

# Bölme işlemi fonksiyonu
def bol():
    try:
        sayi1 = float(entry1.get())
        sayi2 = float(entry2.get())
        sonuc = sayi1 / sayi2
        label_sonuc.config(text=f'Sonuç: {sonuc:.3f}')
    except ZeroDivisionError:
        messagebox.showerror('Hata', 'Sıfıra bölme hatası !') # Kullanıcı sayi2 değerine 0 verirse hata mesajı yazdırılır.
    except ValueError:
        messagebox.showerror('Hata', 'Lütfen geçerli bir sayı girin !')

# Temizle fonksiyonu
def temizle():
    entry1.delete(0,tk.END) # İlk kutuyu temizler.
    entry2.delete(0,tk.END) # İkinci kutuyu temizler.
    label_sonuc.config(text='Sonuç: ') # Sonucu sıfırlar.

# Ana pencere oluşturulur.
pencere = tk.Tk()
pencere.title("Hesap Makinesi") # pencere başlığı
pencere.geometry("400x400") # pencere boyutu

# İlk sayının etiketi
label1 = tk.Label(pencere, text=' İlk Sayı')
label1.pack()

# İlk sayının giriş kutusu
entry1 = tk.Entry(pencere)
entry1.pack(pady=15)

# İkinci sayının etiketi
label2 =tk.Label(pencere,text='İkinci Sayı')
label2.pack()

# İkinci sayının giriş kutusu
entry2 = tk.Entry(pencere)
entry2.pack(pady=15)

# İşlem butonlarını yan yana koymek için bir Frame oluşturulur.
frame_butonlar = tk.Frame(pencere)
frame_butonlar.pack(pady=10)

# İşlem butonları oluşturulur ve frame içinde yan yana yerleştirilir.

# Topla butonu
buton_topla = tk.Button(frame_butonlar, text="Toplama", command=topla,background='#D8BFD8',fg='black',font=('Arial',9,'bold'))
buton_topla.grid(row=0, column=0, padx=5)

# Çıkart butonu
buton_cikar = tk.Button(frame_butonlar,text='Çıkartma', command=cikar,background='Light Steel Blue',fg='black',font=('Arial',9,'bold'))
buton_cikar.grid(row=0, column=1,padx=5)

# Çarp butonu
buton_carp = tk.Button(frame_butonlar,text='Çarpma', command=carp,background='Powder Blue',fg='black',font=('Arial',9,'bold'))
buton_carp.grid(row=0,column=2,padx=5)

# Böl butonu
buton_bol= tk.Button(frame_butonlar,text='Bölme',command=bol,background='#B2F2BB',fg='black',font=('Arial',9,'bold'))
buton_bol.grid(row=0, column=3,padx=5)

# Temizle butonu (frame içinde değil çünkü alt satırda daha iyi gözüküyor.)
buton_temizle = tk.Button(text='Temizle',command=temizle,background='#FFF8DC',fg='black',font=('Arial',9,'bold'))
buton_temizle.pack(pady=10)

# Sonuç etiketi
label_sonuc = tk.Label(pencere, text="Sonuç:",background = '#f0f0f0',font=('Arial',12,'bold'))
label_sonuc.pack(pady=15)

# Arayüzün sürekli çalışması için mainloop kullanılır.
pencere.mainloop()
