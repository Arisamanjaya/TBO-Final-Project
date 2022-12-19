from modules.cnf import get_set_of_production
# ini adalah library yang digunakan untuk mengimport fungsi get_set_of_production

TRIANGULAR_TABLE = {} # ini adalah tabel yang digunakan untuk menyimpan hasil perhitungan CYK
g = None # ini adalah variabel global yang digunakan untuk menyimpan graf yang dibangun dari inputan user
previousNode = None # ini adalah variabel global yang digunakan untuk menyimpan node sebelumnya

def is_accepted(inputString): # ini adalah fungsi yang digunakan untuk mengecek apakah inputan user diterima atau tidak
    global TRIANGULAR_TABLE # ini adalah variabel global yang digunakan untuk menyimpan tabel yang digunakan untuk menyimpan hasil perhitungan CYK
    TRIANGULAR_TABLE.clear() # ini adalah fungsi yang digunakan untuk menghapus isi dari tabel yang digunakan untuk menyimpan hasil perhitungan CYK
    prodRules = get_set_of_production() # ini adalah variabel yang digunakan untuk menyimpan hasil dari fungsi get_set_of_production
    temp = inputString.lower().split(" ") # ini adalah variabel yang digunakan untuk menyimpan hasil dari fungsi get_set_of_production
    inputString = temp # ini adalah variabel yang digunakan untuk menyimpan hasil dari fungsi get_set_of_production
    for i in range(1,len(inputString)+1): # ini adalah perulangan yang digunakan untuk mengisi tabel yang digunakan untuk menyimpan hasil perhitungan CYK
        for j in range(i, len(inputString)+1): # ini adalah perulangan yang digunakan untuk mengisi tabel yang digunakan untuk menyimpan hasil perhitungan CYK
            TRIANGULAR_TABLE[(i,j)] = [] # ini adalah perulangan yang digunakan untuk mengisi tabel yang digunakan untuk menyimpan hasil perhitungan CYK
    for i in reversed(range(1, len(inputString)+1)): # ini adalah perulangan yang digunakan untuk mengisi tabel yang digunakan untuk menyimpan hasil perhitungan CYK
        for j in range(1, i+1): # ini adalah perulangan yang digunakan untuk mengisi tabel yang digunakan untuk menyimpan hasil perhitungan CYK
            if (j == j + len(inputString) - i): # ini adalah perulangan yang digunakan untuk mengisi tabel yang digunakan untuk menyimpan hasil perhitungan CYK
                tempList = [] # ini adalah perulangan yang digunakan untuk mengisi tabel yang digunakan untuk menyimpan hasil perhitungan CYK
                for key, value in prodRules.items(): # ini adalah perulangan yang digunakan untuk mengisi tabel yang digunakan untuk menyimpan hasil perhitungan CYK
                    for val in value: # ini adalah perulangan yang digunakan untuk mengisi tabel yang digunakan untuk menyimpan hasil perhitungan CYK
                        if (val == inputString[j-1] and key not in tempList): # ini adalah perulangan yang digunakan untuk mengisi tabel yang digunakan untuk menyimpan hasil perhitungan CYK
                            tempList.append(key) # ini adalah perulangan yang digunakan untuk mengisi tabel yang digunakan untuk menyimpan hasil perhitungan CYK
                TRIANGULAR_TABLE[(j, j + len(inputString) - i)] = tempList # ini adalah perulangan yang digunakan untuk mengisi tabel yang digunakan untuk menyimpan hasil perhitungan CYK
            else: # ini adalah perulangan yang digunakan untuk mengisi tabel yang digunakan untuk menyimpan hasil perhitungan CYK
                tempList = [] # ini adalah perulangan yang digunakan untuk mengisi tabel yang digunakan untuk menyimpan hasil perhitungan CYK
                resultList = [] # ini adalah perulangan yang digunakan untuk mengisi tabel yang digunakan untuk menyimpan hasil perhitungan CYK
                for k in range(len(inputString) - i): # ini adalah perulangan yang digunakan untuk mengisi tabel yang digunakan untuk menyimpan hasil perhitungan CYK
                    first = TRIANGULAR_TABLE[(j,j+k)] # ini adalah perulangan yang digunakan untuk mengisi tabel yang digunakan untuk menyimpan hasil perhitungan CYK
                    second = TRIANGULAR_TABLE[(j+k+1,j+len(inputString) - i)] # ini adalah perulangan yang digunakan untuk mengisi tabel yang digunakan untuk menyimpan hasil perhitungan CYK
                    for fi in first: # ini adalah perulangan yang digunakan untuk mengisi tabel yang digunakan untuk menyimpan hasil perhitungan CYK
                        for se in second: # ini adalah perulangan yang digunakan untuk mengisi tabel yang digunakan untuk menyimpan hasil perhitungan CYK
                            if (fi + " " + se not in tempList): # ini adalah perulangan yang digunakan untuk mengisi tabel yang digunakan untuk menyimpan hasil perhitungan CYK
                                tempList.append(fi + " " + se) # ini adalah perulangan yang digunakan untuk mengisi tabel yang digunakan untuk menyimpan hasil perhitungan CYK
                for key, value in prodRules.items(): # ini adalah perulangan yang digunakan untuk mengisi tabel yang digunakan untuk menyimpan hasil perhitungan CYK
                    for val in value: # ini adalah perulangan yang digunakan untuk mengisi tabel yang digunakan untuk menyimpan hasil perhitungan CYK
                        if (val in tempList and key not in resultList): # ini adalah perulangan yang digunakan untuk mengisi tabel yang digunakan untuk menyimpan hasil perhitungan CYK
                            resultList.append(key) # ini adalah perulangan yang digunakan untuk mengisi tabel yang digunakan untuk menyimpan hasil perhitungan CYK
                TRIANGULAR_TABLE[(j,j+len(inputString) - i)] = resultList # ini adalah perulangan yang digunakan untuk mengisi tabel yang digunakan untuk menyimpan hasil perhitungan CYK
    if "K" in TRIANGULAR_TABLE[(1, len(inputString))]: # ini adalah perulangan yang digunakan untuk mengisi tabel yang digunakan untuk menyimpan hasil perhitungan CYK
        return True # ini adalah perulangan yang digunakan untuk mengisi tabel yang digunakan untuk menyimpan hasil perhitungan CYK
    else: # ini adalah perulangan yang digunakan untuk mengisi tabel yang digunakan untuk menyimpan hasil perhitungan CYK
        return False # ini adalah perulangan yang digunakan untuk mengisi tabel yang digunakan untuk menyimpan hasil perhitungan CYK

