# Simulador de Ruleta

Desarrollar un programa que simule el juego de la ruleta.
Para ello generar al azar 1000 tiradas y luego informar:
- Cantidad de pares e impares
- Cantidad de tiradas por cada docena
- Porcentaje de ceros sobre el total de jugadas
- Cantidad de rojos y negros

***

## Supuestos
- La ruleta a simular tiene 37 números, que van del 0 al 36. El 00 se ha excluido.
- Las tiradas son independientes y equiprobables.
- Un número es negro si su reducción es un número par, a excepción del 10 y 28.
    - Si la reducción del número no es par, entonces el número es rojo, a excepción del 0, que siempre se considera verde.
    > [!NOTE]
    > La reducción de un número consiste en sumar sus dígitos repetidamente hasta obtener un solo dígito. Por ejemplo, la reducción del 36 es 9 (3 + 6 = 9).
- El cero se considera un caso especial y no es ni par ni impar.
