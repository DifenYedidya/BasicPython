x = "hello world"
# comment
print(x)

# fibonaci ke 10k
x = [0] * 10005  # inisialisasi array 0 sebanyak 10005; x[0]=0
x[1] = 1  # x[1]=1

for j in range(2, 10001):
    x[j] = x[j - 1] + x[j - 2]  # Fibonacci
print(x[10000])

# list
x = [5, 10, 15, 20, 25, 30, 35, 40]
print(x[5])
print(x[-1])
print(x[3:5])
print(x[:5])
print(x[-3:])
print(x[1:7:2])

# replace data
x = [1, 2, 3]
x[2] = 4
print(x)

# adding data
x.append(5)
print(x)

# delete data
spam = ['cat', 'bat', 'rat', 'elephant']
del spam[2]
print(spam)

# set
a = {1, 2, 2, 3, 3, 3}
print(a)

# tuple adl jenis dari list yang tidak dapat diubah elemennya
t = (5, 'program', 1 + 3j)
print(t[1])
print(t[0:3])
# t[0]=10

# set adalah kumpulan item bersifat unik dan tanpa urutan (unordered collection)
a = {1, 2, 2, 3, 3, 3}
print(a)
# Karena set bersifat unordered, maka kita tidak bisa mengambil sebagian data / elemen datanya menggunakan proses slicing
# a = {1,2,3}
# print(a[1])

a = 5
print('The value of a is', a)

# Untuk menampilkan text (string), bisa menggunakan mekanisme string format.
print('hello {}'.format('kakak'))

# atau mirip seperti c/c++
name = "John"
age = 15
print("%s is %d years old." % (name, age))

# menambahkan objek selain string (otomatis dikonversi):
mylist = [1, 2, 3]
print("A list: %s" % mylist)

a, b = 10, 12  # angka 10 dan 12 itu hexadecimal di ascii
print('a: %x and b: %X' % (a, b))

'''
%s - String
%d - Integers
%f - Bilangan Pecahan
%.<digit>f - Bilangan pecahan dengan sejumlah digit angka dibelakang koma.
%x/%X - Bilangan bulat dalam representasi Hexa (huruf kecil/huruf besar)
'''

"""
name = input('Who are you? : ')
age = input('how old are you ? :')
print(name)

# cast inputan yg tadinya string jd type int
int(age)
'''
kalau float ya
float(age)
'''
print(age)
# input

"""
# cek type data
# Ketika kita memberikan nilai 6 pada variabel x
x = 6
print(type(x))
# Kemudian Berikan string “hello” pada variabel x di baris selanjutnya
x = 'hello'
print(type(x))

# fill a 0 number
x = 1
str(x).zfill(5)
print(x)

# transform to upper or lower case
p = 'Hello world!'
p = p.upper()
print(p)
p = p.lower()
print(p)

"""
usually used to validate
    islower() dan isupper() ngembaliin nilai boolean true or false    
    isalpha() mengembalikan True jika string berisi hanya huruf dan tidak kosong.
    isalnum() mengembalikan True jika string berisi hanya huruf atau angka, dan tidak kosong.
    isdecimal() mengembalikan True jika string berisi hanya angka/numerik dan tidak kosong.
    isspace() mengembalikan True jika string berisi hanya spasi, tab, newline, atau whitespaces lainnya dan tidak kosong.
    istitle() mengembalikan True jika string berisi kata yang diawali huruf kapital dan dilanjutkan dengan huruf kecil seterusnya.
"""
'''
example :
    while True:
        print('Enter your age:')
        age = input()
        if age.isdecimal():
            break
        print('Please enter a number for your age.')
    while True:
        print('Select a new password (letters and numbers only):')
        password = input()
        if password.isalnum():
            break
        print('Passwords can only have letters and numbers.')
'''

"""
# startswith() and endswith()
'Hello world!'.startswith('Hello')
'Hello world!'.endswith('world!')

# join() and split()
'ABC'.join(['My', 'name', 'is', 'Simon'])
# output : 'cats, rats, bats'
', '.join(['cats', 'rats', 'bats'])
# output : 'MyABCnameABCisABCSimon'

'MyABCnameABCisABCSimon'.split('ABC')
# output : ['My', 'name', 'is', 'Simon']
"""

a = '''Dear Alice,
How have you been? I am fine.
There is a container in the fridge
that is labeled "Milk Experiment".
Please do not drink it.
Sincerely,
Bob'''
print(a)
print(a.split('\n'))

# Teks rata kanan/kiri/tengah dengan rjust(), ljust(), dan center()
print('Hello'.rjust(10))
print('Hello World'.rjust(20))
print('Hello'.center(20, '='))
print('Hello'.ljust(20, '-'))

# Hapus Whitespace dengan strip(), rstrip(), dan lstrip()
spam = '    Hello World     '
print(spam.strip())
print(spam.lstrip())
print(spam.rstrip())
spam = 'SpamSpamBaconSpamEggsSpamSpam'
print(spam.strip('ampS'))  # urutammya berantakan jg gpp

# Mengganti string/substring dengan replace()
string = "geeks for geeks geeks geeks geeks"
print(string.replace("geeks", "Geeks"))

# Operasi pada urutan (sequences: List, Set, String)
# len() utk itung banyak karakter

l = [1, 2, 3, 3, 4, 4, 4, 4, 5, 6]
s = set(l)
x = "Hello, World"

print(l)
print(len(l))

print(s)
print(len(s))

print(x)
print(len(x))

"""
# penggabungan atau replikasi
[1, 2, 3] + ['A', 'B', 'C']
['X', 'Y', 'Z'] * 3
spam = [1, 2, 3]
spam = spam + ['A', 'B', 'C']
print(spam)
"""

"""
# Fungsi range() memberikan deret bilangan dengan pola tertentu. Untuk melakukan perulangan (misalnya for) dalam mengakses elemen list, Anda dapat menggunakan fungsi range()
for i in range(9):
    print(i)
print('Hello'.center(20, '='))
for i in range(3, 9):
    print(i)

# Range dengan 3 parameter n,p,q: membuat deret bilangan yang dimulai dari n, hingga sebelum p (bilangan p tidak ikut), dengan setiap elemennya memiliki selisih q.
[_ for _ in range(1, 9, 2)]  # list comprehension
"""

"""
# in dan not in. Fungsi ini akan mengembalikan nilai boolean True atau False.
'howdy' in ['hello', 'hi', 'howdy', 'heyas']
spam = ['hello', 'hi', 'howdy', 'heyas']
'cat' in spam
'howdy' not in spam
'cat' not in spam
"""

# Memberikan nilai (assignment) untuk lebih dari 1 variabel sekaligus
"""
cat = ['fat', 'orange', 'loud'] # From List
size, color, disposition = cat
cat = ('fat', 'orange', 'loud')  # From Tuple
size, color, disposition = c
"""
a, b = 'Alice', 'Bob'
a, b = b, a
print(a)
print(b)

# sort
x = [2, 5, 3.14, 1, -7]
x.sort()
print(x)

y = ['ants', 'cats', 'dogs', 'badgers', 'elephants']
y.sort()
print(y)

y.sort(reverse=True)
print(y)

# di sort berdasarkan ascii
m = ['Alice', 'ants', 'Bob', 'badgers', 'Carol', 'cats']
m.sort()
print(m)

# solusinya Untuk mengatasi kendala ini, Anda dapat memasukkan keyword str.lower sebagai argumen metode sort. Hal ini akan membuat metode sort menganggap semua objek menggunakan huruf kecil, tanpa mengubah kondisi asli dari objek tersebut.
spam = ['a', 'z', 'A', 'Z']
spam.sort(key=str.lower)
print(spam)

# String Literals
# Escape Character memungkinkan Anda untuk menggunakan karakter yang sebelumnya tidak bisa dimasukkan dalam string. Umumnya diawali dengan backslash (\) dan diikuti karakter tertentu yang diinginkan
st = 'Say hi to Bob\'s mother.'
print(st)
"""
\'          Single quote
\"          Double quote
\t          Tab
\n         Newline (line break)
\\          Backslash
"""

print("Hello there!\nHow are you?\nI\'m doing fine.")

# string lebih dari satu baris
multi_line = """Hello there!
How are you?
I'm fine."""
print(multi_line)

# raw string
print(r'That is Carol\'s cat.')
"""
    Python juga menyediakan cara untuk memasukkan string sesuai dengan apapun input atau teks yang diberikan. Metode ini dinamakan Raw Strings. Umumnya digunakan untuk regex atau beberapa implementasi lain yang sangat bergantung pada keberadaan backslash. Untuk menjadikan raw string, tambahkan huruf r sebelum pembuka string:
selengkapnya mengenai regex di https://www.w3schools.com/python/python_regex.asp
"""

"""
Jenis-jenis operator
Matematika dan string
+ (tambah)
    Menambahkan dua objek.

- (kurang)
    Mengurangkan operand kedua dari operand pertama. Jika hanya satu operand, diasumsikan nilai operand pertama adalah 0.

* (perkalian)
    Mengembalikan hasil perkalian angka atau mengembalikan string yang diulang sejumlah tertentu.

** (pangkat)
    Mengembalikan operand pertama pangkat operand kedua.
    3 ** 4 menghasilkan 81 (sama dengan 3 * 3 * 3 * 3).
    | Tips: untuk akar dua, gunakan pangkat 0.5.
/ (pembagian)
    Mengembalikan hasil pembagian operand pertama dengan operand kedua (float).

// (pembagian habis dibagi / div)
    Mengembalikan hasil pembagian operand pertama dengan operand kedua (bilangan bulat), kecuali jika salah satu operand adalah float, akan menghasilkan float.
    13 // 3 menghasilkan 4.
    -13 // 3 menghasilkan -5.
    9//1.81 menghasilkan 4.0.
% (modulo)
    Mengembalikan sisa bagi.


Operasi Bit
    << (left shift)
    Menggeser representasi bit/binary dari operand pertama sebanyak operand kedua ke kiri.
    2 << 2 menghasilkan 8.
    2 direpresentasikan sebagai 10 dalam binary.
    Geser ke kiri sebanyak 2x, menjadi 1000 (tambahkan 0 di belakangnya).
    1000 dalam binary bernilai 8 dalam desimal.
    
    >> (right shift)
    Menggeser representasi bit/binary dari operand pertama sebanyak operand kedua ke kanan.
    11 >> 1 menghasilkan 5.
    11 direpresentasikan sebagai 1011 dalam binary.
    Geser ke kanan sebanyak 1x, menjadi 101.
    101 dalam binary bernilai 5 dalam desimal.
    
    & (bit-wise AND)
    Menjalankan operasi binary AND pada representasi operand pertama dan kedua.
    5 & 3 menghasilkan 1.
    Representasi binary 5 adalah 101 dan representasi binary 3 adalah 011.
    101 and 011 bernilai 001.
    001 dalam desimal adalah 1.
    
    | (bit-wise OR)
    Menjalankan operasi binary OR pada representasi operand pertama dan kedua.
    5 | 3 menghasilkan 7.
    Representasi binary 5 adalah 101 dan representasi binary 3 adalah 011.
    101 or 011 bernilai 111.
    111 dalam desimal adalah 7.
    
    ^ (bit-wise XOR)
    Menjalankan operasi binary XOR pada representasi operand pertama dan kedua.
    5 ^ 3 menghasilkan 6.
    Representasi binary 5 adalah 101 dan representasi binary 3 adalah 011.
    101 xor 011 bernilai 110.
    110 dalam desimal adalah 6.
    
    ~ (bit-wise invert)
    Menjalankan operasi binary invert pada representasi operand.
    Nilai invert dari x adalah -(x+1), menggunakan metode Two’s Complement
    ~5 menghasilkan -6.
    
Lebih lanjut mengenai Two’s Complement dapat dibaca pada https://en.wikipedia.org/wiki/Two%27s_complement
"""

