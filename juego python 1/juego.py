import pilasengine
pilas = pilasengine.iniciar()
#sonido_de_menu = pilas.sonidos.cargar('A Better Place - Playing For Change.mp3') WAV!
            
puntaje = pilas.actores.Puntaje(-200, 200, color=pilas.colores.blanco)

class Personaje(pilasengine.actores.Pelota):

    def iniciar(self):
        self.imagen = "imagenes/esfera.png"
        self.aprender( pilas.habilidades.PuedeExplotarConHumo )
        self.x = pilas.azar(-200, 200)
        self.y = 200
        self.velocidad = pilas.azar(10, 40) / 10.0

    def actualizar(self):
        self.rotacion += 4
        self.y -= self.velocidad

        # Elimina el objeto cuando sale de la pantalla.
        if self.y < -300:
            self.eliminar()
#creando fondo
fondo = pilas.fondos.Fondo()



fondo = pilas.fondos.Galaxia(dy=-10)

enemigos = pilas.actores.Grupo()

def crear_enemigo ():
    actor = Personaje(pilas)
    enemigos.agregar(actor)

pilas.tareas.siempre(0.5, crear_enemigo)

NaveRoja = pilas.actores.NaveRoja(y=-200)
NaveRoja.aprender(pilas.habilidades.LimitadoABordesDePantalla)
NaveRoja.definir_enemigos(enemigos, puntaje.aumentar)

pilas.colisiones.agregar(NaveRoja, enemigos, NaveRoja.eliminar)


pilas.ejecutar()
