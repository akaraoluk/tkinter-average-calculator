
import tkinter as tk
from functools import partial


def ort_hesapla(islem_sonucu, s1, s2):
    vize = float((s1.get()))
    final =float((s2.get()))
    sonuc = float(((vize*40) + (final*60))/100)
    islem_sonucu.config(text="ORTALAMA : %f" % sonuc)
    return sonuc


ortalama = tk.Tk()
ortalama.geometry('400x200+100+200')
ortalama.title('ORTALAMA HESAPLAMA')

sayi1 = tk.StringVar()
sayi2 = tk.StringVar()

labelTitle = tk.Label(ortalama, text="NOTLAR").grid(row=0, column=2)
labelvize = tk.Label(ortalama, text="VİZE NOTU").grid(row=1, column=0)
labelfinal = tk.Label(ortalama, text="FİNAL NOTU").grid(row=2, column=0)
labelOrtalama = tk.Label(ortalama)
labelOrtalama.grid(row=7, column=2)

vize1 = tk.Entry(ortalama, textvariable=sayi1).grid(row=1, column=2)
final1 = tk.Entry(ortalama, textvariable=sayi2).grid(row=2, column=2)
Ort_getir = partial(ort_hesapla, labelOrtalama, sayi1, sayi2)
butonOrt = tk.Button(ortalama, text="HESAPLA", command=Ort_getir).grid(row=3, column=0)
ortalama.mainloop()
