class Partido:
    def __init__(self, local, visitante, goles_local, goles_visitante):
        self.local = local
        self.visitante = visitante
        self.goles_local = goles_local
        self.goles_visitante = goles_visitante

        local.registrar_partido(self, es_local=True)
        visitante.registrar_partido(self, es_local=False)

    def ganador(self):
        if self.goles_local > self.goles_visitante:
            return self.local
        elif self.goles_visitante > self.goles_local:
            return self.visitante
        else:
            return None

    def __str__(self):
        return (f"{self.local.nombre} {self.goles_local} - "
                f"{self.goles_visitante} {self.visitante.nombre}")
