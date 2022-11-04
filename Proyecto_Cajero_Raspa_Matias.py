#############
#Tp - Cajero
#############

def cajero():
    #Lista de usuarios
    usuarios = {
        1: {
            "user": "pepe",
            "password": 123,
            "pesos": 200.0,
            "dolares": 50.0,
            "alias": "pepe.el.grillo",
            "inversiones": {},
            "movimientos": []
        },
        2: {
            "user": "lionel",
            "password": 10,
            "pesos": 500.0,
            "dolares": 10.0,
            "alias": "lionel.goat.10",
            "inversiones": {},
            "movimientos": []
        }
    }
    #Inicio cajero
    print("\n\t###################################")
    print("\tBienvenido al cajero de codo a codo")
    print("\t###################################")
    print("\nElegi tu idioma:\n 1- Español \n 2- Ingles \n 3- Portugues")
    idioma = int(input("\nIngresa la opcion deseada: "))
    #1- Español
    if idioma == 1:
        print("\nHas seleccionado el idioma español")
        print("\n 1- Crear cuenta \n 2- Ingresar con una cuenta existente")
        ingresoCuenta = int(input("\nIngresa la opcion deseada: "))
        #1- Crear cuenta
        if ingresoCuenta == 1:
            user = str(input("\nIngresa un nombre para tu usuario: "))
            password = int(input("\nIngresa una contraseña: "))
            usuarios[len(usuarios)+1] = {
            "user": user,
            "password": password,
            "pesos": 0.0,
            "dolares": 0.0,
            "alias": user,
            "inversiones": {},
            "movimientos": []
            }
            print("\nCuenta creada con exito")
        #2- Ingresar cuenta existente
        elif ingresoCuenta == 2:
            user = str(input("\nIngresa tu nombre de usuario: "))
            password = int(input("\nIngresa tu clave: "))
        else:
            print("\nOpcion incorrecta")
        #Interrupcion/continuacion del programa
        interruptorBuscadorCuenta = 0
        peticionVolverAlMenu = "s"
        #Buscando usuario en cajero
        for usuarioActual in usuarios.values():
            if usuarioActual["user"] == user and usuarioActual["password"] == password:
                while peticionVolverAlMenu == "s":
                    interruptorBuscadorCuenta = 1
                    print("\n\t#############################")
                    print(f"\t¡Bienvenido a tu cuenta {usuarioActual.get('user')}!")
                    print("\t#############################\n")
                    print("1- Consultar saldo")
                    print("2- Depositar dinero")
                    print("3- Extraer dinero")
                    print("4- Transferir dinero")
                    print("5- Comprar dolares")
                    print("6- Vender dolares")
                    print("7- Crear plazo fijo")
                    print("8- Ver ultimos movimientos")
                    print("9- Salir de la cuenta")
                    opcionCuenta = int(input("\nIngresa la opcion deseada: "))
                    #1- Consultar saldo
                    if opcionCuenta == 1:
                        print(f"\nTu saldo actual en pesos es de: ${usuarioActual.get('pesos')}")
                        print(f"Tu saldo actual en dolares es de: u${usuarioActual.get('dolares')}")
                        #Regresar al menu principal
                        peticionVolverAlMenu = str(input("\n¿Desea realizar otra operacion? s/n: "))
                        #Registrar movimiento
                        usuarioActual["movimientos"].append("Consulta de saldos en cuenta")
                    #2- Depositar dinero
                    elif opcionCuenta == 2:
                        deposito = float(input("\nDigite por teclado el monto a depositar: $"))
                        if deposito < 0:
                            print("\nNo puede depositar ese monto")
                        else:
                            usuarioActual["pesos"] += deposito
                            print(f"\nGracias por ingresar su dinero, su saldo actual es de: ${usuarioActual.get('pesos')}")
                            #Registrar movimiento
                            usuarioActual["movimientos"].append(str(f"Deposito en cuenta por ${deposito}"))
                        #Regresar al menu principal
                        peticionVolverAlMenu = str(input("\n¿Desea realizar otra operacion? s/n: "))
                    #3- Extraer dinero
                    elif opcionCuenta == 3:
                        extraccion = float(input("\nIngresa el monto a extraer: $"))
                        if usuarioActual["pesos"] == 0 or (usuarioActual["pesos"] - extraccion) < 0 or extraccion < 0:
                            print("\nNo puede extraer ese monto")
                        else:
                            usuarioActual["pesos"] -= extraccion
                            print(f"\nExtraccion exitosa, tu saldo restante es de: ${usuarioActual.get('pesos')}")
                            #Registrar movimiento
                            usuarioActual["movimientos"].append(str(f"Extraccion en cuenta por ${extraccion}"))
                        #Regresar al menu principal
                        peticionVolverAlMenu = str(input("\n¿Desea realizar otra operacion? s/n: "))
                    #4- Transferir dinero
                    elif opcionCuenta == 4:
                        aliasATransferir = str(input("\nIngrese el alias de la cuenta a la cual deseas tranferir: "))
                        #Buscando alias
                        interruptorBuscadorAlias = 0
                        for usuario in usuarios.values():
                            if usuario["alias"] == aliasATransferir:
                                interruptorBuscadorAlias = 1
                                montoATransferir = float(input("\nIngresa el monto a tranferir: "))
                                if montoATransferir < 0 or (usuarioActual["pesos"] - montoATransferir) < 0:
                                    print("\nNo puede transferir ese monto")
                                else:
                                    confirmacionDeTransferencia = str(input(f"\nEstas por realizar una transferencia al alias {aliasATransferir}, con el siguiente monto: ${montoATransferir}\n¿Estas seguro que deseas realizar esta accion? s/n: "))
                                    if confirmacionDeTransferencia == "s":
                                        usuarioActual["pesos"] -= montoATransferir
                                        print(f"\nGracias tu tranferencia ha sido realizada con exito, tu saldo actual es de: ${usuarioActual.get('pesos')}")
                                        #Registrar movimiento
                                        usuarioActual["movimientos"].append(str(f"Transferencia realizada al alias {aliasATransferir} por un monto de ${montoATransferir}"))
                                    elif confirmacionDeTransferencia == "n":
                                        print("\nHas cancelado tu transferencia")
                                    else:
                                        print("\nOpcion incorrecta")
                        if interruptorBuscadorAlias == 0:
                            print("\nEl alias ingresado no existe")
                        #Regresar al menu principal
                        peticionVolverAlMenu = str(input("\n¿Desea realizar otra operacion? s/n: "))
                    #5- Comprar dolares
                    elif opcionCuenta == 5:
                        print("\nEl precio del dolar es de $160")
                        print(f"Tu saldo actual en dolares es de: u${usuarioActual.get('dolares')}")
                        compraDolar = float(input("\nIngresa el monto de dolares a comprar: u$"))
                        conversionAPesos = compraDolar * 160
                        if compraDolar < 0 or (usuarioActual["pesos"] - conversionAPesos) < 0:
                            print("\nNo puede realizar esta compra")
                        else:
                            confirmacionDeCompra = str(input(f"\n¿Confirmar la compra de u${compraDolar}? s/n: "))
                            if confirmacionDeCompra == "s":
                                usuarioActual["pesos"] -= conversionAPesos
                                usuarioActual["dolares"] += compraDolar
                                print(f"\nCompra realizada con exito")
                                print(f"\nTu saldo actual en pesos es de: ${usuarioActual.get('pesos')}")
                                print(f"Tu saldo actual en dolares es de: u${usuarioActual.get('dolares')}")
                                #Registrar movimiento
                                usuarioActual["movimientos"].append(str(f"Compra de u${compraDolar} dolares realizada por un monto de ${conversionAPesos} pesos"))
                            elif confirmacionDeCompra == "n":
                                print("\nHas cancelado tu compra")
                            else:
                                print("\nOpcion incorrecta")
                        #Regresar al menu principal
                        peticionVolverAlMenu = str(input("\n¿Desea realizar otra operacion? s/n: "))
                    #6- Vender dolares
                    elif opcionCuenta == 6:
                        print("\nEl precio del dolar es de $160")
                        print(f"Tu saldo actual en dolares es de: u${usuarioActual.get('dolares')}")
                        ventaDolar = float(input("\nIngresa el monto de dolares a vender: u$"))
                        conversionAPesos = ventaDolar * 160
                        if ventaDolar < 0 or (usuarioActual["dolares"] - ventaDolar) < 0:
                            print("\nNo puede realizar esta compra")
                        else:
                            confirmacionDeCompra = str(input(f"\n¿Confirmar la venta de u${ventaDolar}? s/n: "))
                            if confirmacionDeCompra == "s":
                                usuarioActual["pesos"] += conversionAPesos
                                usuarioActual["dolares"] -= ventaDolar
                                print(f"\nVenta realizada con exito")
                                print(f"\nTu saldo actual en pesos es de: ${usuarioActual.get('pesos')}")
                                print(f"Tu saldo actual en dolares es de: u${usuarioActual.get('dolares')}")
                                #Registrar movimiento
                                usuarioActual["movimientos"].append(str(f"Venta de u${ventaDolar} dolares"))
                            elif confirmacionDeCompra == "n":
                                print("\nHas cancelado la venta")
                            else:
                                print("\nOpcion incorrecta")
                        #Regresar al menu principal
                        peticionVolverAlMenu = str(input("\n¿Desea realizar otra operacion? s/n: "))
                    #7- Crear plazo fijo
                    elif opcionCuenta == 7:
                        print("\nEl rendimiento del plazo fijo en pesos a 30 dias es de 60%")
                        confirmacionOperacionPlazoFijo = str(input(f"\n¿Desea continuar? s/n: "))
                        if confirmacionOperacionPlazoFijo == "s":
                            montoPlazoFijo = float(input("\nIngresar el monto para la creacion del plazo fijo: $"))
                            if usuarioActual["pesos"] == 0 or (usuarioActual["pesos"] - montoPlazoFijo) < 0 or montoPlazoFijo < 100:
                                print("\nNo puede crear este plazo fijo")
                            else:
                                confirmacionPlazoFijo = str(input(f"\n¿Confirmar plazo fijo por ${montoPlazoFijo}? s/n: "))
                                if confirmacionPlazoFijo == "s":
                                    usuarioActual["pesos"] -= montoPlazoFijo
                                    interesesGanados = 60 * montoPlazoFijo / 100
                                    usuarioActual["inversiones"] = {
                                        "plazo": 30,
                                        "monto": montoPlazoFijo,
                                        "intereses": interesesGanados
                                    }
                                    print(f"\nGracias por crear tu plazo fijo, el saldo restante de la cuenta en pesos es de: ${usuarioActual.get('pesos')}")
                                    print(f"Las ganancias de tu plazo fijo seran de: ${interesesGanados}")
                                    #Registrar movimiento
                                    usuarioActual["movimientos"].append(f"Creacion de plazo fijo por ${montoPlazoFijo} pesos")
                                elif confirmacionPlazoFijo == "n":
                                    print("\nHas cancelado la creacion del plazo fijo")
                                else:
                                    print("\nOpcion incorrecta")
                        elif confirmacionOperacionPlazoFijo == "n":
                            print("\nVolviendo al menu principal...")
                        else:
                            print("\nOpcion incorrecta")
                        #Regresar al menu principal
                        peticionVolverAlMenu = str(input("\n¿Desea realizar otra operacion? s/n: "))
                    #8- Ver ultimos movimientos
                    elif opcionCuenta == 8:
                        print(f"\nSus ultimos movimientos fueron:\n")
                        incrementador = 1
                        for movimiento in usuarioActual['movimientos']:
                            print(f"\t{incrementador}- {movimiento}")
                            incrementador += 1
                        #Regresar al menu principal
                        peticionVolverAlMenu = str(input("\n¿Desea realizar otra operacion? s/n: "))
                    #9- Salir de la cuenta
                    elif opcionCuenta == 9:
                        peticionVolverAlMenu = "n"
                    while peticionVolverAlMenu != "n" and peticionVolverAlMenu != "s":
                            print("\nOpcion incorrecta")
                            peticionVolverAlMenu = str(input("\n¿Desea realizar otra operacion? s/n: "))
        if peticionVolverAlMenu == "n":
            print("\n\tGracias por confiar en nosotros, hasta la proxima.")
        if interruptorBuscadorCuenta == 0:
            print("\nEl nombre de usuario y/o clave son incorrectos")
    #2- Ingles
    elif idioma == 2:
        print("\nYou have selected the English language")
    #3- Portugues
    elif idioma == 3:
        print("\nVocê selecionou o idioma português")
    else:
        print("\nOpcion incorrecta")
#Llamado funcion
cajero()