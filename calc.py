angka1 = int(input('masukan angka pertama: '))
angka2 = int(input('masukan angka kedua: '))
operation = str(input('pilih: tambah, kurang, kali, bagi: '))

if operation == 'tambah' or '+':
    hasil = angka1 + angka2
    print(f"{angka1} + {angka2} = {hasil}")
elif operation == 'kurang' or '-':
    hasil = angka1 - angka2
    print(f"{angka1} - {angka2} = {hasil}")
elif operation == 'kali' or 'x':
    hasil = angka1 * angka2
    print(f"{angka1} x {angka2} = {hasil}")
elif operation == 'bagi' or '/':
    hasil = angka1 / angka2
    print(f"{angka1} / {angka2} = {hasil}")
else:
    print('gk jelas loe capek ah gwe..')