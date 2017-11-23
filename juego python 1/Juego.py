
import pilasengine
import os
pilas = pilasengine.iniciar()

puntaje = pilas.actores.Puntaje(-200, 200, color=pilas.colores.blanco)


class Personaje(pilasengine.actores.Pelota):

    def iniciar(self):
        self.imagen = "Pelota.png"
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

pelota = pilas.actores.NaveRoja(y=-200)
pelota.aprender(pilas.habilidades.LimitadoABordesDePantalla)
pelota.definir_enemigos(enemigos, puntaje.aumentar)

pilas.colisiones.agregar(pelota, enemigos, pelota.eliminar)


pilas.ejecutar()
