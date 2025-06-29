
from tkinter import *
import tkinter.font as font
import math
kemal = Tk()
kemal.title("CALCULATOR kemal")
kemal.geometry("300x400")
kemal["bg"] = "white"
myfont = font.Font(size=20)
a = Entry(kemal,width=25,borderwidth=0)
a["font"] = myfont
a["bg"] = "white"
a.grid(row=0,column=0,columnspan=5,padx=25,pady=20)
def angka(nilai):
    sebelum = a.get()
    a.delete(0,END)
    a.insert(0,str(sebelum)+str(nilai))
def tambah():
    nomor_awal = a.get()
    global n_awal
    global mtk
    mtk = "penjumlahan"
    n_awal = int(nomor_awal)
    a.delete(0,END)
def kurang():
    nomor_awal = a.get()
    global n_awal
    global mtk
    mtk = "pengurangan"
    n_awal = int(nomor_awal)
    a.delete(0,END)
def bagi():
    nomor_awal = a.get()
    global n_awal
    global mtk
    mtk = "pembagian"
    n_awal = int(nomor_awal)
    a.delete(0,END)
def kali():
    nomor_awal = a.get()
    global n_awal
    global mtk
    mtk = "perkalian"
    n_awal = int(nomor_awal)
    a.delete(0,END)
def samadengan():
    nomor_akhir = a.get()
    a.delete(0,END)
    if mtk == "penjumlahan":
        a.insert(0,n_awal + int(nomor_akhir))
    elif mtk == "pengurangan":
        a.insert(0,n_awal - int(nomor_akhir))
    elif mtk == "pembagian":
        try:
            hitung = n_awal / int(nomor_akhir)
            a.insert(0,hitung)
        except ZeroDivisionError:
            a.insert(0,'0')
    elif mtk == "perkalian":
        a.insert(0,n_awal * int(nomor_akhir))
def hapus():
   a.delete(0,END)
btn1 = Button(kemal,text="1",padx="30",bg="gray",fg="white",pady="25",command=lambda:angka(1))
btn2 = Button(kemal,text="2",padx="30",bg="gray",fg="white",pady="25",command=lambda:angka(2))
btn3 = Button(kemal,text="3",padx="30",bg="gray",fg="white",pady="25",command=lambda:angka(3))
btn4 = Button(kemal,text="4",padx="30",bg="gray",fg="white",pady="25",command=lambda:angka(4))
btn5 = Button(kemal,text="5",padx="30",bg="gray",fg="white",pady="25",command=lambda:angka(5))
btn6 = Button(kemal,text="6",padx="30",bg="gray",fg="white",pady="25",command=lambda:angka(6))
btn7 = Button(kemal,text="7",padx="30",bg="gray",fg="white",pady="25",command=lambda:angka(7))
btn8 = Button(kemal,text="8",padx="30",bg="gray",fg="white",pady="25",command=lambda:angka(8))
btn9 = Button(kemal,text="9",padx="30",bg="gray",fg="white",pady="25",command=lambda:angka(9))
btn0 = Button(kemal,text="0",padx="30",bg="gray",fg="white",pady="25",command=lambda:angka(0))
tambah = Button(kemal,text="+",bg="white",fg="orange",padx="30",pady="25",command=tambah)
kurang = Button(kemal,text="-",bg="white",fg="orange",padx="30",pady="25",command=kurang)
bagi = Button(kemal,text="/",bg="white",fg="orange",padx="30",pady="25",command=bagi)
kali = Button(kemal,text="x",bg="white",fg="orange",padx="30",pady="25",command=kali)
samadengan = Button(kemal,text="=",bg="dark blue",fg="white",padx="30",pady="25",command=samadengan)
hapus = Button(kemal,text="C",bg="orange",fg="white",padx="30",pady="25",command=hapus)
btn1.grid(row=3,column=0,pady=2)
btn2.grid(row=3,column=1,pady=2)
btn3.grid(row=3,column=2,pady=2)
btn4.grid(row=2,column=0,pady=2)
btn5.grid(row=2,column=1,pady=2)
btn6.grid(row=2,column=2,pady=2)
btn7.grid(row=1,column=0,pady=2)
btn8.grid(row=1,column=1,pady=2)
btn9.grid(row=1,column=2,pady=2)
btn0.grid(row=4,column=1,pady=2)
tambah.grid(row=1,column=3,pady=2)
kurang.grid(row=2,column=3,pady=2)
bagi.grid(row=3,column=3,pady=2)
kali.grid(row=4,column=3,pady=2)
samadengan.grid(row=4,column=0,pady=2)
hapus.grid(row=4,column=2,pady=2)
kemal.mainloop()
#link youtube tutorial
#https://youtu.be/-isfRqTR-Qo?si=p9CCwVCeKBGvEmg-