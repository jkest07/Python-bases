import os
from datetime import datetime

inv_file = "inventario.txt"
fac_file = "facturas.txt"

while True:
    print("\n1. Inventario")
    print("2. Facturas")
    print("3. Salir")
    op = input("Opción: ")

    if op == "1":  # INVENTARIO
        while True:
            print("\n--- INVENTARIO ---")
            print("1. Añadir")
            print("2. Listar")
            print("3. Buscar")
            print("4. Actualizar")
            print("5. Eliminar")
            print("6. Volver")
            opi = input("Opción: ")

            if opi == "1":
                if os.path.exists(inv_file):
                    with open(inv_file, "r") as f:
                        ln = f.readlines()
                else:
                    ln = []
                nid = str(len(ln) + 1)
                nom = input("Nombre: ")
                pre = float(input("Precio: "))
                stk = int(input("Stock: "))
                with open(inv_file, "a") as f:
                    f.write(f"{nid}|{nom}|{pre}|{stk}\n")
                print("Producto añadido.")

            elif opi == "2":
                if os.path.exists(inv_file):
                    with open(inv_file, "r") as f:
                        for l in f:
                            print(l.strip())
                else:
                    print("Inventario vacío.")

            elif opi == "3":
                bus = input("ID o nombre: ")
                if os.path.exists(inv_file):
                    with open(inv_file, "r") as f:
                        en = False
                        for l in f:
                            p = l.strip().split("|")
                            if p[0] == bus or p[1].lower() == bus.lower():
                                print("Encontrado:", l.strip())
                                en = True
                        if not en:
                            print("No encontrado.")
                else:
                    print("Inventario vacío.")

            elif opi == "4":
                uid = input("ID a actualizar: ")
                if os.path.exists(inv_file):
                    with open(inv_file, "r") as f:
                        ln = f.readlines()
                    nuevo = []
                    for l in ln:
                        p = l.strip().split("|")
                        if p[0] == uid:
                            pre = float(input("Nuevo precio: "))
                            stk = int(input("Nuevo stock: "))
                            nuevo.append(f"{p[0]}|{p[1]}|{pre}|{stk}\n")
                        else:
                            nuevo.append(l)
                    with open(inv_file, "w") as f:
                        f.writelines(nuevo)
                    print("Producto actualizado.")
                else:
                    print("Inventario vacío.")

            elif opi == "5":
                uid = input("ID a eliminar: ")
                if os.path.exists(inv_file):
                    with open(inv_file, "r") as f:
                        ln = f.readlines()
                    nuevo = [l for l in ln if l.split("|")[0] != uid]
                    with open(inv_file, "w") as f:
                        f.writelines(nuevo)
                    print("Producto eliminado.")
                else:
                    print("Inventario vacío.")

            elif opi == "6":
                break

    elif op == "2":  # FACTURAS
        while True:
            print("\n--- FACTURAS ---")
            print("1. Crear")
            print("2. Listar")
            print("3. Detalle")
            print("4. Eliminar")
            print("5. Volver")
            opf = input("Ingrese la opción: ")

            if opf == "1":
                if os.path.exists(fac_file):
                    with open(fac_file, "r") as f:
                        ln = f.readlines()
                else:
                    ln = []
                fid = str(len([l for l in ln if l.startswith("FACTURA")]) + 1)
                cli = input("Cliente: ")
                fh = datetime.now().strftime("%Y-%m-%d %H:%M")
                items, sbt = [], 0
                while True:
                    listar = []
                    if os.path.exists(inv_file):
                        with open(inv_file, "r") as f:
                            listar = f.readlines()
                    if not listar:
                        print("No hay inventario.")
                        break
                    for l in listar:
                        print(l.strip())
                    pid = input("ID prod (0=fin): ")
                    if pid == "0":
                        break
                    cant = int(input("Cant: "))
                    for l in listar:
                        p = l.strip().split("|")
                        if p[0] == pid:
                            tot = float(p[2]) * cant
                            items.append(f"ITEM|{p[0]}|{p[1]}|{cant}|{p[2]}|{tot}\n")
                            sbt += tot
                iva = sbt * 0.19
                ttl = sbt + iva
                with open(fac_file, "a") as f:
                    f.write(f"FACTURA|{fid}|{fh}|{cli}\n")
                    f.writelines(items)
                    f.write(f"SUBTOTAL|{sbt}\nIVA|{iva}\nTOTAL|{ttl}\n")
                print("Factura creada.")

            elif opf == "2":
                if os.path.exists(fac_file):
                    with open(fac_file, "r") as f:
                        for l in f:
                            if l.startswith("FACTURA"):
                                print(l.strip())
                else:
                    print("Sin facturas.")

            elif opf == "3":
                fid = input("ID factura: ")
                if os.path.exists(fac_file):
                    with open(fac_file, "r") as f:
                        pr = False
                        for l in f:
                            if l.startswith("FACTURA") and l.split("|")[1] == fid:
                                pr = True
                                print(l.strip())
                            elif pr and l.strip() != "" and not l.startswith("FACTURA"):
                                print(l.strip())
                                if l.startswith("TOTAL"):
                                    break
                else:
                    print("Sin facturas.")

            elif opf == "4":
                fid = input("ID factura a eliminar: ")
                if os.path.exists(fac_file):
                    with open(fac_file, "r") as f:
                        ln = f.readlines()
                    nuevo, skip = [], False
                    for l in ln:
                        if l.startswith("FACTURA") and l.split("|")[1] == fid:
                            skip = True
                        if skip and l.startswith("TOTAL"):
                            skip = False
                            continue
                        if not skip:
                            nuevo.append(l)
                    with open(fac_file, "w") as f:
                        f.writelines(nuevo)
                    print("Factura eliminada.")
                else:
                    print("Sin facturas.")

            elif opf == "5":
                break

    elif op == "3":
        print("Saliendo...")
        break
