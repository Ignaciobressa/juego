import pilasengine
from dragon import Dragon
pilas = pilasengine.iniciar()
          
puntaje = pilas.actores.Puntaje(-200, 200, color=pilas.colores.blanco)

class Personaje(pilasengine.actores.Actor):

    def iniciar(self):
        self.imagen = "imagenes/esfera.png"
        self.aprender( pilas.habilidades.PuedeExplotarConHumo )
        self.x = pilas.azar(-200, 200)
        self.y = 200
        self.velocidad = pilas.azar(10, 40) / 10.0

    def actualizar(self):
        self.rotacion += 10
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
#cada 0,5 crea un enemigo
pilas.tareas.siempre(0.5, crear_enemigo)

pj= Dragon(pilas)
pj.aprender(pilas.habilidades.LimitadoABordesDePantalla)
pj.escala = 0.5
pj.definir_enemigos(enemigos, puntaje.aumentar)

pilas.colisiones.agregar(pj, enemigos, pj.eliminar)
pilas.actores.vincular(Dragon)



 
        
        
        
pilas.ejecutar()
