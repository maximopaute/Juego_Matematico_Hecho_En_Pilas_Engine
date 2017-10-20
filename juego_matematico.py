"""
	Autor: Maximo Abel Paute Jumbo
	Carrera: Sistemas Informaticos y Computacion
"""
import pilasengine # Importamos las librerias

pilas = pilasengine.iniciar() # Para iniciar pilas engine
musica = pilas.sonidos.cargar("sonidos/bienvenida.wav")# Se carga un sonido.
musica.reproducir()# Se reproduce el sonido.

# --------------------------------------------------- INICIO CODIGO PRESENTACION DEL JUEGO ----------------------------------------------- #

class InicioJuego(pilasengine.escenas.Escena):# Clase para crear la pantalla de bienvenida inicial del juego

    def iniciar(self): #Se inicia la clase y se llama todas las funciones.
        self.pilas.fondos.FondoMozaico('imagenes/inicio.png') # Se implementa un fondo al Menu.
        actor_texto = self.pilas.actores.Actor() # Se declara la variable.
        actor_texto.imagen = "imagenes/click.png" # A la variable se le da una imagen.
        self._aplicar_animacion(actor_texto) # Función para aplicar animación.
        self.pilas.eventos.click_de_mouse.conectar(self._iniciar_el_juego)#Función para conctar Escenas.
        self._crear_indicador_creditos() # Función para crear créditos.

    def _aplicar_animacion(self, texto): # Función para aplicar animación a actor_texto.
        texto.y = -500 # Ubicación de la imagen en el eje y.
        texto.escala = 4 # Escala o tamaño de la imagen.
        texto.escala = [1], 1.5#Escala de la imagen.
        texto.y = [-200], 1

    def _iniciar_el_juego(self, evento): # Función para conectar las Escenas.
        self.pilas.escenas.EscenaMenu()#  Se conecta con la escena del Juego.


    def _crear_indicador_creditos(self): # Función para crear créditos.
        actor = self.pilas.actores.Actor()# Se crea la variable actor.
        actor.imagen = "imagenes/logo.png" # Se le da una imagen a esa variable.
        actor.escala = 0.17 # Escala de la imagen.
        actor.x = 200 # Ubicación de la imagen en el eje x.
        actor.y = -200 # Ubicación de la imagen en el eje y.
        actor.x = [400, 400, 270], 0.5 # Animación de la imagen
		
# ----------------------------------------------------- FIN CODIGO DE PRESENTACION DEL JUEGO ---------------------------------------------- #

# ----------------------------------------------------- INICIO: MENU DE INICIO PARA JUGAR ------------------------------------------------- #
class EscenaMenu(pilasengine.escenas.Escena): # Clase para crear la escena del menu principal del juego
	def iniciar(self): # Se inicia la clase
		self.fondo = self.pilas.fondos.Fondo("imagenes/menu_principal.png") # Se carga un fondo a la escena principal del juego

		dialogo=pilas.actores.Dialogo() # Muestra un mensaje de bienvenida
		self.mono1 = pilas.actores.Mono() # Personaje que muestra el mensaje
		self.mono1.x=270 # Ubicacion del personaje en el eje x que muestra el mensaje
		self.mono1.y=-50 # Ubicacion del personaje en el eje y que muestra el mensaje

		dialogo.decir(self.mono1, "HOLA AMIGUIT@!!! VAMOS A JUGAR CON LAS MATEMATICAS  ---> Presiona en mi")
		dialogo.decir(self.mono1, "DEMUESTRALES A TUS AMIG@S QUE ERES BUEN@ CON LOS NUMEROS. BUENA SUERTE!!!")

		dialogo.comenzar() # Comienza a mostrar el dialgo el personaje
		
		# Nos muestra el menu principal de juego 
		self.Mi_Menu = pilas.actores.Menu(
			[
				(u"Jugar Ahora", self.Ir_al_juego), 		# Primera opcion del menu principal
				(u"Ir a Ayuda", self.Ayuda),				# Segunda opcion del menu principal
				(u"Creditos", self.Creditos),				# Tercera opcion del menu principal
				(u"Salir del Juego", self.Salir_de_Pilas) 	# Cuarta opcion del menu principal
			])
		
		#  Nos muestra un texto en la parte inferior del menu principal
		Nombre_de_autor = pilas.actores.Texto(u"Autor: Maximo Abel Paute Jumbo") # Texto que se mostrara en el menu principal
		Nombre_de_autor.color = pilas.colores.amarillo # Le da el color al texto
		Nombre_de_autor.y = -210 # Ubicacion del texto en el eje y

	def actualizar(self): # Funcion que actualiza los objetos en la pantalla del juego 
		pass

	def Creditos(self): # Funcion que nos envia a una escena enlazada
		pilas.escenas.EscenaCreditos() # Se llama a la escena enlazada

	def Ayuda(self): # Funcion que nos envia a la escena ayuda
		pilas.escenas.EscenaAyuda() # Se llama a la escena enlazada

	def Salir_de_Pilas(self): # Funcion para salir del juego
		pilas.terminar() # Termnina y sale del juego

	def Ir_al_juego(self): # Funcion que nos envia a la escena operaciones
		pilas.escenas.EscenaOperaciones() # Se llama a la escena enlazada
		
# ----------------------------------------------------- FIN: MENU DE INICIO PARA JUGAR ------------------------------------------------- #

# ----------------------------------------------------- INICIO: OPERACIONES PARA JUGAR ------------------------------------------------- #
class EscenaOperaciones(pilasengine.escenas.Escena): # Clase para crear la escena del segundo menu de opciones del juego.
	def iniciar(self): # Se inicia la clase
		self.fondo = self.pilas.fondos.Fondo("imagenes/menu_operaciones.png") # Se carga un fondo a la escena de operaciones del juego

		dialogo=pilas.actores.Dialogo() # Nos muestra un mensaje del personaje
		self.mono1 = pilas.actores.Mono() # Personaje que muestra el mensaje
		self.mono1.x=270 # Ubicacion del mensaje en el eje x
		self.mono1.y=-50 # Ubicacion del mensaje en el eje y
		
		dialogo.decir(self.mono1, "Selecciona cualquiera de las opciones para jugar  ---> Presiona en mi")
		dialogo.decir(self.mono1, "Si respondes 10 veces bien ganas, si erras 3 veces pierdes")

		dialogo.comenzar() # Comienza a mostrar el mensaje

		self.Mi_Menu = pilas.actores.Menu( #  Parametro que contiene las opciones del menu
			[
				(u"Sumas y Restas", self.IrSuRes), # Primera opcion del menu principal
				(u"Multiplicaciones y Divisiones", self.IrMultiDivi), # Segundaa opcion del menu principal
				(u"Operaciones Combinadas", self.IrOperaCombi), # Tercera opcion del menu principal
				(u"Ir a Tutorial", self.Ayuda) # # Cuarta opcion del menu principal
			])
			
		#  Nos muestra un texto en la parte inferior del menu principal
		Nombre_de_autor = pilas.actores.Texto(u"Juego creado en Pilas Engine") # Texto que se mostrara en el menu principal
		Nombre_de_autor.color = pilas.colores.amarillo # Le da el color al texto
		Nombre_de_autor.y = -210 # Ubicacion del texto en el eje y

	def actualizar(self): # Funcion que actualiza los objetos en la pantalla del juego
		pass

	def IrOperaCombi(self): # Funcion que nos envia a una escena enlazada
		pilas.escenas.EscenaOperacionesCombinadas() # Se llama a la escena enlazada

	def IrMultiDivi(self): # Funcion que nos envia a una escena enlazada
		pilas.escenas.EscenaMultiplicacionDivision() # Se llama a la escena enlazada

	def Ayuda(self): # Funcion que nos envia a una escena enlazada
		pilas.escenas.EscenaAyuda() # Se llama a la escena enlazada

	def IrSuRes(self): # Funcion que nos envia a una escena enlazada
		pilas.escenas.EscenaSumaResta() # Se llama a la escena enlazada
		
# ----------------------------------------------------- FIN: OPERACIONES DE INICIO PARA JUGAR ------------------------------------------------- #

# ----------------------------------------------------- INICIO: ESCENA DE CREDITOS ------------------------------------------------- #

class EscenaCreditos(pilasengine.escenas.Escena): # Clase para crear la escena de créditos.
	def iniciar(self): # Se inicia la clase
		self.fondo = self.pilas.fondos.Fondo("imagenes/fondopantalla.png") # Se carga un fondo a la escena de operaciones del juego
		self.Boton_Volver =pilas.interfaz.Boton("Regresar al Menu")
		self.Boton_Volver.y = -220 # Ubicacion del boton en el eje y
		self.Boton_Volver.x = -250 # Ubicacion del boton en el eje x
		self.Boton_Volver.conectar(self.Volver) # Conecta con el boton para ir a la escena enlazada
		imagen = pilas.imagenes.cargar("imagenes/creditos.png") # Cargo una imagen a la escena
		actor = pilas.actores.Actor()
		actor.imagen = imagen

	def Volver(self): # Funcion para volver a la escena enlazada
		pilas.escenas.EscenaMenu() # Se llama a la escena enlazada
		
# ----------------------------------------------------- FIN: ESCENAS DE CREDITOS ------------------------------------------------- #

# ----------------------------------------------------- INICIO: ESCENA DE AYUDA ------------------------------------------------- #

class EscenaAyuda(pilasengine.escenas.Escena): # Clase para crear la escena de ayuda.
	def iniciar(self): # Se inicia la clase
		self.fondo = self.pilas.fondos.Fondo("imagenes/fondopantalla.png") # Se carga un fondo a la escena de ayuda del juego
		self.Boton_Volver =pilas.interfaz.Boton("Regresar al Menu") # Boton para regresar al menu principal
		self.Boton_Volver.y = -220 # Ubicacion del boton en el eje y
		self.Boton_Volver.x = -250 # Ubicacion del boton en el eje x
		self.Boton_Volver.conectar(self.Volver) # Conecta con el boton para ir a la escena enlazada
		imagen = pilas.imagenes.cargar("imagenes/ayuda.png") # Cargar una imagen a mi escena
		actor = pilas.actores.Actor()
		actor.imagen = imagen
		

	def Volver(self): # Funcion para volver a una escena definida
		pilas.escenas.EscenaMenu() # Conecta con la escena principal de menu
		
# ----------------------------------------------------- FIN: ESCENA DE AYUDA ------------------------------------------------- #

# ----------------------------------------------------- INICIO: ESCENA DE SUMA Y RESTAS ------------------------------------------------- #

class EscenaSumaResta(pilasengine.escenas.Escena):  # Clase para crear la escena de suma y resta.
	def iniciar(self): # Se inicia la clase
		self.nombre=raw_input("INGRESA TU NOMBRE PARA JUGAR: ") # Esta funcion nos pedira el nombre para jugar
		self.lista=[["Cuanto es 13 + 8 =?:", "21", "9", "7"],["Cuanto es 15 - 4 =?:", "11", "7", "3"],
					["Cuanto es 17 - 9 =?:", "8", "10", " 4"],["Cuanto es 29 + 5 =?:", "34", "29", "16"],
					["Cuanto es 7 + 8 =?:", "15", "21", "18"],["Cuanto es 23 - 8 =?:", "15", "11", "17"],
					["Cuanto es 23 - 17 =?:", "6", "9", "4"],["Cuanto 12 + 19 =?:", "31", "27", "42"],
					["Cuanto es 34 - 18 =?:", "16", "22", "13"],["Cuanto es 23 + 14 =?:", "37", "28", "41"],
					["Cuanto es 32 + 27 =?:", "59", "47", "63"],["Cuanto es 115 - 18 =?:", "97", "88", "104"],
					["Cuanto es 47 + 38=?:","85", "76", "68"],["Cuanto es 53 + 88 =?:", "141", "157", "195"],
					["Cuanto es 75 + 48 =?:","123", "142","118"],["Cuanto es 98 - 67 =?:", "31", "27", "38"],
					["Cuanto es 98 - 53 = ?:", "45", "56", "78"],["Cuanto es 54 + 37?:","91","88","113"],
					["Cuanto es 134 - 89?:","45","59","37"],["Cuanto es 37 + 58?:", "95", "87", "73"]] # 
	
		self.fondo = self.pilas.fondos.Fondo("imagenes/fondopantalla.png") # Cargo una imagen de fondo a mi escena
		
		# Color del puntaje que aumenta puntos correctos
		self.puntaje = pilas.actores.Puntaje(color="blanco") # Color del texto
		self.puntaje.x = -150 # Ubicacion del puntaje en el eje x
		self.puntaje.y = -190 # Ubicacion del puntaje en el eje y
		self.puntaje.valor = 0 # Inicia en cero el puntaje
		self.correctosaparecer=pilas.actores.Texto("Correctos: ") # Texto que se muestra en la escena del juego
		self.correctosaparecer.x=-220 # Ubicacion del puntaje que muestra en el eje x
		self.correctosaparecer.y=-190 # Ubicacion del puntaje que muestra en el eje y
		
		# Color del puntaje que aumenta puntos incorrectos
		self.error=pilas.actores.Puntaje(color="rojo") # Color del texto
		self.error.valor=0 # Inicia en cero el puntaje
		self.error.x=-150 # Ubicacion del puntaje en el eje x
		self.error.y=-220 # Ubicacion del puntaje en el eje y
		self.incorrectosaparecer=pilas.actores.Texto("Incorrectos: ") # Texto que se muestra en la escena del juego
		self.incorrectosaparecer.x=-230 # Ubicacion del puntaje que muestra en el eje x
		self.incorrectosaparecer.y=-220 # Ubicacion del puntaje que muestra en el eje y

		self.mono = pilas.actores.Mono()
		self.mono.escala = 0.8 # Tamaño del personaje
		self.mono.aprender('arrastrable') #Arraste el personaje
		self.mono.aprender('MoverseConElTeclado') 
		self.mono.decir("Bienvenido/a "+ self.nombre + " Juguemos... arrastrarme a la respuesta correcta") # Muestra el personaje un mensaje de bienvenida al jugador
		self.mono.x=[0,200],1 # Corre automaticamente al lado derecho luego de responder una pregunta

		# Boton para regresar al menu principal
		self.Boton_Volver =pilas.interfaz.Boton("Regresar al Menu") # Muestra el texto en el boton
		self.Boton_Volver.y = -220 # Ubicacion del boton en el eje x
		self.Boton_Volver.x = 250 # Ubicacion del boton en el eje x
		self.Boton_Volver.conectar(self.Volver) # Nos envia de regreso al menu principal
		
		# Boton que nos envia a la  escena credtos
		self.Boton_Creditos =pilas.interfaz.Boton("Ir a Creditos") # Muestra el texto en el boton
		self.Boton_Creditos.y = -220 # Ubicacion del boton en el eje y
		self.Boton_Creditos.x = 143 # Ubicacion del boton en el eje x
		self.Boton_Creditos.conectar(self.Creditos) # Nos envia a la escena creditos


		#Agrego las colisiones
		pilas.colisiones.agregar('aceituna', 'mono', self.el_mono_come)#añadido

		#Agrego tarea
		pilas.tareas.agregar(3, self.Preguntando)
		

	def Reiniciar(self):
    # Obtiene todos los actores de la pantalla.
		actores = pilas.actores.listar_actores()

    # Elimina todos los actores excepto el fondo y el puntaje
		for actor in actores:
			if actor not in [self.puntaje, self.fondo, self.mono,self.error,self.correctosaparecer,self.incorrectosaparecer,self.Boton_Volver]:
				actor.eliminar()

    # --- Genera una pregunta nueva --- #
		self.Preguntando()
	
		# Boton que nos envia a la  escena creditos
		self.Boton_Creditos =pilas.interfaz.Boton("Ir a Creditos") # Muestra el texto en el boton
		self.Boton_Creditos.y = -220 # Ubicacion del boton en el eje y
		self.Boton_Creditos.x = 143 # Ubicacion del boton en el eje x
		self.Boton_Creditos.conectar(self.Creditos) # Nos envia a la escena creditos

	# Ubicacion de las respuestas generadas
	def Preguntando(self): # Funcion que muestra la respuestas
		self.b1=pilas.actores.Aceituna() # Primera respuesta
		self.b1.x=-275 #Ubicacion de respuesta en eje x
		self.b1.y=100 #Ubicacion de respuesta en eje y
		self.b1.esverdadera=False
		self.b2=pilas.actores.Aceituna() # Segunda respuesta
		self.b2.x=-275 #Ubicacion de respuesta en eje x
		self.b2.y=0 #Ubicacion de respuesta en eje y
		self.b2.esverdadera=False
		self.b3=pilas.actores.Aceituna() # Tercera respuesta
		self.b3.x=-275 #Ubicacion de respuesta en eje x
		self.b3.y=-100 #Ubicacion de respuesta en eje y
		self.b3.esverdadera=False

		# Numero de preguntas agregadas
		self.poslista=pilas.azar(0,19) # Limite de las preguntas
		self.encuentrapreg=self.lista[self.poslista][0] # Comienza a generar las preguntas desde la primera
		self.mostrar_pregunta=pilas.actores.Texto(self.encuentrapreg) # Nos muestra la primera pregunta 
		self.mostrar_pregunta.y=210 # Ubicacion de la pregunta en el eje y
		self.mostrar_pregunta.escala=0.8 # Nos muestra la tamaño de letra de la pregunta
		
		# Ubicacion de la respuesta correcta de las preguntas
		self.respuesta_correcta = self.lista[self.poslista][1] #Respuesta Correcta
		self.respuesta_incorrecta_1 = self.lista[self.poslista][2] #Respuesta incorrecta 1
		self.respuesta_incorrecta_2 = self.lista[self.poslista][3] #Respuesta incorrecta 2

		# Ubicacion de las respuestas de las preguntas a responder
		self.rta_1 = pilas.actores.Texto("")
		self.rta_1.x=-230 # Ubicacion de la primera pregunta en el eje x
		self.rta_1.y=100  # Ubicacion de la primera pregunta en el eje y
		self.rta_2 = pilas.actores.Texto("")
		self.rta_2.x=-230 # Ubicacion de la segunda pregunta en el eje x
		self.rta_2.y=0 # Ubicacion de la segunda pregunta en el eje y
		self.rta_3 = pilas.actores.Texto("")
		self.rta_3.x=-230 # Ubicacion de la tercera pregunta en el eje x
		self.rta_3.y=-100 # Ubicacion de la tercera pregunta en el eje y

		#Aceitunas verdadera
		self.aceitunas_posibles = [self.b1,self.b2,self.b3]
		self.textos_posibles = [self.rta_1,self.rta_2,self.rta_3]
		self.indiceok=pilas.azar(0,2) # Que alguna de las tres respuestas son correctas
		self.aceituna_verdadera=self.aceitunas_posibles[self.indiceok]
		self.aceituna_verdadera.esverdadera=True
		self.texto_respuesta_verdadera=self.textos_posibles[self.indiceok]
		self.texto_respuesta_verdadera.texto=str(self.respuesta_correcta)
		
		# Condiciones de la respuesta correcta va preguntando cuando es la verdadera
		if self.b1.esverdadera: # Nos muestra aletoriamente las respuesta correcta
			self.rta_1.texto=str(self.respuesta_correcta) # Respuesta correcta
			self.rta_2.texto = str(self.respuesta_incorrecta_1)
			self.rta_3.texto = str(self.respuesta_incorrecta_2)
		elif self.b2.esverdadera:
			self.rta_2.texto=str(self.respuesta_correcta) # Respuesta correcta
			self.rta_1.texto = str(self.respuesta_incorrecta_1)
			self.rta_3.texto = str(self.respuesta_incorrecta_2)
		elif self.b3.esverdadera:
			self.rta_3.texto= str(self.respuesta_correcta) # Respuesta correcta
			self.rta_1.texto = str(self.respuesta_incorrecta_1)
			self.rta_2.texto = str(self.respuesta_incorrecta_2)

	def ganaste(self): # Funcion cuando se gana el juego
		actores = pilas.actores.listar_actores() # Muestra 

    # Elimina todos los actores excepto el fondo y el puntaje
		for actor in actores:
			if actor not in [self.mono]:
				actor.eliminar()
		self.fondo = self.pilas.fondos.Fondo("imagenes/fondopantalla.png")#cargo un fondo para mi menu
		self.Boton_Volver =pilas.interfaz.Boton("Regresar al Menu")
		self.Boton_Volver.y = -220 #Ubicacion del boton volver en el eje y
		self.Boton_Volver.x = 250 # Ubicacion del boton vovlver en el eje x
		self.Boton_Volver.conectar(self.Volver) # Conecta con la escena del menu principal
		self.puntajefinal=pilas.actores.Texto(str(self.puntaje.valor)) # Nos muestra el puntaje de respuestas correctas
		self.puntajefinal.escala=2 # Tamaño del puntaje correcto
		self.cartelfelicidades=pilas.actores.Texto("FELICIDADES " +self.nombre+ " has ganado") # Nos muestra un mensaje con el nombre del jugador
		self.cartelfelicidades.y=200 # Ubicacion del mensaje de texto en el eje y
		self.cartelfelicidades=pilas.actores.Texto("GRACIAS POR JUGAR NUESTRO JUEGO MATEMATICO") # Nos muestra un texto en la escena
		self.cartelfelicidades.y=100 # Ubicacion del texto en el eje y
		self.cartelpuntaje=pilas.actores.Texto(self.nombre+ " tu puntaje es: ") # Nos muestra el nombre del jugar y su puntaje obtenido
		self.cartelpuntaje.x=-150 # Ubicacion del texto de puntaje en el eje x
		self.errorestotales=pilas.actores.Texto(str(self.error.valor)) # Nos muestra el puntaje de respuestas incorrectas
		self.errorestotales.y=-100 # Ubicacion del puntaje incorrecto en el eje y
		self.errorestotales.escala=2 # Tamaño del puntaje
		self.cartelerror=pilas.actores.Texto(self.nombre+" tus errores son: ") # Nos muestra el nombre del jugar y su puntaje obtenido
		self.cartelerror.x=-150 # Ubicacion del texto de puntaje en el eje x
		self.cartelerror.y=-100 # Ubicacion del texto de puntaje en el eje y
		sonido = pilas.sonidos.cargar("sonidos/bien.wav") # Carga un sonido al juego
		sonido.reproducir() # Reproduce un sonido cuando respondes bien la pregunta
		self.mono.x=[0,200],1 # Corre automaticamente al lado derecho el personaje
		self.cartelfelicidades=pilas.actores.Texto("Autor: Maximo Abel Paute Jumbo") # Nos muestra un texto en la escena
		self.cartelfelicidades.y=-180 # Ubicacion del texto en el eje y
		self.cartelfelicidades=pilas.actores.Texto("2017 - 2018") # Nos muestra un texto en la escena
		self.cartelfelicidades.y=-210 # Ubicacion del texto en el eje y

	def perdiste(self): # Funcion cuando se pierde el juego
		actores = pilas.actores.listar_actores() # Obtiene todos los actores de la pantalla

    # Elimina todos los actores excepto el fondo y el puntaje
		for actor in actores:
			if actor not in [self.mono]:
				actor.eliminar()
		self.fondo = self.pilas.fondos.Fondo("imagenes/fondopantalla.png")#cargo un fondo para mi menu
		self.Boton_Volver =pilas.interfaz.Boton("Regresar al Menu")
		self.Boton_Volver.y = -220 #Ubicacion del boton volver en el eje y
		self.Boton_Volver.x = 250 # Ubicacion del boton vovlver en el eje x
		self.Boton_Volver.conectar(self.Volver) # Conecta con la escena del menu principal
		self.puntajefinal=pilas.actores.Texto(str(self.puntaje.valor)) # Nos muestra el puntaje de respuestas correctas
		self.puntajefinal.escala=2 # Tamaño del puntaje correcto
		self.cartelfelicidades=pilas.actores.Texto(" PERDISTE " +self.nombre+ " INTENTALO DE NUEVO") # Nos muestra un mensaje con el nombre del jugador
		self.cartelfelicidades.y=175 # Ubicacion del mensaje de texto en el eje y
		self.cartelfelicidades=pilas.actores.Texto("GRACIAS POR JUGAR NUESTRO JUEGO MATEMATICO") # Nos muestra un texto en la escena
		self.cartelfelicidades.y=100 # Ubicacion del texto en el eje y
		self.cartelpuntaje=pilas.actores.Texto(self.nombre+ " tu puntaje es: ") # Nos muestra el nombre del jugar y su puntaje obtenido
		self.cartelpuntaje.x=-150 # Ubicacion del texto de puntaje en el eje x
		self.errorestotales=pilas.actores.Texto(str(self.error.valor)) # Nos muestra el puntaje de respuestas incorrectas
		self.errorestotales.y=-100 # Ubicacion del puntaje incorrecto en el eje y
		self.errorestotales.escala=2 # Tamaño del puntaje
		self.cartelerror=pilas.actores.Texto(self.nombre+" tus errores son: ") # Nos muestra el nombre del jugar y su puntaje obtenido
		self.cartelerror.x=-150 # Ubicacion del texto de puntaje en el eje x
		self.cartelerror.y=-100 # Ubicacion del texto de puntaje en el eje y
		sonido = pilas.sonidos.cargar("sonidos/burla.wav") # Carga un sonido al juego
		sonido.reproducir() # Reproduce un sonido cuando responde mal una pregunta
		self.mono.x=[0,200],1 # Corre automaticamente al lado derecho el personaje
		self.cartelfelicidades=pilas.actores.Texto("Autor: Maximo Abel Paute Jumbo") # Nos muestra un texto en la escena
		self.cartelfelicidades.y=-175 # Ubicacion del texto en el eje y
		self.cartelfelicidades=pilas.actores.Texto("2017 - 2018") # Nos muestra un texto en la escena
		self.cartelfelicidades.y=-210 # Ubicacion del texto en el eje y
		
		# Boton que nos envia a la  escena creditos
		self.Boton_Creditos =pilas.interfaz.Boton("Intentar de nuevo") # Muestra el texto en el boton
		self.Boton_Creditos.y = -220 # Ubicacion del boton en el eje y
		self.Boton_Creditos.x = -250 # Ubicacion del boton en el eje x
		self.Boton_Creditos.conectar(self.Creditos) # Nos envia a la escena intentar de nuevo

	def Creditos(self): # Funcion que nos envia a una escena enlazada
		pilas.escenas.EscenaSumaResta() # Se llama a la escena enlazada
	


	def Volver(self): # Funcion para volver a la escena enlazada
		pilas.escenas.EscenaMenu() # Se llama a la escena enlazada

	def actualizar(self): # Funcion que actualiza los objetos en la pantalla del juego
		pass


	def el_mono_come(self, aceitunas, mono): # Funciona que evalua la respuesta
		if not aceitunas.esverdadera: #aceitunas es la aceituna colisionada
			if self.error.valor<2: # Si la respuesta no es correcta acumula un punto incorrecto
				pilas.camara.vibrar() # Vibra la pantalla cuando responde mal
				aceitunas.eliminar() # Se elimina el actor de la respuesta seleccionada
				sonido = pilas.sonidos.cargar("sonidos/burla.wav") # Carga un sonido al juego
				sonido.reproducir() # Reproduce un sonido cuando respondes mal la pregunta
				mono.decir("Incorrecto!!! " + self.nombre + " No te rindas sigue avanzando")
				self.mono.x=[0,200],1 # Corre automaticamente al lado derecho el personaje
				self.error.aumentar() #aumenta 1 error. En total puede ser hasta 3 errores.
				pilas.tareas.agregar(3, self.Reiniciar) # Se reinicia y vuelve aparecer las tres respuestas

			else: # Si llega al limite termina el juego y pierdes
				pilas.avisar("Fin del juego") # Termina el juego
				self.error.aumentar() # Aumenta el puntaje en puntos incorrectos
				self.perdiste() # Termina y pierdes el juego

		else:
			if self.puntaje.valor<9: # Limite del puntaje para ganar el juego
				aceitunas.eliminar() #hay que eliminar la aceituna colisionada
				mono.rotacion=[0,360] # Cuando se responde bien la pregunta el personaje gira para celebrar
				sonido = pilas.sonidos.cargar("sonidos/bien.wav") # Carga un sonido al juego
				sonido.reproducir() # Reproduce un sonido cuando respondes bien una pregunta
				mono.decir("Correcto!!! " + self.nombre + " sigue avanzando")
				self.mono.x=[0,200],1 # Corre automaticamente al lado derecho el personaje
				estrella = pilas.actores.Estrella() # Muestra una estrella al responder bien la respuesta
				estrella.x = aceitunas.x # Ubicacion de la estrella encima de la respuesta correcta en el eje x
				estrella.y = aceitunas.y # Ubicacion de la estrella encima de la respuesta correcta en el eje y
				estrella.escala = 0.2 # Tamaño de la estrella
				estrella.escala = [2, 1] * 2 # Tamaño de la estrella al hacer zoom
				self.puntaje.aumentar() # Aumenta el puntaje en correcto
				pilas.tareas.agregar(3, self.Reiniciar) # Se reinicia y vuelve aparecer las tres respuestas
			else: # Si llega al limite termina el juego y ganas el juego
				pilas.avisar("Felicidades has ganado") # Muestra un mensaje que has ganado
				self.puntaje.aumentar() # Aumenta el puntaje en puntos incorrectos
				self.ganaste() # Termina y ganas el juego



	def Volver(self): # Funcion para volver a la escena enlazada
		pilas.escenas.EscenaMenu() # Se llama a la escena enlazada

	def actualizar(self): # Funcion que actualiza los objetos en la pantalla del juego
		pass
		
# ----------------------------------------------------- FIN: ESCENA DE SUMAS Y RESTAS ------------------------------------------------- #

# ----------------------------------------------------- INICIO: ESCENA DE MULTIPLICACIONES Y DIVISIONES ------------------------------------------------- #
		
class EscenaMultiplicacionDivision(pilasengine.escenas.Escena): # Clase para crear la escena de suma y resta.
	def iniciar(self): # Se inicia la clase
		self.nombre=raw_input("INGRESA TU NOMBRE PARA JUGAR: ") # Esta funcion nos pedira el nombre para jugar
		self.lista=[["Cuanto es 9 * 7 =?:", "63", "34", "21"],["Cuanto es 36 / 6 =?:", "6", "7", "3"],
					["Cuanto es 81 / 9 =?:", "9", "7", "11"],["Cuanto es 12 * 7 =?:", "84", "69", "96"],
					["Cuanto es 7 * 8 =?:", "56", "43", "68"],["Cuanto es 28 / 4 =?:", "7", "4", "9"],
					["Cuanto es 25 * 7 =?:", "175", "140", "205"],["Cuanto 12 / 4 =?:", "3", "7", "1"],
					["Cuanto es 34 * 8 =?:", "272", "184", "138"],["Cuanto es 96 / 8 =?:", "12", "28", "56"],
					["Cuanto es 29 * 9 =?:", "261", "147", "163"],["Cuanto es 135 / 9 =?:", "15", "23", "48"],
					["Cuanto es 47 * 3=?:","141", "156", "168"],["Cuanto es 144 / 12 =?:", "12", "15", "19"],
					["Cuanto es 75 / 3 =?:","25", "14","18"],["Cuanto es 98 * 6 =?:", "588", "374", "282"],
					["Cuanto es 53 * 8 =?:", "424", "156", "378"],["Cuanto es 343 / 7 =?:","49","38","87"],
					["Cuanto es 525 / 25 =?:","21","59","37"],["Cuanto es 37 * 5 =?:", "185", "87", "173"]]

		self.fondo = self.pilas.fondos.Fondo("imagenes/fondopantalla.png") # Cargo una imagen de fondo a mi escena
		
		# Color del puntaje que aumenta puntos correctos
		self.puntaje = pilas.actores.Puntaje(color="blanco") # Color de texto
		self.puntaje.x = -150 # Ubicacion del puntaje en el eje x
		self.puntaje.y = -190 # Ubicacion del puntaje en el eje y
		self.puntaje.valor = 0 # Inicia en cero el puntaje
		self.correctosaparecer=pilas.actores.Texto("Correctos: ") # Texto que se muestra en la escena del juego
		self.correctosaparecer.x=-220 # Ubicacion del puntaje que muestra en el eje x
		self.correctosaparecer.y=-190 # Ubicacion del puntaje que muestra en el eje y
		
		# Color del puntaje que aumenta puntos incorrectos
		self.error=pilas.actores.Puntaje(color="rojo") # Color de texto
		self.error.valor=0 # Inicia en cero el puntaje
		self.error.x=-150 # Ubicacion del puntaje en el eje x
		self.error.y=-220 # Ubicacion del puntaje en el eje x
		self.incorrectosaparecer=pilas.actores.Texto("Incorrectos: ") # Texto que se muestra en la escena del juego
		self.incorrectosaparecer.x=-230 # Ubicacion del puntaje que muestra en el eje x
		self.incorrectosaparecer.y=-220 # Ubicacion del puntaje que muestra en el eje y

		self.mono = pilas.actores.Mono()
		self.mono.escala = 0.8 # Tamaño del personaje
		self.mono.aprender('arrastrable') #Arraste el personaje
		self.mono.aprender('MoverseConElTeclado') 
		self.mono.decir("Bienvenido/a "+ self.nombre + " Juguemos... arrastrarme a la respuesta correcta") # Muestra el personaje un mensaje de bienvenida al jugador
		self.mono.x=[0,200],1 # Corre automaticamente al lado derecho luego de responder una pregunta
		
		# Boton para regresar al menu principal
		self.Boton_Volver =pilas.interfaz.Boton("Regresar al Menu") # Muestra el texto en el boton
		self.Boton_Volver.y = -220 # Ubicacion del boton en el eje y
		self.Boton_Volver.x = 250 # Ubicacion del boton en el eje x
		self.Boton_Volver.conectar(self.Volver) # Nos envia a la escena menu principal
		
		# Boton para regresar al menu principal
		self.Boton_Creditos =pilas.interfaz.Boton("Ir a Creditos") # Muestra el texto en el boton
		self.Boton_Creditos.y = -220 # Ubicacion del boton en el eje y
		self.Boton_Creditos.x = 143 # Ubicacion del boton en el eje x
		self.Boton_Creditos.conectar(self.Creditos) # Conectar a la escena enlazada
	

		#Agrego las colisiones
		pilas.colisiones.agregar('aceituna', 'mono', self.el_mono_come)#añadido

		#Agrego tarea
		pilas.tareas.agregar(3, self.Preguntando)
		

	def Reiniciar(self):
		actores = pilas.actores.listar_actores() # Obtiene todos los actores de la pantalla.

    # Elimina todos los actores excepto el fondo y el puntaje
		for actor in actores:
			if actor not in [self.puntaje, self.fondo, self.mono,self.error,self.correctosaparecer,self.incorrectosaparecer,self.Boton_Volver]:
				actor.eliminar()

    # Genera una pregunta nueva
		self.Preguntando()
		
		# Boton para ir a la escena creditos
		self.Boton_Creditos =pilas.interfaz.Boton("Ir a Creditos") # Muestra el texto en el boton
		self.Boton_Creditos.y = -220 # Ubicacion del boton en el eje y
		self.Boton_Creditos.x = 143 # Ubicacion del boton en el eje x
		self.Boton_Creditos.conectar(self.Creditos) # Conectar a la escena enlazada


	# Ubicacion de las respuestas generadas
	def Preguntando(self): # Funcion que muestra la respuestas
		self.b1=pilas.actores.Aceituna() # Primera respuesta
		self.b1.x=-275 #Ubicacion de respuesta en eje x
		self.b1.y=100 #Ubicacion de respuesta en eje y
		self.b1.esverdadera=False
		self.b2=pilas.actores.Aceituna() # Segunda respuesta
		self.b2.x=-275 #Ubicacion de respuesta en eje x
		self.b2.y=0 #Ubicacion de respuesta en eje y
		self.b2.esverdadera=False
		self.b3=pilas.actores.Aceituna() # Tercera respuesta
		self.b3.x=-275 #Ubicacion de respuesta en eje x
		self.b3.y=-100 #Ubicacion de respuesta en eje y
		self.b3.esverdadera=False

		# Numero de preguntas agregadas
		self.poslista=pilas.azar(0,19) # Limite de las preguntas
		self.encuentrapreg=self.lista[self.poslista][0] # Comienza a generar las preguntas desde la primera
		self.mostrar_pregunta=pilas.actores.Texto(self.encuentrapreg) # Nos muestra la primera pregunta 
		self.mostrar_pregunta.y=210 # Ubicacion de la pregunta en el eje y
		self.mostrar_pregunta.escala=0.8 # Nos muestra la tamaño de letra de la pregunta

		# Ubicacion de la respuesta correcta de las preguntas
		self.respuesta_correcta = self.lista[self.poslista][1] #Respuesta Correcta
		self.respuesta_incorrecta_1 = self.lista[self.poslista][2] #Respuesta incorrecta 1
		self.respuesta_incorrecta_2 = self.lista[self.poslista][3] #Respuesta incorrecta 2

		# Ubicacion de las respuestas de las preguntas a responder
		self.rta_1 = pilas.actores.Texto("")
		self.rta_1.x=-230 # Ubicacion de la primera pregunta en el eje x
		self.rta_1.y=100  # Ubicacion de la primera pregunta en el eje y
		self.rta_2 = pilas.actores.Texto("")
		self.rta_2.x=-230 # Ubicacion de la segunda pregunta en el eje x
		self.rta_2.y=0 # Ubicacion de la segunda pregunta en el eje y
		self.rta_3 = pilas.actores.Texto("")
		self.rta_3.x=-230 # Ubicacion de la tercera pregunta en el eje x
		self.rta_3.y=-100 # Ubicacion de la tercera pregunta en el eje y

		#Aceitunas verdadera
		self.aceitunas_posibles = [self.b1,self.b2,self.b3]
		self.textos_posibles = [self.rta_1,self.rta_2,self.rta_3]
		self.indiceok=pilas.azar(0,2) # Que alguna de las tres respuestas son correctas
		self.aceituna_verdadera=self.aceitunas_posibles[self.indiceok]
		self.aceituna_verdadera.esverdadera=True
		self.texto_respuesta_verdadera=self.textos_posibles[self.indiceok]
		self.texto_respuesta_verdadera.texto=str(self.respuesta_correcta)
		
		# Condiciones de la respuesta correcta va preguntando cuando es la verdadera
		if self.b1.esverdadera: # Nos muestra aletoriamente las respuesta correcta
			self.rta_1.texto=str(self.respuesta_correcta) # Respuesta correcta
			self.rta_2.texto = str(self.respuesta_incorrecta_1)
			self.rta_3.texto = str(self.respuesta_incorrecta_2)
		elif self.b2.esverdadera:
			self.rta_2.texto=str(self.respuesta_correcta) # Respuesta correcta
			self.rta_1.texto = str(self.respuesta_incorrecta_1)
			self.rta_3.texto = str(self.respuesta_incorrecta_2)
		elif self.b3.esverdadera:
			self.rta_3.texto= str(self.respuesta_correcta) # Respuesta correcta
			self.rta_1.texto = str(self.respuesta_incorrecta_1)
			self.rta_2.texto = str(self.respuesta_incorrecta_2)

	def ganaste(self): # Funcion cuando se gana el juego
		actores = pilas.actores.listar_actores() # Muestra 

    # Elimina todos los actores excepto el fondo y el puntaje
		for actor in actores:
			if actor not in [self.mono]:
				actor.eliminar()
		self.fondo = self.pilas.fondos.Fondo("imagenes/fondopantalla.png")#cargo un fondo para mi menu
		self.Boton_Volver =pilas.interfaz.Boton("Regresar al Menu")
		self.Boton_Volver.y = -220 #Ubicacion del boton volver en el eje y
		self.Boton_Volver.x = 250 # Ubicacion del boton vovlver en el eje x
		self.Boton_Volver.conectar(self.Volver) # Conecta con la escena del menu principal
		self.puntajefinal=pilas.actores.Texto(str(self.puntaje.valor)) # Nos muestra el puntaje de respuestas correctas
		self.puntajefinal.escala=2 # Tamaño del puntaje correcto
		self.cartelfelicidades=pilas.actores.Texto("FELICIDADES " +self.nombre+ " has ganado") # Nos muestra un mensaje con el nombre del jugador
		self.cartelfelicidades.y=200 # Ubicacion del mensaje de texto en el eje y
		self.cartelfelicidades=pilas.actores.Texto("GRACIAS POR JUGAR NUESTRO JUEGO MATEMATICO") # Nos muestra un texto en la escena
		self.cartelfelicidades.y=100 # Ubicacion del texto en el eje y
		self.cartelpuntaje=pilas.actores.Texto(self.nombre+ " tu puntaje es: ") # Nos muestra el nombre del jugar y su puntaje obtenido
		self.cartelpuntaje.x=-150 # Ubicacion del texto de puntaje en el eje x
		self.errorestotales=pilas.actores.Texto(str(self.error.valor)) # Nos muestra el puntaje de respuestas incorrectas
		self.errorestotales.y=-100 # Ubicacion del puntaje incorrecto en el eje y
		self.errorestotales.escala=2 # Tamaño del puntaje
		self.cartelerror=pilas.actores.Texto(self.nombre+" tus errores son: ") # Nos muestra el nombre del jugar y su puntaje obtenido
		self.cartelerror.x=-150 # Ubicacion del texto de puntaje en el eje x
		self.cartelerror.y=-100 # Ubicacion del texto de puntaje en el eje y
		sonido = pilas.sonidos.cargar("sonidos/bien.wav") # Carga un sonido al juego
		sonido.reproducir() # Reproduce un sonido cuando respondes bien la pregunta
		self.mono.x=[0,200],1 # Corre automaticamente al lado derecho el personaje
		self.cartelfelicidades=pilas.actores.Texto("Autor: Maximo Abel Paute Jumbo") # Nos muestra un texto en la escena
		self.cartelfelicidades.y=-180 # Ubicacion del texto en el eje y
		self.cartelfelicidades=pilas.actores.Texto("2017 - 2018") # Nos muestra un texto en la escena
		self.cartelfelicidades.y=-210 # Ubicacion del texto en el eje y


	def perdiste(self): # Funcion cuando se pierde el juego
		actores = pilas.actores.listar_actores() # Obtiene todos los actores de la pantalla

    # Elimina todos los actores excepto el fondo y el puntaje
		for actor in actores:
			if actor not in [self.mono]:
				actor.eliminar()
		self.fondo = self.pilas.fondos.Fondo("imagenes/fondopantalla.png")#cargo un fondo para mi menu
		self.Boton_Volver =pilas.interfaz.Boton("Regresar al Menu")
		self.Boton_Volver.y = -220 #Ubicacion del boton volver en el eje y
		self.Boton_Volver.x = 250 # Ubicacion del boton vovlver en el eje x
		self.Boton_Volver.conectar(self.Volver) # Conecta con la escena del menu principal
		self.puntajefinal=pilas.actores.Texto(str(self.puntaje.valor)) # Nos muestra el puntaje de respuestas correctas
		self.puntajefinal.escala=2 # Tamaño del puntaje correcto
		self.cartelfelicidades=pilas.actores.Texto(" PERDISTE " +self.nombre+ " INTENTALO DE NUEVO") # Nos muestra un mensaje con el nombre del jugador
		self.cartelfelicidades.y=175 # Ubicacion del mensaje de texto en el eje y
		self.cartelfelicidades=pilas.actores.Texto("GRACIAS POR JUGAR NUESTRO JUEGO MATEMATICO") # Nos muestra un texto en la escena
		self.cartelfelicidades.y=100 # Ubicacion del texto en el eje y
		self.cartelpuntaje=pilas.actores.Texto(self.nombre+ " tu puntaje es: ") # Nos muestra el nombre del jugar y su puntaje obtenido
		self.cartelpuntaje.x=-150 # Ubicacion del texto de puntaje en el eje x
		self.errorestotales=pilas.actores.Texto(str(self.error.valor)) # Nos muestra el puntaje de respuestas incorrectas
		self.errorestotales.y=-100 # Ubicacion del puntaje incorrecto en el eje y
		self.errorestotales.escala=2 # Tamaño del puntaje
		self.cartelerror=pilas.actores.Texto(self.nombre+" tus errores son: ") # Nos muestra el nombre del jugar y su puntaje obtenido
		self.cartelerror.x=-150 # Ubicacion del texto de puntaje en el eje x
		self.cartelerror.y=-100 # Ubicacion del texto de puntaje en el eje y
		sonido = pilas.sonidos.cargar("sonidos/burla.wav") # Carga un sonido al juego
		sonido.reproducir() # Reproduce un sonido cuando responde mal una pregunta
		self.mono.x=[0,200],1 # Corre automaticamente al lado derecho el personaje
		self.cartelfelicidades=pilas.actores.Texto("Autor: Maximo Abel Paute Jumbo") # Nos muestra un texto en la escena
		self.cartelfelicidades.y=-175 # Ubicacion del texto en el eje y
		self.cartelfelicidades=pilas.actores.Texto("2017 - 2018") # Nos muestra un texto en la escena
		self.cartelfelicidades.y=-210 # Ubicacion del texto en el eje y
		
		# Boton para intentar de nuevo la escena perdida
		self.Boton_Creditos =pilas.interfaz.Boton("Intentar de nuevo") # Muestra el nombre en el boton
		self.Boton_Creditos.y = -220 # Ubicacion del boton en el eje y
		self.Boton_Creditos.x = -250 # Ubicacion del boton en el eje x
		self.Boton_Creditos.conectar(self.Creditos) # Conectar a la escena enlazada

	def Creditos(self): # Funcion para ir a la escena creditos
		pilas.escenas.EscenaSumaResta() # Se llama  a la escena enlazada
	

	def Volver(self): # Funcion para volver a la escena del menu principal
		pilas.escenas.EscenaMenu() # Sellama a la escena enlazada

	def actualizar(self): # Funcion que actualiza los objetos en la pantalla del juego
		pass


	def el_mono_come(self, aceitunas, mono): # Funciona que evalua la respuesta
		if not aceitunas.esverdadera: #aceitunas es la aceituna colisionada
			if self.error.valor<2: # Si la respuesta no es correcta acumula un punto incorrecto
				pilas.camara.vibrar() # Vibra la pantalla cuando responde mal
				aceitunas.eliminar() # Se elimina el actor de la respuesta seleccionada
				sonido = pilas.sonidos.cargar("sonidos/burla.wav") # Carga un sonido al juego
				sonido.reproducir() # Reproduce un sonido cuando respondes mal la pregunta
				mono.decir("Incorrecto!!! " + self.nombre + " No te rindas sigue avanzando")
				self.mono.x=[0,200],1 # Corre automaticamente al lado derecho el personaje
				self.error.aumentar() #aumenta 1 error. En total puede ser hasta 3 errores.
				pilas.tareas.agregar(3, self.Reiniciar) # Se reinicia y vuelve aparecer las tres respuestas

			else:# Si llega al limite termina el juego y pierdes
				pilas.avisar("Fin del juego") # Termina el juego
				self.error.aumentar() # Aumenta el puntaje en puntos incorrectos
				self.perdiste() # Termina y pierdes el juego

		else:
			if self.puntaje.valor<9: # Limite del puntaje para ganar el juego
				aceitunas.eliminar() #hay que eliminar la aceituna colisionada
				mono.rotacion=[0,360] # Cuando se responde bien la pregunta el personaje gira para celebrar
				sonido = pilas.sonidos.cargar("sonidos/bien.wav") # Carga un sonido al juego
				sonido.reproducir() # Reproduce un sonido cuando respondes bien una pregunta
				mono.decir("Correcto!!! " + self.nombre + " sigue avanzando")
				self.mono.x=[0,200],1 # Corre automaticamente al lado derecho el personaje
				estrella = pilas.actores.Estrella() # Muestra una estrella al responder bien la respuesta
				estrella.x = aceitunas.x # Ubicacion de la estrella encima de la respuesta correcta en el eje x
				estrella.y = aceitunas.y # Ubicacion de la estrella encima de la respuesta correcta en el eje y
				estrella.escala = 0.2 # Tamaño de la estrella
				estrella.escala = [2, 1] * 2 # Tamaño de la estrella al hacer zoom
				self.puntaje.aumentar() # Aumenta el puntaje en correcto
				pilas.tareas.agregar(3, self.Reiniciar) # Se reinicia y vuelve aparecer las tres respuestas
			else: # Si llega al limite termina el juego y ganas el juego
				pilas.avisar("Felicidades has ganado") # Muestra un mensaje que has ganado
				self.puntaje.aumentar() # Aumenta el puntaje en puntos incorrectos
				self.ganaste() # Termina y ganas el juego



	def Volver(self): # Funcion para volver a la escena enlazada
		pilas.escenas.EscenaMenu() # Se llama a la escena enlazada

	def actualizar(self): # Funcion que actualiza los objetos en la pantalla del juego
		pass
		
# ----------------------------------------------------- FIN: ESCENA DE MULTIPLICACIONES Y DIVISIONES ------------------------------------------------- #

# ----------------------------------------------------- INICIO: ESCENA DE OPERACIONES COMBINADAS ------------------------------------------------- #
		
class EscenaOperacionesCombinadas(pilasengine.escenas.Escena): # Clase para crear la escena de operaciones combinadas
	def iniciar(self): # Se inicia la clase
		self.nombre=raw_input("INGRESA TU NOMBRE PARA JUGAR: ") # Esta funcion nos pedira el nombre para jugar
		self.lista=[["Cuanto es 15 - 3 * 2 / 2 =?:", "12", "18", "27"],["Cuanto es 20 + 5 - 3 * 3 =?:", "16", "37", "53"],
					["Cuanto es 2 * 2 - 2 / 2 =?:", "3", "10", " 14"],["Cuanto es 18 + 5 - 13 =?:", "10", "25", "36"],
					["Cuanto es 3 * 4 / 3 =?:", "4", "26", "8"],["Cuanto es 11 + 2 - 3 * 4 =?:", "1", "14", "27"],
					["Cuanto es 2 + 3 * 5 =?:", "17", "29", "14"],["Cuanto 14 - 3 * 2 / 1 =?:", "8", "27", "12"],
					["Cuanto es 1 + 2 * 3 =?:", "7", "22", "33"],["Cuanto es 17 - 5 + 3 * 2 =?:", "18", "22", "34"],
					["Cuanto es 2 (3 + 5) =?:", "16", "37", "23"],["Cuanto es (10 + 5 ) * 2 =?:", "30", "18", "10"],
					["Cuanto es 2 * 3 + 2 * 5=?:","16", "22", "18"],["Cuanto es 6 * 3 / 9 - 2 =?:", "0", "15", "19"],
					["Cuanto es 5 * (3 + 4) =?:","35", "42","18"],["Cuanto es 3 * 5 - 3 + 5 =?:", "17", "23", "8"],
					["Cuanto es 1 + 1 * 1 / 1 - 1 =?:", "1", "6", "2"],["Cuanto es 2 * 1 + 3 *4 ?:","14","8","23"],
					["Cuanto es 6 * (2 + 6)?:","48","79","37"],["Cuanto es 17 - 5 + 3 * 2=?:", "18", "57", "23"]]

		self.fondo = self.pilas.fondos.Fondo("imagenes/fondopantalla.png") # Cargo una imagen de fondo a mi escena
		
		# Color del puntaje que aumenta puntos correctos
		self.puntaje = pilas.actores.Puntaje(color="blanco") # Color del texto
		self.puntaje.x = -150 # Ubicacion del puntaje en el eje x
		self.puntaje.y = -190 # Ubicacion del puntaje en el eje y
		self.puntaje.valor = 0 # Inicia en cero el puntaje
		self.correctosaparecer=pilas.actores.Texto("Correctos: ")
		self.correctosaparecer.x=-220 # Ubicacion del puntaje que muestra en el eje x
		self.correctosaparecer.y=-190 # Ubicacion del puntaje que muestra en el eje y
		
		# Color del puntaje que aumenta puntos incorrectos
		self.error=pilas.actores.Puntaje(color="rojo") # Color del texto
		self.error.valor=0 # Inicia el puntaje en cero
		self.error.x=-150 # Ubicacion del puntaje en el eje x
		self.error.y=-220 # Ubicacion del puntaje en el eje y
		self.incorrectosaparecer=pilas.actores.Texto("Incorrectos: ")
		self.incorrectosaparecer.x=-230 # Ubicacion del puntaje que muestra en el eje x
		self.incorrectosaparecer.y=-220 # Ubicacion del puntaje que muestra en el eje y

		self.mono = pilas.actores.Mono()
		self.mono.escala = 0.8 # Tamaño del personaje
		self.mono.aprender('arrastrable') # Arrastra al personaje
		self.mono.aprender('MoverseConElTeclado')
		self.mono.decir("Bienvenido/a "+ self.nombre + " Juguemos... arrastrarme a la respuesta correcta") # Muestra el personaje un mensaje de bienvenida al jugador
		self.mono.x=[0,200],1 # Corre automaticamente al lado derecho luego de responder una pregunta
		
		# Boton para regresar al menu principal
		self.Boton_Volver =pilas.interfaz.Boton("Regresar al Menu") # Muestra el texto en el boton
		self.Boton_Volver.y = -220 # Ubicacion del boton en el eje y
		self.Boton_Volver.x = 250 # Ubicacion del boton en el eje x
		self.Boton_Volver.conectar(self.Volver) # Conecta con la escena enlazada
		
		# Boton para intentar de nuevo la escena perdida
		self.Boton_Creditos =pilas.interfaz.Boton("Ir a Creditos") # Muestra el nombre en el boton
		self.Boton_Creditos.y = -220 # Ubicacion del boton en el eje y
		self.Boton_Creditos.x = 143 # Ubicacion del boton en el eje x
		self.Boton_Creditos.conectar(self.Creditos) # Conecta con la escena enlazada


		#Agrego las colisiones
		pilas.colisiones.agregar('aceituna', 'mono', self.el_mono_come)#añadido

		#Agrego tarea o las respuestas
		pilas.tareas.agregar(3, self.Preguntando)
		

	def Reiniciar(self):
    # Obtiene todos los actores de la pantalla.
		actores = pilas.actores.listar_actores()

    # Elimina todos los actores excepto el fondo y el puntaje
		for actor in actores:
			if actor not in [self.puntaje, self.fondo, self.mono,self.error,self.correctosaparecer,self.incorrectosaparecer,self.Boton_Volver]:
				actor.eliminar()

    # Genera una pregunta nueva
		self.Preguntando()
		
		# Boton para ir a la escena creditos
		self.Boton_Creditos =pilas.interfaz.Boton("Ir a Creditos") # Muestra el nombre en el boton
		self.Boton_Creditos.y = -220 # Ubicacion del boton en el eje y
		self.Boton_Creditos.x = 143 # Ubicacion del boton en el x
		self.Boton_Creditos.conectar(self.Creditos) # Conecta con la escena enlazada


	# Ubicacion de las respuestas generadas
	def Preguntando(self): # Funcion que muestra la respuestas
		self.b1=pilas.actores.Aceituna() # Primera respuesta
		self.b1.x=-275 #Ubicacion de respuesta en eje x
		self.b1.y=100 #Ubicacion de respuesta en eje y
		self.b1.esverdadera=False
		self.b2=pilas.actores.Aceituna() # Segunda respuesta
		self.b2.x=-275 #Ubicacion de respuesta en eje x
		self.b2.y=0 #Ubicacion de respuesta en eje y
		self.b2.esverdadera=False
		self.b3=pilas.actores.Aceituna() # Tercera respuesta
		self.b3.x=-275 #Ubicacion de respuesta en eje x
		self.b3.y=-100 #Ubicacion de respuesta en eje y
		self.b3.esverdadera=False

		# Numero de preguntas agregadas
		self.poslista=pilas.azar(0,19) # Limite de las preguntas
		self.encuentrapreg=self.lista[self.poslista][0] # Comienza a generar las preguntas desde la primera
		self.mostrar_pregunta=pilas.actores.Texto(self.encuentrapreg) # Nos muestra la primera pregunta 
		self.mostrar_pregunta.y=210 # Ubicacion de la pregunta en el eje y
		self.mostrar_pregunta.escala=0.8 # Nos muestra la tamaño de letra de la pregunta

		# Ubicacion de la respuesta correcta de las preguntas
		self.respuesta_correcta = self.lista[self.poslista][1] #Respuesta Correcta
		self.respuesta_incorrecta_1 = self.lista[self.poslista][2] #Respuesta incorrecta 1
		self.respuesta_incorrecta_2 = self.lista[self.poslista][3] #Respuesta incorrecta 2

		# Ubicacion de las respuestas de las preguntas a responder
		self.rta_1 = pilas.actores.Texto("")
		self.rta_1.x=-230 # Ubicacion de la primera pregunta en el eje x
		self.rta_1.y=100  # Ubicacion de la primera pregunta en el eje y
		self.rta_2 = pilas.actores.Texto("")
		self.rta_2.x=-230 # Ubicacion de la segunda pregunta en el eje x
		self.rta_2.y=0 # Ubicacion de la segunda pregunta en el eje y
		self.rta_3 = pilas.actores.Texto("")
		self.rta_3.x=-230 # Ubicacion de la tercera pregunta en el eje x
		self.rta_3.y=-100 # Ubicacion de la tercera pregunta en el eje y

		#Aceitunas verdadera
		self.aceitunas_posibles = [self.b1,self.b2,self.b3]
		self.textos_posibles = [self.rta_1,self.rta_2,self.rta_3]
		self.indiceok=pilas.azar(0,2) # Que alguna de las tres respuestas son correctas
		self.aceituna_verdadera=self.aceitunas_posibles[self.indiceok]
		self.aceituna_verdadera.esverdadera=True
		self.texto_respuesta_verdadera=self.textos_posibles[self.indiceok]
		self.texto_respuesta_verdadera.texto=str(self.respuesta_correcta)
		
		# Condiciones de la respuesta correcta va preguntando cuando es la verdadera
		if self.b1.esverdadera: # Nos muestra aletoriamente las respuesta correcta
			self.rta_1.texto=str(self.respuesta_correcta) # Respuesta correcta
			self.rta_2.texto = str(self.respuesta_incorrecta_1)
			self.rta_3.texto = str(self.respuesta_incorrecta_2)
		elif self.b2.esverdadera:
			self.rta_2.texto=str(self.respuesta_correcta) # Respuesta correcta
			self.rta_1.texto = str(self.respuesta_incorrecta_1)
			self.rta_3.texto = str(self.respuesta_incorrecta_2)
		elif self.b3.esverdadera:
			self.rta_3.texto= str(self.respuesta_correcta) # Respuesta correcta
			self.rta_1.texto = str(self.respuesta_incorrecta_1)
			self.rta_2.texto = str(self.respuesta_incorrecta_2)

	def ganaste(self): # Funcion cuando se gana el juego
		actores = pilas.actores.listar_actores() # Obtiene todos los actores de la pantalla

    # Elimina todos los actores excepto el fondo y el puntaje
		for actor in actores:
			if actor not in [self.mono]:
				actor.eliminar()
		self.fondo = self.pilas.fondos.Fondo("imagenes/fondopantalla.png")#cargo un fondo para mi menu
		self.Boton_Volver =pilas.interfaz.Boton("Regresar al Menu")
		self.Boton_Volver.y = -220 #Ubicacion del boton volver en el eje y
		self.Boton_Volver.x = 250 # Ubicacion del boton vovlver en el eje x
		self.Boton_Volver.conectar(self.Volver) # Conecta con la escena del menu principal
		self.puntajefinal=pilas.actores.Texto(str(self.puntaje.valor)) # Nos muestra el puntaje de respuestas correctas
		self.puntajefinal.escala=2 # Tamaño del puntaje correcto
		self.cartelfelicidades=pilas.actores.Texto("FELICIDADES " +self.nombre+ " has ganado") # Nos muestra un mensaje con el nombre del jugador
		self.cartelfelicidades.y=200 # Ubicacion del mensaje de texto en el eje y
		self.cartelfelicidades=pilas.actores.Texto("GRACIAS POR JUGAR NUESTRO JUEGO MATEMATICO") # Nos muestra un texto en la escena
		self.cartelfelicidades.y=100 # Ubicacion del texto en el eje y
		self.cartelpuntaje=pilas.actores.Texto(self.nombre+ " tu puntaje es: ") # Nos muestra el nombre del jugar y su puntaje obtenido
		self.cartelpuntaje.x=-150 # Ubicacion del texto de puntaje en el eje x
		self.errorestotales=pilas.actores.Texto(str(self.error.valor)) # Nos muestra el puntaje de respuestas incorrectas
		self.errorestotales.y=-100 # Ubicacion del puntaje incorrecto en el eje y
		self.errorestotales.escala=2 # Tamaño del puntaje
		self.cartelerror=pilas.actores.Texto(self.nombre+" tus errores son: ") # Nos muestra el nombre del jugar y su puntaje obtenido
		self.cartelerror.x=-150 # Ubicacion del texto de puntaje en el eje x
		self.cartelerror.y=-100 # Ubicacion del texto de puntaje en el eje y
		sonido = pilas.sonidos.cargar("sonidos/bien.wav") # Carga un sonido al juego
		sonido.reproducir() # Reproduce un sonido cuando respondes bien la pregunta
		self.mono.x=[0,200],1 # Corre automaticamente al lado derecho el personaje
		self.cartelfelicidades=pilas.actores.Texto("Autor: Maximo Abel Paute Jumbo") # Nos muestra un texto en la escena
		self.cartelfelicidades.y=-180 # Ubicacion del texto en el eje y
		self.cartelfelicidades=pilas.actores.Texto("2017 - 2018") # Nos muestra un texto en la escena
		self.cartelfelicidades.y=-210 # Ubicacion del texto en el eje y


	def perdiste(self): # Funcion cuando se pierde el juego
		actores = pilas.actores.listar_actores() # Obtiene todos los actores de la pantalla

    # Elimina todos los actores excepto el fondo y el puntaje
		for actor in actores:
			if actor not in [self.mono]:
				actor.eliminar()
		self.fondo = self.pilas.fondos.Fondo("imagenes/fondopantalla.png")#cargo un fondo para mi menu
		self.Boton_Volver =pilas.interfaz.Boton("Regresar al Menu")
		self.Boton_Volver.y = -220 #Ubicacion del boton volver en el eje y
		self.Boton_Volver.x = 250 # Ubicacion del boton vovlver en el eje x
		self.Boton_Volver.conectar(self.Volver) # Conecta con la escena del menu principal
		self.puntajefinal=pilas.actores.Texto(str(self.puntaje.valor)) # Nos muestra el puntaje de respuestas correctas
		self.puntajefinal.escala=2 # Tamaño del puntaje correcto
		self.cartelfelicidades=pilas.actores.Texto(" PERDISTE " +self.nombre+ " INTENTALO DE NUEVO") # Nos muestra un mensaje con el nombre del jugador
		self.cartelfelicidades.y=175 # Ubicacion del mensaje de texto en el eje y
		self.cartelfelicidades=pilas.actores.Texto("GRACIAS POR JUGAR NUESTRO JUEGO MATEMATICO") # Nos muestra un texto en la escena
		self.cartelfelicidades.y=100 # Ubicacion del texto en el eje y
		self.cartelpuntaje=pilas.actores.Texto(self.nombre+ " tu puntaje es: ") # Nos muestra el nombre del jugar y su puntaje obtenido
		self.cartelpuntaje.x=-150 # Ubicacion del texto de puntaje en el eje x
		self.errorestotales=pilas.actores.Texto(str(self.error.valor)) # Nos muestra el puntaje de respuestas incorrectas
		self.errorestotales.y=-100 # Ubicacion del puntaje incorrecto en el eje y
		self.errorestotales.escala=2 # Tamaño del puntaje
		self.cartelerror=pilas.actores.Texto(self.nombre+" tus errores son: ") # Nos muestra el nombre del jugar y su puntaje obtenido
		self.cartelerror.x=-150 # Ubicacion del texto de puntaje en el eje x
		self.cartelerror.y=-100 # Ubicacion del texto de puntaje en el eje y
		sonido = pilas.sonidos.cargar("sonidos/burla.wav") # Carga un sonido al juego
		sonido.reproducir() # Reproduce un sonido cuando responde mal una pregunta
		self.mono.x=[0,200],1 # Corre automaticamente al lado derecho el personaje
		self.cartelfelicidades=pilas.actores.Texto("Autor: Maximo Abel Paute Jumbo") # Nos muestra un texto en la escena
		self.cartelfelicidades.y=-175 # Ubicacion del texto en el eje y
		self.cartelfelicidades=pilas.actores.Texto("2017 - 2018") # Nos muestra un texto en la escena
		self.cartelfelicidades.y=-210 # Ubicacion del texto en el eje y
		
		# Boton para intentar de nuevo la escena perdida
		self.Boton_Creditos =pilas.interfaz.Boton("Intentar de nuevo") # Muestra el texto en el boton
		self.Boton_Creditos.y = -220 # Ubicacion del boton en el eje y
		self.Boton_Creditos.x = -250 # Ubicacion del boton en el eje x
		self.Boton_Creditos.conectar(self.Creditos) # Conecta con la escena enlazada

	def Creditos(self): # Funcion para intentar de nuevo la escena operaciones combinadas
		pilas.escenas.EscenaOperacionesCombinadas() # Se llama  a la funcion enlazada


	def Volver(self): # Funcion para volver a la escena enlazada
		pilas.escenas.EscenaMenu() # Se llama a la escena enlazada

	def actualizar(self): # Funcion que actualiza los objetos en la pantalla del juego
		pass


	def el_mono_come(self, aceitunas, mono): # Funciona que evalua la respuesta
		if not aceitunas.esverdadera: #aceitunas es la aceituna colisionada
			if self.error.valor<2: # Si la respuesta no es correcta acumula un punto incorrecto
				pilas.camara.vibrar() # Vibra la pantalla cuando responde mal
				aceitunas.eliminar() # Se elimina el actor de la respuesta seleccionada
				sonido = pilas.sonidos.cargar("sonidos/burla.wav") # Carga un sonido al juego
				sonido.reproducir() # Reproduce un sonido cuando respondes mal la pregunta
				mono.decir("Incorrecto!!! " + self.nombre + " No te rindas sigue avanzando")
				self.mono.x=[0,200],1 # Corre automaticamente al lado derecho el personaje
				self.error.aumentar() #aumenta 1 error. En total puede ser hasta 3 errores.
				pilas.tareas.agregar(3, self.Reiniciar) # Se reinicia y vuelve aparecer las tres respuestas

			else:# Si llega al limite termina el juego y pierdes
				pilas.avisar("Fin del juego") # Termina el juego
				self.error.aumentar() # Aumenta el puntaje en puntos incorrectos
				self.perdiste() # Termina y pierdes el juego

		else:
			if self.puntaje.valor<9: # Limite del puntaje para ganar el juego
				aceitunas.eliminar() #hay que eliminar la aceituna colisionada
				mono.rotacion=[0,360] # Cuando se responde bien la pregunta el personaje gira para celebrar
				sonido = pilas.sonidos.cargar("sonidos/bien.wav") # Carga un sonido al juego
				sonido.reproducir() # Reproduce un sonido cuando respondes bien una pregunta
				mono.decir("Correcto!!! " + self.nombre + " sigue avanzando")
				self.mono.x=[0,200],1 # Corre automaticamente al lado derecho el personaje
				estrella = pilas.actores.Estrella() # Muestra una estrella al responder bien la respuesta
				estrella.x = aceitunas.x # Ubicacion de la estrella encima de la respuesta correcta en el eje x
				estrella.y = aceitunas.y # Ubicacion de la estrella encima de la respuesta correcta en el eje y
				estrella.escala = 0.2 # Tamaño de la estrella
				estrella.escala = [2, 1] * 2 # Tamaño de la estrella al hacer zoom
				self.puntaje.aumentar() # Aumenta el puntaje en correcto
				pilas.tareas.agregar(3, self.Reiniciar) # Se reinicia y vuelve aparecer las tres respuestas
			else: # Si llega al limite termina el juego y ganas el juego
				pilas.avisar("Felicidades has ganado") # Muestra un mensaje que has ganado
				self.puntaje.aumentar() # Aumenta el puntaje en puntos incorrectos
				self.ganaste() # Termina y ganas el juego



	def Volver(self): # Funcion para volver a la escena enlazada
		pilas.escenas.EscenaMenu() # Se llama a la escena enlazada

	def actualizar(self): # Funcion que actualiza los objetos en la pantalla del juego
		pass
		
# ----------------------------------------------------- FIN: ESCENA DE OPERACIONES COMBINADAS ------------------------------------------------- #

# Se vinculan las escenas creadas.
pilas.escenas.vincular(EscenaSumaResta)
pilas.escenas.vincular(EscenaMultiplicacionDivision)
pilas.escenas.vincular(EscenaOperacionesCombinadas)
pilas.escenas.vincular(InicioJuego)
pilas.escenas.vincular(EscenaAyuda)
pilas.escenas.vincular(EscenaCreditos)
pilas.escenas.vincular(EscenaMenu)
pilas.escenas.vincular(EscenaOperaciones)

pilas.escenas.InicioJuego() # Escena en la cual inicia el juego.

pilas.ejecutar() # Permite ejecutar el juego
