# -*- coding: utf-8 -*-
from Tkinter import *
root = Tk()

#Dpp - Ширина ПП
Dpp = 2400
#Lpp - длина ПП
Lp = 13500
#Lzo - длина от голопы ПП до задней оси
#Nzo - количество задних осей
Nzo = 3

col = int(Dpp/1200*Lp/800) - 1

entr = []

mainframe = Frame(root, width = 940)
setframe = Frame(mainframe, width = 200)
gridframe = Frame(mainframe, width = 600)
ansframe = Frame(mainframe, width = 500)
lb1 = Label(setframe, text = "Настройки Т и ПП").pack()
lb2 = Label(setframe, text = "Mt").pack()
lb2 = Label(setframe, text = "Mt")
ent2 = Entry(setframe)
ent2.pack()
lb2 = Label(setframe, text = "Nt20").pack()
ent3 = Entry(setframe)
ent3.pack()
lb2 = Label(setframe, text = "Lt").pack()
ent4 = Entry(setframe)
ent4.pack()
lb2 = Label(setframe, text = "L1").pack()
ent12 = Entry(setframe)
ent12.pack()
lb2 = Label(setframe, text = "Lpp").pack()
ent5 = Entry(setframe)
ent5.pack()
lb2 = Label(setframe, text = "LA").pack()
ent13 = Entry(setframe)
ent13.pack()
lb2 = Label(setframe, text = "LC").pack()
ent15 = Entry(setframe)
ent15.pack()
lb2 = Label(setframe, text = "Mpp").pack()
ent6 = Entry(setframe)
ent6.pack()
lb2 = Label(setframe, text = "N11").pack()
ent7 = Entry(setframe)
ent7.pack()
lb2 = Label(setframe, text = "N21").pack()
ent8 = Entry(setframe)
ent8.pack()



ansLb1 = Label(ansframe)
ansLb1.pack()
ansLb2 = Label(ansframe)
ansLb2.pack()
ansLb3 = Label(ansframe)
ansLb3.pack()
ansLb4 = Label(ansframe)
ansLb4.pack()
ansLb5 = Label(ansframe)
ansLb5.pack()




def calculate(event):
	Chisl = 0
	Znam = 0
	Mt = float(ent2.get())
	Nt20 = float(ent3.get())
	Lt = float(ent4.get())
	Lpp = float(ent5.get())
	Mpp = float(ent6.get())
	N11 = float(ent7.get())
	N21 = float(ent8.get())
	L1 = float(ent12.get())
	LA = float(ent13.get())
	LC = float(ent15.get())
	
	Lb = LA/col*2
	print "Lb",Lb
	for ent in range(col):
		if entr[ent][1].get() =='':
			continue
		else:
			mx = float(entr[ent][1].get())
			
			xn = (col/2-float(entr[ent][0]))*Lb+(Lb/2)-LC
			

			#xn = Lzo-800*float(entr[ent][0])+400
			Chisl = Chisl+mx*xn
			Znam = Znam+mx
	A = Chisl/Znam
	
	Mgr = Znam
	
	

	Xtct = Lt*Nt20/Mt
	#центр тяжести тягача
	
	N0 = N11+N21-Mt
	
	Xppct = N0*Lpp/(Mpp)
	
	N = (Mgr*A+Mpp*Xppct)/Lpp
	

	N3 = (Mgr + Mpp) - N
	N2 = (Mt*Xtct+N*L1)/Lt
	N1 = Mt+N-N2
	
	N1 = int(N1)
	N2 = int(N2)
	N3 = int(N3)

	ansLb1.configure(text = "Ось №1: "+str(N1))
	ansLb2.configure(text = "Ось №2: "+str(N2))
	ansLb3.configure(text = "Ось №3: "+str(N3/3))
	ansLb4.configure(text = "Ось №4: "+str(N3/3))
	ansLb5.configure(text = "Ось №5: "+str(N3/3))





row = 1
cl = 1
for ent in range(col):
	
	rowlb = Label(gridframe, text = row)
	rowlb.grid(row = row, column = 1)
	entr.append([int(rowlb['text']), Entry(gridframe, width = 10)])
	entr[ent][1].grid(row = row, column = cl+1)
	
	if cl == 2:
		cl = 1
		row = row+1
	else:
		cl = 2
calcbtn = Button(gridframe, text = "Рассчет")
calcbtn.bind('<Button-1>',calculate)
calcbtn.grid(row=col/2+1, column = 1, columnspan = 2)

setframe.pack(side = 'left')
gridframe.pack(side = 'right')
ansframe.pack(side = 'bottom')
mainframe.pack()
root.mainloop()
