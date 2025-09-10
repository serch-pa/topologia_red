import tkinter as tk
from tkinter import ttk, messagebox,font
import telnetlib
import time
import asyncio


routers=[]
lienzo=""
imagen_router=""
routers2=[]
ip_entry=""
username_entry=""
password_entry=""
notebook=""
cuadros_texto=""
barra_progreso=""
ventana=""
etiqueta_progreso=""
barra_progreso2=""
etiqueta_progreso2=""


def conectar_telnet(router_ip, username, password):
    try:
        # Establecer conexión Telnet
        output=""
        output2=""
        outputroute=""
        outputroute2=""
        outputrun=""
        outputrun2=""
        outputlistas=""
        outputlistas2=""
        outputdhcp=""
        outputdhcp2=""
        outputnat=""
        outputnat2=""

        
        port = 23
        
        # Establecer conexión Telnet
        tn = telnetlib.Telnet(router_ip, port)

        # Leer la respuesta inicial del router
        output = tn.read_until(b"Username:", timeout=1).decode("utf-8")
        output2=""
        # Enviar el nombre de usuario al router
        tn.write(username.encode("utf-8") + b"\n")
        print(2)
        # Leer la respuesta del router
        output += tn.read_until(b"Password:", timeout=1).decode("utf-8")
        print(3)
        # Enviar la contraseña al router
        tn.write(password.encode("utf-8") + b"\n")

        # Leer la respuesta del router
        output += tn.read_until(b">", timeout=1).decode("utf-8")


        barra_progreso2['value'] = 16
        etiqueta_progreso2.config(text="Verificando:  {}%".format(16))
        ventana.update_idletasks()


        # Enviar el comando para mostrar las interfaces
        tn.write(b"show ip interface brief\n")
        print(4)
        # Leer y mostrar la salida de manera iterativa hasta que ya no haya más paginación
        while True:
            output = tn.read_until(b"--More--", timeout=1).decode("utf-8")
            output2+=output
            print(output)
            print("tamaño: ",len(output))
            
            if "--More--" not in output:
                break
        
            tn.write(b" ")
            print("espacio")


        barra_progreso2['value'] = 32
        etiqueta_progreso2.config(text="Verificando:  {}%".format(32))
        ventana.update_idletasks()

        # Enviar el comando para mostrar show ip route
        tn.write(b"show ip route\n")
        print("ip route")
        # Leer y mostrar la salida de manera iterativa hasta que ya no haya más paginación
        while True:
            outputroute = tn.read_until(b"--More--", timeout=1).decode("utf-8")
            outputroute2+=outputroute
            print(outputroute)
            print("tamaño: ",len(outputroute))
            
            if "--More--" not in outputroute:
                break
        
            tn.write(b" ")
            print("espacio route")   


        barra_progreso2['value'] = 48
        etiqueta_progreso2.config(text="Verificando:  {}%".format(48))
        ventana.update_idletasks()

        # Enviar el comando para mostrar show running
        tn.write(b"show running-config\n")
        print("running config")
        # Leer y mostrar la salida de manera iterativa hasta que ya no haya más paginación
        while True:
            outputrun = tn.read_until(b"--More--", timeout=3).decode("utf-8")
            outputrun2+=outputrun
            print(outputrun)
            print("tamaño: ",len(outputrun))
            
            if "--More--" not in outputrun:
                break
        
            tn.write(b" ")
            print("espacio route")    

        barra_progreso2['value'] = 64
        etiqueta_progreso2.config(text="Verificando:  {}%".format(64))
        ventana.update_idletasks()      


        # Enviar el comando para mostrar las interfaces
        tn.write(b"show access-lists\n")
        print("ACL")
        # Leer y mostrar la salida de manera iterativa hasta que ya no haya más paginación
        while True:
            outputlistas = tn.read_until(b"--More--", timeout=3).decode("utf-8")
            outputlistas2+=outputlistas
            print(outputlistas)
            
            print("tamaño: ",len(outputlistas))
            
            if "--More--" not in outputlistas:
                break
        
            tn.write(b" ")
            print("espacio")
            print(outputlistas2)



        barra_progreso2['value'] = 80
        etiqueta_progreso2.config(text="Verificando:  {}%".format(80))
        ventana.update_idletasks()


        # Enviar el comando para mostrar las interfaces
        tn.write(b"show ip dhcp pool\n")
        print("DHCPPP")
        # Leer y mostrar la salida de manera iterativa hasta que ya no haya más paginación
        while True:
            outputdhcp = tn.read_until(b"--More--", timeout=3).decode("utf-8")
            outputdhcp2+=outputdhcp
            print(outputdhcp)
            print("tamaño: ",len(outputdhcp))
            
            if "--More--" not in outputdhcp:
                break
        
            tn.write(b" ")
            print("espacio")    




        barra_progreso2['value'] = 96
        etiqueta_progreso2.config(text="Verificando:  {}%".format(96))
        ventana.update_idletasks()



        tn.write(b"show ip nat translations\n")
        print(" aqui nat ")
        # Leer y mostrar la salida de manera iterativa hasta que ya no haya más paginación
        while True:
            outputnat = tn.read_until(b"--More--", timeout=3).decode("utf-8")
            outputnat2+=outputnat
            print(outputnat)
            print("tamaño: ",len(outputnat))
            
            if "--More--" not in outputnat:
                break
        
            tn.write(b" ")
            print("espacio")    




        barra_progreso2['value'] = 99
        etiqueta_progreso2.config(text="Verificando:  {}%".format(99))
        ventana.update_idletasks()

        # Cerrar la conexión Telnet
        tn.close()
        
        
        

        # Devolver la salida
        return output2,outputroute2,outputrun2,outputlistas2,outputnat2,outputdhcp2

    except ConnectionRefusedError:
        messagebox.showerror("Error", "No se puede establecer la conexión Telnet")
    except Exception as e:
        messagebox.showerror("Error", str(e))

def conectar_telnet_callback():
    # Obtener los datos de conexión
    
    barra_progreso2['value'] = 0
    etiqueta_progreso2.config(text="Verificando:  {}%".format(0))
    ventana.update_idletasks()

    router_ip = ip_entry.get()
    username = username_entry.get()
    password = password_entry.get()

    # Llamar a la función conectar_telnet y obtener la salida
    output,outputroute,outputrun,outputlistas,outputnat,outputdhcp = conectar_telnet(router_ip, username, password)
    
    # Mostrar la salida en el cuadro de texto de la pestaña seleccionada
    print(notebook.select())
    
    pestaña_seleccionada = notebook.tab(notebook.select(), "text")
    print("pestaña: ",pestaña_seleccionada)
    cuadro_texto = cuadros_texto["Pestaña 1"]
    cuadro_texto.delete("1.0", tk.END)
    cuadro_texto.insert(tk.END, output)

    
    cuadro_texto = cuadros_texto["Pestaña 2"]
    cuadro_texto.delete("1.0", tk.END)
    cuadro_texto.insert(tk.END, outputroute)

    cuadro_texto = cuadros_texto["Pestaña 3"]
    cuadro_texto.delete("1.0", tk.END)
    cuadro_texto.insert(tk.END, outputrun)

    cuadro_texto = cuadros_texto["Pestaña 4"]
    cuadro_texto.delete("1.0", tk.END)
    cuadro_texto.insert(tk.END, outputlistas)

    cuadro_texto = cuadros_texto["Pestaña 5"]
    cuadro_texto.delete("1.0", tk.END)
    cuadro_texto.insert(tk.END, outputnat)

    cuadro_texto = cuadros_texto["Pestaña 6"]
    cuadro_texto.delete("1.0", tk.END)
    cuadro_texto.insert(tk.END, outputdhcp)



    barra_progreso2['value'] = 100
    etiqueta_progreso2.config(text="Verificando:  {}%".format(100))
    ventana.update_idletasks()













async def verificar_router(ip, username, password):
    print("dentro de verificar router")
    try:
        tn = telnetlib.Telnet(ip, timeout=5)
        tn.read_until(b"Username: ", timeout=5)
        tn.write(username.encode('ascii') + b"\n")
        tn.read_until(b"Password: ", timeout=5)
        tn.write(password.encode('ascii') + b"\n")
        tn.write(b"exit\n")
        tn.read_all()
        
        
        
        return True
        
        
        
    except Exception:
        return False
    
    

async def monitorear_routers():
    


        print("Verificando estado de los routers:")
        for router in routers:
            ip = router["ip"]
            username = router["username"]
            password = router["password"]
            verificacion =await verificar_router(ip, username, password)  
            
            print(verificacion)
            if  verificacion:
                print(f"{ip}: OK")
                if ip =="180.16.1.2":
                        lienzo.create_line(316, 116, 616, 116, fill="green", width=2)
                                                
                        print("hi")
                        
                elif ip=="180.16.2.2":
                        lienzo.create_line(316, 116, 316, 316, fill="green", width=2)
                        print("hi")

                elif ip=="172.16.1.21":
                        lienzo.create_line(316, 116, 166, 216, fill="green", width=2)
                        
                        print("hi")

                elif ip=="172.16.1.20":
                        lienzo.create_line(166, 216, 166, 316, fill="green", width=2)
                        
                        print("hi")

                elif ip=="180.16.3.2":
                        lienzo.create_line(316,316,616,316, fill="green", width=2)
                        print("hi")

                elif ip=="180.16.4.2":
                        lienzo.create_line(616,116,616,316, fill="green", width=2)
                        print("hi")
                               
                

            else:
                print(f"{ip}: Router apagado")
                if ip =="180.16.1.2":
                        print("hi")
                        lienzo.create_line(316, 116, 616, 116, fill="red", width=2)
                        # canvas.itemconfig(circle2, fill="red")
                        
                elif ip=="180.16.2.2":
                        print("hi")
                        lienzo.create_line(316, 116, 316, 316, fill="red", width=2)

                elif ip=="172.16.1.21":
                        lienzo.create_line(316, 116, 166, 216, fill="red", width=2)

                        lienzo.create_line(316, 116, 616, 116, fill="red", width=2)
                        lienzo.create_line(316, 116, 316, 316, fill="red", width=2)
                        lienzo.create_line(316,316,616,316, fill="red", width=2)
                        lienzo.create_line(616,116,616,316, fill="red", width=2)
                        break
                 
                        

                elif ip=="172.16.1.20":
                        lienzo.create_line(166, 216, 166, 316, fill="red", width=2)
                        lienzo.create_line(316, 116, 616, 116, fill="red", width=2)
                        lienzo.create_line(316, 116, 316, 316, fill="red", width=2)
                        lienzo.create_line(316, 116, 166, 216, fill="red", width=2)
                        lienzo.create_line(316,316,616,316, fill="red", width=2)
                        lienzo.create_line(616,116,616,316, fill="red", width=2)
                        break
                        
                        

                elif ip=="180.16.3.2":
                        lienzo.create_line(316,316,616,316, fill="red", width=2)
                        print("hi")   

                elif ip=="180.16.4.2":
                        lienzo.create_line(616,116,616,316, fill="red", width=2)
                        print("hi")                     

            print("mensaje en cada iteracion ")
            barra_progreso['value']+=19
            
            etiqueta_progreso.config(text="Verificando:  {}%".format(barra_progreso['value']))
            ventana.update_idletasks()            
        
        print("")

        # Esperar 1 minuto antes de la próxima verificación
        # time.sleep(2)
        print("inicio: ")


def cambiar_barra():
     time.sleep(2)

def monitorear_routers_asincrono():
    inicio = time.time()
      
    # cambiar lienzos a negros cuando se oprima el boton   
    lienzo.create_line(316, 116, 616, 116, fill="black", width=2)            
    lienzo.create_line(316, 116, 316, 316, fill="black", width=2)
    lienzo.create_line(316, 116, 166, 216, fill="black", width=2)
    lienzo.create_line(166, 216, 166, 316, fill="black", width=2)
    lienzo.create_line(316,316,616,316, fill="black", width=2)
    lienzo.create_line(616,116,616,316, fill="black", width=2)

    barra_progreso['value'] = 0
    etiqueta_progreso.config(text="Verificando:  {}%".format(0))
    ventana.update_idletasks()
 

    loop=asyncio.get_event_loop()
    print("dentro de funcion que llama a asincrona")
    loop.run_until_complete(monitorear_routers())
    print("completado")

    barra_progreso['value'] = 100
    etiqueta_progreso.config(text="Completado:  {}%".format(100))
    ventana.update_idletasks()

    fin=time.time()
    print(fin-inicio)
      


def imprimir_hola():
    print("Hola")
    time.sleep(2)

def clic_en_imagen(event):
    # Obtener las coordenadas x e y del evento de clic
    x = event.x
    y = event.y
    
    # Verificar si el clic está dentro de alguna imagen de router
    for router in routers2:
        router_x = router["x"]
        router_y = router["y"]
        if x >= router_x and x <= router_x + imagen_router.width() and y >= router_y and y <= router_y + imagen_router.height():
            abrir_ventana_router(router["IP"])


def conectar():
    print("conectar")

def abrir_ventana_router(router_name):
    # Crear una nueva ventana para mostrar la información del router
    # Crear la ventana
    # Crear la ventana
    print(router_name)
    ventana = tk.Tk()

    ventana.title("Conexión Telnet")
    ventana.geometry("750x550") #900x700

    # Etiquetas y campos de entrada
    ip_label = tk.Label(ventana, text="Dirección IP del router:")
    ip_label.pack()
    global ip_entry
    ip_entry = tk.Entry(ventana)
    ip_entry.pack()

    
    username_label = tk.Label(ventana, text="Nombre de usuario:")
    username_label.pack()
    global username_entry
    username_entry = tk.Entry(ventana)
    username_entry.pack()

    password_label = tk.Label(ventana, text="Contraseña:")
    password_label.pack()
    global password_entry
    password_entry = tk.Entry(ventana, show="*")
    password_entry.pack()

    # Botón para conectar
    connect_button = tk.Button(ventana, text="Conectar", command=conectar_telnet_callback)
    connect_button.pack()


     # Barra de progreso
    global barra_progreso2

    # Crear barra de progreso
    barra_progreso2 = ttk.Progressbar(ventana, orient='horizontal', length=300, mode='determinate')
    barra_progreso2.pack(pady=5)

    global etiqueta_progreso2
    # Crear etiqueta para mostrar el progreso
    etiqueta_progreso2 = tk.Label(ventana, text="Verificando: 0%")
    etiqueta_progreso2.pack()


    
    # Agregar valores del router
    ip_entry.insert(0,router_name)
    username_entry.insert(0,"cisco")
    password_entry.insert(0,"cisco")

    # Widget de Notebook (pestañas)
    global notebook
    notebook = ttk.Notebook(ventana)

    # Crear diccionario para almacenar los cuadros de texto de las pestañas
    global cuadros_texto
    cuadros_texto = {}

    # Crear pestañas
    pestaña1 = ttk.Frame(notebook)
    pestaña1.pack(fill="both", expand=True)
    cuadro_texto1 = tk.Text(pestaña1)
    cuadro_texto1.pack(fill="both", expand=True)
    notebook.add(pestaña1, text="Interface")
    cuadros_texto["Pestaña 1"] = cuadro_texto1

    pestaña2 = ttk.Frame(notebook)
    pestaña2.pack(fill="both", expand=True)
    cuadro_texto2 = tk.Text(pestaña2)
    cuadro_texto2.pack(fill="both", expand=True)
    notebook.add(pestaña2, text="Ip route")
    cuadros_texto["Pestaña 2"] = cuadro_texto2

    pestaña3 = ttk.Frame(notebook)
    pestaña3.pack(fill="both", expand=True)
    cuadro_texto3 = tk.Text(pestaña3)
    cuadro_texto3.pack(fill="both", expand=True)
    notebook.add(pestaña3, text="running-config")
    cuadros_texto["Pestaña 3"] = cuadro_texto3

    pestaña4 = ttk.Frame(notebook)
    pestaña4.pack(fill="both", expand=True)
    cuadro_texto4 = tk.Text(pestaña4)
    cuadro_texto4.pack(fill="both", expand=True)
    notebook.add(pestaña4, text="ACL")
    cuadros_texto["Pestaña 4"] = cuadro_texto4

    pestaña5 = ttk.Frame(notebook)
    pestaña5.pack(fill="both", expand=True)
    cuadro_texto5 = tk.Text(pestaña5)
    cuadro_texto5.pack(fill="both", expand=True)
    notebook.add(pestaña5, text="NAT")
    cuadros_texto["Pestaña 5"] = cuadro_texto5

    pestaña6 = ttk.Frame(notebook)
    pestaña6.pack(fill="both", expand=True)
    cuadro_texto6 = tk.Text(pestaña6)
    cuadro_texto6.pack(fill="both", expand=True)
    notebook.add(pestaña6, text="DHCP")
    cuadros_texto["Pestaña 6"] = cuadro_texto6

    # Mostrar el Notebook
    notebook.pack(fill="both", expand=True, padx=10, pady=10)


    


    # Iniciar el bucle principal de la ventana
    ventana.mainloop()
    
    # Agregar más información del router...
    # Puedes agregar más etiquetas, botones u otros widgets para mostrar la información deseada



def main():

    global routers
    routers = [
        {"ip": "172.16.1.20", "username": "cisco", "password": "cisco"},
        {"ip": "172.16.1.21", "username": "cisco", "password": "cisco"}, 
        {"ip": "180.16.1.2", "username": "cisco", "password": "cisco"},
        {"ip": "180.16.2.2", "username": "cisco", "password": "cisco"},
        {"ip": "180.16.3.2", "username": "cisco", "password": "cisco"},
        {"ip": "180.16.4.2", "username": "cisco", "password": "cisco"}
    ]
        # Crear la ventana

    # Crear la ventana principal
    global ventana
    ventana = tk.Tk()
    ventana.title("Topología de red")
    ventana.geometry("900x600") #800x600

    # Crear un lienzo (canvas)
    global lienzo
    lienzo = tk.Canvas(ventana, width=820, height=380, bg="white")
    lienzo.pack()

    # Cargar las imágenes de los routers
    global imagen_router
    imagen_router = tk.PhotoImage(file="enrutador.png").subsample(4)
    imagen_router_f=tk.PhotoImage(file="computadora.png").subsample(3)

    # Coordenadas de los routers
    global routers2
    routers2 = [
        {"nombre": "Router A", "x": 300, "y": 100,"IP":"172.16.1.21"},
        {"nombre": "Router B", "x": 600, "y": 100,"IP":"180.16.1.2"},
        {"nombre": "Router C", "x": 300, "y": 300,"IP":"180.16.2.2"},
        {"nombre": "Router D", "x": 600, "y": 300,"IP":"180.16.3.2"},
        {"nombre": "Router F", "x": 150, "y": 300,"IP":"192.168.100.10"},
        {"nombre": "Router E", "x": 150, "y": 200,"IP":"172.16.1.20"}
    ]

    # Mostrar los routers en el lienzo
    for router in routers2:
        x = router["x"]
        y = router["y"]
        if router["nombre"]=="Router F":
             lienzo.create_image(x, y, image=imagen_router_f, anchor="nw")
        else:
             lienzo.create_image(x, y, image=imagen_router, anchor="nw")
        lienzo.create_text(x+imagen_router.width()//2,y+imagen_router.height()+10,text=router["nombre"],anchor="center")

    # Conexiones entre los routers
    conexiones = [
        {"router1": "Router A", "router2": "Router B", "color": "black","IP":"180.16.1.0"},
        {"router1": "Router A", "router2": "Router C", "color": "black","IP":"180.16.2.0"},
        {"router1": "Router B", "router2": "Router D", "color": "black","IP":"180.16.4.0"},
        {"router1": "Router C", "router2": "Router D", "color": "black","IP":"180.16.3.0"},
        {"router1": "Router A", "router2": "Router E", "color": "black","IP":"172.16.1.0"},
        {"router1": "Router E", "router2": "Router F", "color": "black","IP":"192.168.100.0"}
    ]

    # Dibujar las líneas de conexión entre los routers
    for conexion in conexiones:
        router1 = next((r for r in routers2 if r["nombre"] == conexion["router1"]), None)
        router2 = next((r for r in routers2 if r["nombre"] == conexion["router2"]), None)
        if router1 and router2:
            x1 = router1["x"] + imagen_router.width() // 2
            y1 = router1["y"] + imagen_router.height() // 2
            x2 = router2["x"] + imagen_router.width() // 2
            y2 = router2["y"] + imagen_router.height() // 2
            color = conexion["color"]
            IP= conexion["IP"]
            text_font=font.Font(size=9,weight="bold")
            if color=="red":
                print(x1)
                print(y1)
                print(x2)
                print(y2)
            lienzo.create_line(x1, y1, x2, y2, fill=color, width=2)
            lienzo.create_text((x1+x2)//2,(y1+y2)//2,text=IP,font=text_font)

    # Asociar evento de clic a las imágenes de los routers
    lienzo.bind("<Button-1>", clic_en_imagen)

    # Crear el botón
    boton = tk.Button(ventana, text="¡Haz clic!", command=monitorear_routers_asincrono)
    boton.pack(pady=10)

    # Barra de progreso
    global barra_progreso
    
    # Crear barra de progreso
    barra_progreso = ttk.Progressbar(ventana, orient='horizontal', length=300, mode='determinate')
    barra_progreso.pack(pady=5)

    global etiqueta_progreso
    # Crear etiqueta para mostrar el progreso
    etiqueta_progreso = tk.Label(ventana, text="Verificando: 0%")
    etiqueta_progreso.pack()

    # Crear el primer cuadro de color "Sí"
    si_label = tk.Label(ventana, text="Conectado", bg="green", fg="white")
    si_label.pack(pady=5)

    # Crear el segundo cuadro de color "No"
    no_label = tk.Label(ventana, text="Sin conexion", bg="red", fg="white")
    no_label.pack(pady=5)

    # Iniciar el bucle principal de la ventana
    ventana.mainloop()


if __name__ == "__main__":
    main()
