# -*- coding: utf-8 -*-

from ClaseEmail import email

def test():
    email.crearCuenta('informatica.fcefn@gmail.com')
    email.crearCuenta('wicc2019@unsj-cuim.edu')
    email.crearCuenta('juanLiendro1957@yahoo.com')   

if __name__ == '__main__':
    idCuenta = input('idCuenta: ')
    dominio = input('dominio: ')
    tipoDom = input('tipo de dominio: ')
    contraseña = input('contraseña: ')
    correo = email(idCuenta,dominio,tipoDom,contraseña)
    

    nombre = input('Ingrese nombre del usuario: ')
    
    print('Estimado {} te enviaremos tus mensajes a la direccion {}'.format(nombre,correo.retornaEmail()))
    
    print('\n ----- Cambio de contraseña------ ')
    correo.cambiarContra()
    
    test()
    
    correo.buscar()