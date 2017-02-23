from xlrd import open_workbook,XL_CELL_TEXT
from tkinter import *

# Pentru tkinter:
root = Tk()
root.title("Test interactiv")

# Pentru xlrd:
book = open_workbook("D:\Kiki\Kevin's Stuff\Scoala\pt info\Test interactiv\Intrebari.xlsx")
sheet = book.sheet_by_index(0)

# Pentru stocarea in timp real a var butoanelor selectate:
raspunsuri_alese = []


# 1. Get number of questions

intrebari_total = sheet.nrows

# 2. Get questions in lists
# 2.1. Create lists for questions and answers
intrebari = []
raspunsuri = []
raspunsuri_corecte = []

for i in range(1,intrebari_total):
	#2.2. Append questions:

	intrebare = sheet.cell(i,1)
	intrebari.append(intrebare)
	#2.3. Create list for a set of questions
	lista = []

	#2.4. Append answers to multidimensional list:
	raspunsuri_total = sheet.row_slice(rowx=i, start_colx=2, end_colx=6)
	for elem in raspunsuri_total:
		lista.append(elem.value)
	raspunsuri.append(lista)

	#2.5. Get corect answer:
	raspuns_corect = sheet.cell(i,6)
	#print(int(raspuns_corect.value))
	raspunsuri_corecte.append(int(raspuns_corect.value))

#PENTRU DEBBUGING (a se adauga command = testare ca atribut la Radiobuttons):
#def testare():
	#zar = 0
	#while zar < 5:
		#lol = raspunsuri_alese[zar].get()
		#print(lol)
		#zar +=1



# 3. Print intrebari + raspunsuri din lists:

# j= Counter pt repeatul intrebarilor
j = 0

for i in intrebari:
	#print(i.value)
	myLabel = Label(root, text=i.value, fg="red")
	myLabel.pack()

	lista = raspunsuri[j]
	#print(lista)
	#Indicatii: Counterul trebuie sa creasca cu 1. Rasp corect se face din 4 in 4

	# Pentru radio buttons:
	counter = 1

	# Pentru event listening:
	cititor = IntVar()
	raspunsuri_alese.append(cititor)
	for k in lista:
		#print(k)
		#Do it radio (value nu e terminat inca)
		b = Radiobutton(root, text=k, value = counter, variable = cititor)
		b.pack()
		#print(counter)
		counter+=1

	j+=1
#print(raspunsuri_corecte)
#print(raspunsuri)


# 4. Creare button cu functie de comparare rasp_alese cu rasp_corecte

# 4.1. Creare functie de verificare rezultate
def verificare():
	contor = 0
	for i in range(len(raspunsuri_corecte)):
		raspuns_ales_selectat = raspunsuri_alese[i].get()
		#print(raspunsuri_corecte[i])
		#print(raspuns_ales_selectat)
		if raspunsuri_corecte[i] == raspuns_ales_selectat:
			#print("DA")
			contor += 1
		#else:
			#print("NU")
	print(contor)


# 4.2. Creare buton
gata = Button(root, text="Am terminat!", command=verificare)
gata.pack()



'''
===================================================PENTRU DEBUGGING==============================
#  Input raspuns
punctaj = 0
	raspuns = float(input("Raspunsul tau (numarul):"))

#  If raspuns == rasp corect Tpoints += 1

	if raspuns == raspuns_corect:

		punctaj += 1

#  print("Punctaj:" + Tpoints)
print(punctaj)

float(input("Test"))
==================================================================================================
'''

root.mainloop()