# # zad1
# ulubione_filmy=["Avengers", "Nowy początek", "Kryptonim U.N.C.L.E.", "Jason Bourne", "Coś", "Spider-man"]
# print(ulubione_filmy)
# ulubione_filmy.reverse()
# print(ulubione_filmy)
# ulubione_filmy.insert(5,"Thor")
# ulubione_filmy.insert(6,"Split")
# ulubione_filmy.insert(7,"Ugotowany")
# ulubione_filmy.insert(8,"Tożsamość zdrajcy")
# print(ulubione_filmy)
#
# # zad2
# slownik_filmow={'Sci-fi 1':ulubione_filmy[0],'Sci-fi 2':ulubione_filmy[4],'Sci-fi 3':ulubione_filmy[5],'Sci-fi 4':ulubione_filmy[6],'Sci-fi 5':ulubione_filmy[9]}
# slownik_filmow['Akcji 1']=ulubione_filmy[2]
# slownik_filmow['Akcji 2']=ulubione_filmy[3]
# slownik_filmow['Akcji 3']=ulubione_filmy[8]
# slownik_filmow['Komedio dramat 1']=ulubione_filmy[7]
# slownik_filmow['Horror 1']=ulubione_filmy[1]
# print(slownik_filmow)
#
# # zad3
# przedmioty={'WD':'Wizualizacja danych','CAD':'CAD Komputerowe wspomaganie programowania','Rric':'Rachunek różniczkowy i całkowy'}
# przedmioty['Ang']='Język angielski'
# przedmioty['Emd']='Elementy matematyki dyskretnej'
# przedmioty['PS']='Programowanie strukturalne'
# przedmioty['Kul kres']='Kultura kresów północno-wschodnich i jej kontynuacja'
# print(przedmioty)
# suma=0
# for x in przedmioty:
#     suma+=1
# print(suma)
#
# # zad4
# from math import *
# a=int(input('Wprowadź liczbę: '))
# a=pow(a,a)
# print(a)
#
# # zad5
#
# import sys as system
# ilosc=int(input("Długość ciągu znaków: "))
# x=0
# lista=[system.stdin.readline()]
# while x<ilosc-1:
#     lista.append(system.stdin.readline())
#     x+=1
# print(lista)
#
# # zad6
# a=int(input('Podaj a: '))
# b=int(input('Podaj b: '))
# c=int(input('Podaj c: '))
#
# if (a%2==0) & (b>c):
#     print('Warunki a parzyste oraz b>c zostały spełnione')
# else:
#     print('Warunki a parzyste oraz b>c nie zostały spełnione')