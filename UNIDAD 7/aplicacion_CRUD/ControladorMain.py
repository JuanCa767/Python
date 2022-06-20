import CRUD
import InterfaceGUI as GUI
import tkinter as tk
import sys

# cargar tarea
tareas = CRUD.Read()
if not (tareas):
    sys.exit(1)

#cargar mi ventana
m=GUI.ventanaMenuPrincipal(tareas)

#Mostrar mi ventana
m.mainloop()

