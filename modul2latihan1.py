# -*- coding: utf-8 -*-
"""
@Materi: Operasi Aritmatika pada Python
@Judul: Praktikum 2 Materi
@Hari/Tanggal: Senin, 20210927
@NIM: 065002100021
@author: Aldis Tamara Putri Iskandar
"""

a = int(input('Masukan nilai a: '))
b = int(input('Masukan nilai b: '))

count1 = a + b
print('Jumlah nilai a dan b adalah ', count1)

count2 = a - b
print('Selisih nilai a dan b adalah', count2)

count3 = a * b
print('Perkalian nilai a dan b adalah', count3)

count4 = a % b
print('Sisa pembagian nilai a dan b adalah', count4)

count5 = a / b
print('Pembagian nilai a dan b adalah', count5)

from math import log10
print('Logaritma basis 10 dari', a, 'adalah', log10(a))

count7 = a ** b
print('Hasil nilai a pangkat b adalah', count7)
