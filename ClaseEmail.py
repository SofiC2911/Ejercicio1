# -*- coding: utf-8 -*-
import re
import csv

class email:

    __idCuenta = ''
    __dominio = ''
    __tipoDom = ''
    __contraseña = ''

    def __init__(self, idCuenta, dominio, tipoDom, contraseña):
        self.__idCuenta = idCuenta
        self.__dominio = dominio
        self.__tipoDom = tipoDom
        self.__contraseña = contraseña
        
    def buscar(self):
        archi = open('RegCorreo.csv')
        reader = csv.reader(archi,delimiter=';')
        c = 0
        b = True
        dom = input('ingrese dominio a buscar: ')
        for i in reader:
            if b:
                b = not b
            elif i[1] == dom:
                c += 1
    
        print ('el dominio solicitado se repite {} veces'.format(c))
        archi.close()
    
    def retornaEmail(self):
        return '' + self.__idCuenta + '@' + self.__dominio + '.' + self.__tipoDom
    
    def getDominio(self):
        return self.__dominio
    
    def cambiarContra(self):
        cont = input('contraseña actual: ')
        
        if (cont == self.__contraseña):
            nueva = input('Nueva contraseña: ')
            self.__contraseña = nueva
            
        else:
            print('contraseña incorrecta')

    def crearCuenta(correoElec):
        
        if type(correoElec) == str:
            if (re.match('^[(a-z0-9\_\-\.)]+@[(a-z0-9\_\-\.)]+\.[(a-z)]{2,15}$',correoElec.lower())):
                print('\ncorreo: \n',correoElec)
                parte1 = re.split(r'[@]', correoElec)
                parte2 = re.split(r'[.]', parte1[1])
                idC = parte1[0]
                domi = parte2[0]
                tiD = parte2[1]
                contra = '123'
                e = email(idC,domi,tiD,contra)
                e.mostrarC()
        else:
            print('parametros con tipo incorrectos')
    
    def mostrarC(self):
        print('\n idCuenta: {}'.format(self.__idCuenta))
        print('\n dominio: {}'.format(self.__dominio) )
        print('\n tipo de dominio: {}'.format(self.__tipoDom))
        print('\n contraseña: {}'.format(self.__contraseña))