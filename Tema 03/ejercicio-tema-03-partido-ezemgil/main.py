from Equipo import Equipo
from Partido import Partido

def main():
    river = Equipo("River")
    boca = Equipo("Boca")
    independiente = Equipo("Independiente")

    p1 = Partido(river, boca, 2, 1)
    p2 = Partido(boca, independiente, 0, 0)
    p3 = Partido(independiente, river, 3, 2)

    print(p1)
    print(p2)
    print(p3)
    
    print(river)
    print(boca)
    print(independiente)


if __name__ == '__main__':
    main()