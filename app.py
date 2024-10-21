import tkinter as tk
from tkinter import messagebox
import pandas as pd


gelirler = []
giderler = []

# Gelir ekleme fonksiyonu
def gelir_ekle():
    try:
        gelir_turu = gelir_turu_entry.get()
        gelir_miktari = float(gelir_miktari_entry.get())
        gelirler.append({"Tür": gelir_turu, "Miktar": gelir_miktari})
        messagebox.showinfo("Başarılı", "Gelir başarıyla eklendi.")
    except ValueError:
        messagebox.showerror("Hata", "Geçerli bir miktar girin.")
    gelir_turu_entry.delete(0, tk.END)
    gelir_miktari_entry.delete(0, tk.END)

# Gider ekleme fonksiyonu
def gider_ekle():
    try:
        gider_turu = gider_turu_entry.get()
        gider_miktari = float(gider_miktari_entry.get())
        giderler.append({"Tür": gider_turu, "Miktar": gider_miktari})
        messagebox.showinfo("Başarılı", "Gider başarıyla eklendi.")
    except ValueError:
        messagebox.showerror("Hata", "Geçerli bir miktar girin.")
    gider_turu_entry.delete(0, tk.END)
    gider_miktari_entry.delete(0, tk.END)

# Hesaplama fonksiyonu
def hesapla():
    toplam_gelir = sum([gelir["Miktar"] for gelir in gelirler])
    toplam_gider = sum([gider["Miktar"] for gider in giderler])
    net_gelir = toplam_gelir - toplam_gider

    sonuc_label.config(text=f"Toplam Gelir: {toplam_gelir} TL\nToplam Gider: {toplam_gider} TL\nNet Gelir: {net_gelir} TL")

# Excel dosyasına kaydetme fonksiyonu
def excel_kaydet():
    try:
        if not gelirler and not giderler:
            messagebox.showerror("Hata", "Kaydedilecek veri yok.")
            return
        
        gelirler_df = pd.DataFrame(gelirler)
        giderler_df = pd.DataFrame(giderler)
        
        with pd.ExcelWriter("GelirGiderHesaplaması.xlsx", engine="openpyxl") as writer:
            if not gelirler_df.empty:
                gelirler_df.to_excel(writer, sheet_name="Gelirler", index=False)
            if not giderler_df.empty:
                giderler_df.to_excel(writer, sheet_name="Giderler", index=False)
        
        messagebox.showinfo("Başarılı", "Veriler Excel dosyasına başarıyla kaydedildi.")
    except Exception as e:
        messagebox.showerror("Hata", f"Excel kaydedilirken bir hata oluştu: {e}")

# Arayüz 
root = tk.Tk()
root.title("Gelir ve Gider Hesaplama Aracı")

# Gelir Ekleme 
tk.Label(root, text="Gelir Türü:").grid(row=0, column=0)
gelir_turu_entry = tk.Entry(root)
gelir_turu_entry.grid(row=0, column=1)

tk.Label(root, text="Gelir Miktarı:").grid(row=1, column=0)
gelir_miktari_entry = tk.Entry(root)
gelir_miktari_entry.grid(row=1, column=1)

tk.Button(root, text="Gelir Ekle", command=gelir_ekle).grid(row=2, column=1)

# Gider Ekleme 
tk.Label(root, text="Gider Türü:").grid(row=3, column=0)
gider_turu_entry = tk.Entry(root)
gider_turu_entry.grid(row=3, column=1)

tk.Label(root, text="Gider Miktarı:").grid(row=4, column=0)
gider_miktari_entry = tk.Entry(root)
gider_miktari_entry.grid(row=4, column=1)

tk.Button(root, text="Gider Ekle", command=gider_ekle).grid(row=5, column=1)

# Hesaplama 
tk.Button(root, text="Hesapla", command=hesapla).grid(row=6, column=1)
sonuc_label = tk.Label(root, text="")
sonuc_label.grid(row=7, column=1)

# Excel'e Kaydet
tk.Button(root, text="Excel'e Kaydet", command=excel_kaydet).grid(row=8, column=1)

root.mainloop()
