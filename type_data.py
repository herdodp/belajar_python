# type data integer
angka1 = 10
print(type(angka1))

# type data float
angka2 = 10.5
print(type(angka2))

# type data string
angka3 = "10"
print(type(angka3))

#type data boolean
angka4 = True
angka5 = False
print(type(angka4))
print(type(angka5))

## type data khusus

#type data complex
angka6 = complex(10,5)
print(type(angka6))

# type data dari C 
from ctypes import c_double, c_int

angka7 = c_double(10.5)
print(type(angka7))

angka8 = c_int(10)
print(type(angka8))