""" Esta clase define una tarea con una descripción y un estado de completado. 
Tiene un constructor __init__ para inicializar la descripción y el estado de 
completado de la tarea."""
class Tarea:
    def __init__(self, descripcion):            
        self.descripcion = descripcion      
        self.completada = False             

""" Esta clase es un gestor que administra una lista de tareas. 
Tiene métodos para agregar una nueva tarea, marcar una tarea como completada, 
cambiar una tarea completada a pendiente, eliminar una tarea y mostrar todas 
las tareas."""
class GestorTareas:                         
    def __init__(self):                     
        self.tareas = []                    

    # Método agregar_tarea en la clase GestorTareas
    def agregar_tarea(self, descripcion):
        tarea = Tarea(descripcion)          
        self.tareas.append(tarea)           
        print("\033[34mHas agregado la tarea correctamente.\033[0m") 

    # Método para marcar la tarea como completada, avisa si ya está marcada como completa y excepción si la posición es incorrecta.       
    def marcar_completada(self, numero_tarea):
        try:                                                       
            tarea = self.tareas[numero_tarea - 1]                   
            if tarea.completada:
                print("\033[32m¡Despierta! Esta ya está completada.\033[0m")
            else:
                tarea.completada = True
                print("\033[32mTarea marcada como completada:\033[0m", tarea.descripcion)
        except IndexError:
            print("\033[31m¡Horror! Esa posición te la has inventado.\033[0m")
    
    # Método para cambiar una tarea completada a pendiente, avisa si ya está en pendiente o si la posición introducida no existe
    def cambiar_pendiente(self, numero_tarea):
        try:
            tarea = self.tareas[numero_tarea - 1]
            if not tarea.completada:
                print("\033[31m¡Despierta! Esto ya está en pendiente.\033[0m")
            else:
                tarea.completada = False
                print("\033[31mTarea cambiada a pendiente:\033[0m", tarea.descripcion)
        except IndexError:
            print("\033[31mDeja de inventar. La posición que has puesto no existe.\033[0m")

    # Método para eliminar una tarea y excepción si la posición introducida no existe
    def eliminar_tarea(self, numero_tarea):
        try:
            tarea_eliminada = self.tareas.pop(numero_tarea - 1)
            print(f"Tarea '{tarea_eliminada.descripcion}' eliminada.")
        except IndexError:
            print("\033[31mDeja de inventar. La posición que has puesto no existe.\033[0m")

    # Método para mostrar las tareas
    def mostrar_tareas(self):
        if not self.tareas:
            print("No hay tareas añadidas.")
        else:
            print("""
\033[34mLista de tareas:\033[0m                  
                  """)
            for i, tarea in enumerate(self.tareas, 1):
                if tarea.completada:
                    estado = "\033[32mCompletada\033[0m"
                else:
                    estado = "\033[31mPendiente\033[0m"
                print(f"\033[36m{i}.\033[0m {tarea.descripcion} [{estado}]")

""" 
Con if __name__ == "__main__":  verificamos si el script se está ejecutando como 
un programa independiente. Si es así "if" se ejecutará.
Entonces se creará una instancia de la clase GestorTareas llamada gestor. 
Permitiendo al usuer interactuar con el sistema a través del menú y realizar
operaciones como agregar, marcar como completada, cambiar a pendiente, eliminar 
o mostrar tareas.
"""
if __name__ == "__main__":
    gestor = GestorTareas()
    
    # Función principal de interacción con el usuario
    while True:                                         
        print("\n")
        print( """\033[33m
SISTEMA DE GESTIÓN DE TAREAS HOSTIL Ò.Ó 
  CREADO POR: CRISTINA CULEBRAS 2024\033[0m
====================================== 
              """)
        print("\033[34m| 1. Agregar Tarea\033[0m")
        print("\033[34m| 2. Marcar Tarea como Completada\033[0m")
        print("\033[34m| 3. Cambiar Tarea a Pendiente\033[0m")
        print("\033[34m| 4. Eliminar Tarea\033[0m")
        print("\033[34m| 5. Mostrar Tareas\033[0m")
        print("\033[34m| 6. Salir\033[0m")
        
        opcion = input("""
\033[30m¿Qué quieres hacer?: \033[0m""")
#asignación de nombre
        if opcion == "1":
            descripcion = input("\033[34m¿Cómo quieres llamar a esta tarea?: \033[0m")
            gestor.agregar_tarea(descripcion)
        #Para marcar como completada la tarea, lista y muestra estado de las tareas añadidas y muestra mensaje si no hay ninguna añadida
        elif opcion == "2":
            if gestor.tareas:
                gestor.mostrar_tareas()
                numero_tarea = int(input("""
\033[34m¿Qué tarea quieres marcar como completada?: \033[0m"""))
                gestor.marcar_completada(numero_tarea)
            else:
                print("\033[31mEnhorabuena. No tienes tareas pendientes.\033[0m")
        #Aquí cambiamos la tarea a pendiente, lista las tareas añadidas y avisa si no hay tareas.
        elif opcion == "3":
            if gestor.tareas:
                gestor.mostrar_tareas()
                numero_tarea = int(input("""
\033[34m¿Qué tarea quieres marcar como pendiente?: \033[0m"""))
                gestor.cambiar_pendiente(numero_tarea)
            else:
                print("\033[31mEnhorabuena. No tienes tareas pendientes.\033[0m")
        #Eliminar tarea, lista las tareas añadidas y avisa si no hay ninguna.
        elif opcion == "4":
            if gestor.tareas:
                gestor.mostrar_tareas()
                numero_tarea = int(input("\033[34m¿Qué tarea quieres eliminar?: \033[0m"))
                gestor.eliminar_tarea(numero_tarea)
            else:
                print("\033[31mEnhorabuena. No tienes tareas pendientes.\033[0m")
        #Lista las tareas añadidas y muestra estado
        elif opcion == "5":
            gestor.mostrar_tareas()
        elif opcion == "6":
            print("\033[34mSaliendo...\033[0m")
            break
        else:
            print("\033[31mSelecciona una opción válida. Pringao\033[0m")
