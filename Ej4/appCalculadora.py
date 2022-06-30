from tkinter import *
from tkinter import ttk
from functools import partial
from tkinter.tix import Tree
from claseFraccion1 import Fraccion

class Calculadora(object):
    __ventana = None
    __operador = None
    __panel = None
    __operadorAux = None
    __primerOperando = None
    __segundoOperando = None
    __fraccion1 = None
    __fraccion2 = None
    def __init__(self):
        self.__ventana = Tk()
        self.__ventana.title('Tk-Calculadora')
        mainframe = ttk.Frame(self.__ventana, padding="3 10 3 10")
        mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        mainframe.columnconfigure(0, weight=1)
        mainframe.rowconfigure(0, weight=1)
        mainframe['borderwidth'] = 2
        mainframe['relief'] = 'sunken'
        self.__panel = StringVar()
        self.__operador = StringVar()
        self.__operadorAux = None
        
        operatorEntry=ttk.Entry(mainframe, width=10, textvariable=self.__operador, justify='center', state='disabled') #---->panel de operadores
        operatorEntry.grid(column=1, row=1, columnspan=1, sticky=(W,E))
        panelEntry = ttk.Entry(mainframe, width=20, textvariable=self.__panel, justify='right',state='disabled') #---->panel de numeros
        panelEntry.grid(column=2, row=1, columnspan=2, sticky=(W, E))
        ttk.Button(mainframe, text=u"\u232B", command=partial(self.borrarPanel)).grid(column=4, row=1, sticky=(W, E)) #---->borrar
        


        ttk.Button(mainframe, text='1', command=partial(self.ponerNUMERO, '1')).grid(column=1, row=3, sticky=W)
        ttk.Button(mainframe, text='2', command=partial(self.ponerNUMERO,'2')).grid(column=2, row=3, sticky=W)
        ttk.Button(mainframe, text='3', command=partial(self.ponerNUMERO,'3')).grid(column=3, row=3, sticky=W)
        ttk.Button(mainframe, text='4', command=partial(self.ponerNUMERO,'4')).grid(column=1, row=4, sticky=W)
        ttk.Button(mainframe, text='5', command=partial(self.ponerNUMERO,'5')).grid(column=2, row=4, sticky=W)
        ttk.Button(mainframe, text='6', command=partial(self.ponerNUMERO,'6')).grid(column=3, row=4, sticky=W)
        ttk.Button(mainframe, text='7', command=partial(self.ponerNUMERO,'7')).grid(column=1, row=5, sticky=W)
        ttk.Button(mainframe, text='8', command=partial(self.ponerNUMERO,'8')).grid(column=2, row=5, sticky=W)
        ttk.Button(mainframe, text='9', command=partial(self.ponerNUMERO,'9')).grid(column=3, row=5, sticky=W)
        ttk.Button(mainframe, text='0', command=partial(self.ponerNUMERO, '0')).grid(column=2, row=6, sticky=W)
        ttk.Button(mainframe, text='+', command=partial(self.ponerOPERADOR, '+')).grid(column=4, row=4, sticky=W)
        ttk.Button(mainframe, text='-', command=partial(self.ponerOPERADOR, '-')).grid(column=4, row=5, sticky=W)
        ttk.Button(mainframe, text='*', command=partial(self.ponerOPERADOR, '*')).grid(column=5, row=4, sticky=W)
        ttk.Button(mainframe, text='%', command=partial(self.ponerOPERADOR, '%')).grid(column=5, row=3, sticky=W)
        ttk.Button(mainframe, text='=', command=partial(self.ponerOPERADOR, '=')).grid(column=5, row=5, sticky=W)
        ttk.Button(mainframe, text='/', command=partial(self.ponerNUMERO, '/')).grid(column=4, row=3, sticky=W) #----> para fraccion
        #ttk.Button(boton, command=partial(self.borrarPanel))#boton4=self.crearBoton(u"\u232B",escribir=False) #borrar


        panelEntry.focus() #---->cursor en el entry
        self.__ventana.mainloop()

    def ponerNUMERO(self, numero):
        aux = list(numero)
        b = False
        i = 0
        while not b and i < len(aux):
            if aux[i] == '/':
                b = True
            else:
                i+=1
        if self.__operadorAux == None:
            valor = self.__panel.get()
            # numero = str(numero)
            self.__panel.set(valor + numero)
        else:
            self.__operadorAux = None
            valor = self.__panel.get()
            if b:
                # numero = str(numero)
                
            else:
                #numero = str(numero)
                self.__primerOperando = int(valor)
            self.__panel.set(numero)

    def borrarPanel(self):
        aux = self.__panel.set('')
        if aux == None:
            self.__operador.set('')

    def resolverOperacion(self, operando1, operacion, operando2):
        auxop1 = list(operando1)
        auxop2 = list(operando2)
        b = False
        b1 = False
        i = 0
        while not b and i < len(auxop1):
            if auxop1[i] == '/':
                b = True
            else:
                i+=1
        i = 0
        while not b1 and i < len(auxop2):
            if auxop2[i] == '/':
                b1 = True
            else:
                i+=1
        if b:
            operando1 = Fraccion(auxop1)
        if b1:
            operando2 = Fraccion(auxop2)
        resultado = 0
        if operacion == '+':
            resultado = operando1+operando2
        else:
            if operacion == '-':
                resultado = operando1-operando2
            else:
                if operacion == '*':
                    resultado = operando1*operando2
                else:
                    if operacion == '%':
                        resultado = operando1/operando2
        self.__panel.set(str(resultado))

    def ponerOPERADOR(self, op):
        if op == '=':
            operacion = self.__operador.get()
            self.__segundoOperando = int(self.__panel.get())
            self.resolverOperacion(self.__primerOperando, operacion, self.__segundoOperando)
            self.__operador.set('')
            self.__operadorAux = None
        else:
            if self.__operador.get() == '':
                self.__operador.set(op)
                self.__operadorAux = op #---> asigna el operador elegido 
            else:
                operacion = self.__operador.get()
                self.__segundoOperando = int(self.__panel.get())
                self.resolverOperacion(self.__primerOperando, operacion, self.__segundoOperando)
                self.__operador.set(op)
                self.__operadorAux = op

    def ponerFraccion (self):
        # if op == '=':
            # operacion = self.__operador.get()
            # for i in range(1, 0):
            #     operacion = self.__operador.get()
            #     self.__segundoOperando = self.__panel.get()
            #     aux = self.__primerOperando + "/" + self.__segundoOperando
            #     print(aux)
            #     print(operacion)
            self.__fraccion1 = self.ponerNUMERO()
            self.__segundoOperando = self.__panel.get()
            aux = self.__fraccion1 + '/' + self.__segundoOperando
            print(aux)

            

