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
# a=float(input('Wprowadź liczbę: '))
# a=pow(a,a)
# print(a)
#
# # zad5
#
# import sys as system
# sys.stdout.write("Wczytaj tekst: ")
# tekst = sys.stdin.readline()
# sys.stdout.write(tekst)
# sys.stdout.write(str(tekst.count("a")))
# sys.stdout.write("\n")
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
#
# # zad7
# liczby = [1, 2, 3, 4, 5, 5.5]
# print(liczby)
# for i in range(0,len(liczby),1):
#     if i == 0:
#         print(liczby[i])
#     else:
#         suma = liczby[i] + liczby[i-1]
#         print(suma)
#
# # zad8
# x=0
# lista=[]
# while x<10:
#     a=input()
#     if liczba.count(".")==0:
#        int(liczba)
#        lista.append(liczba)
#     x+=1
# print(lista)
#
# # zad9
# import sys as system
# lista=[1,2,3,4,5,6]
# for y in lista:
#     for x in lista:
#         if y==1:
#             system.stdout.write('O')
#         elif y==len(lista):
#             system.stdout.write('O')
#         elif x==1:
#             system.stdout.write('O')
#         elif x==len(lista):
#             system.stdout.write('O')
#         else:
#             system.stdout.write(' ')
#     print('\n')
#
# zad10
# try:
#     wprowadzana_liczba = input("wprowadź liczbę: ")
#     wprowadzana_liczba = float(wprowadzana_liczba)
#     print(wprowadzana_liczba)
# except ValueError:
#     print("Wprowadzona wartość nie jest liczbą")