class Equipo:
    def __init__(self, nombre):
        self.nombre = nombre
        self.partidos_jugados = 0
        self.partidos_local = 0
        self.partidos_visitante = 0
        self.goles_a_favor = 0
        self.goles_en_contra = 0
        self.partidos_ganados = 0
        self.partidos_empatados = 0
        self.partidos_perdidos = 0
        self.puntos = 0

    def registrar_partido(self, partido, es_local):
        # Datos del partido
        if es_local:
            goles_propios = partido.goles_local
            goles_rival = partido.goles_visitante
            self.partidos_local += 1
        else:
            goles_propios = partido.goles_visitante
            goles_rival = partido.goles_local
            self.partidos_visitante += 1

        # Actualización general
        self.partidos_jugados += 1
        self.goles_a_favor += goles_propios
        self.goles_en_contra += goles_rival

        # Resultado
        if goles_propios > goles_rival:
            self.partidos_ganados += 1
            self.puntos += 3
        elif goles_propios == goles_rival:
            self.partidos_empatados += 1
            self.puntos += 1
        else:
            self.partidos_perdidos += 1

    def diferencia_goles(self):
        return self.goles_a_favor - self.goles_en_contra

    def __str__(self):
        return (f"{self.nombre} | PJ: {self.partidos_jugados}, "
                f"Local: {self.partidos_local}, Visitante: {self.partidos_visitante}, "
                f"Goles a favor: {self.goles_a_favor}, Goles en contra: {self.goles_en_contra}, "
                f"Dif: {self.diferencia_goles()}, "
                f"G: {self.partidos_ganados}, E: {self.partidos_empatados}, P: {self.partidos_perdidos}, "
                f"Puntos: {self.puntos}")