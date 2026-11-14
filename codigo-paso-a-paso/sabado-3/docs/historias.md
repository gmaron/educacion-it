# Historias

Vienen del tablero del sábado 1. Los criterios de aceptación son casos de `especificacion.md`. La definición de terminado está en `CLAUDE.md`.

## H1 · Saber quién le transfiere a quién
- **Como** alguien que salió a comer con amigos
- **quiero** saber quién le transfiere a quién y cuánto
- **para** quedar a mano sin hacer cuentas.
- **Requisitos:** R1, R2
- **Criterios de aceptación:** C1, C2, C3, C4, C5, C6, C7, C8
- **Estado:** Hecho

## H2 · Ver las cuentas antes de las transferencias
- **Como** alguien que tiene que pagar
- **quiero** ver cómo se calculó lo que me toca
- **para** confiar en el número.
- **Requisitos:** R3
- **Criterios de aceptación:** C3
- **Estado:** Hecho

## H3 · Que no se cuele un dato mal cargado
- **Como** quien carga los gastos
- **quiero** que el programa me avise si me equivoqué
- **para** no repartir mal la plata.
- **Requisitos:** R4
- **Criterios de aceptación:** C9, C10
- **Estado:** Hecho

## H4 · Distinguir a dos personas con el mismo nombre
- **Como** alguien que tiene dos amigas que se llaman Ana
- **quiero** que cada una tenga su cuenta
- **para** saber cuál le paga a cuál.
- **Requisitos:** R1
- **Criterios de aceptación:** C11
- **Estado:** Hecho

## H5 · Cargar los montos con coma
- **Como** quien carga los gastos
- **quiero** escribir los montos con coma, como en el ticket
- **para** no tener que pasarlos a punto.
- **Requisitos:** R6
- **Criterios de aceptación:** C12, C13
- **Estado:** Hecho

## H6 · Ver de un vistazo quién debe
- **Como** alguien que mira la pantalla
- **quiero** ver en rojo a los que deben y en verde a los que pagaron de más
- **para** encontrarme rápido.
- **Requisitos:** R5
- **Criterios de aceptación:** C14
- **Estado:** Hecho

## H7 · Repartir la cuenta desde otra app
- **Como** alguien que quiere usar el divisor desde una página
- **quiero** mandarle los pagos por HTTP y recibir las transferencias y el estado de cada uno
- **para** no depender de la terminal.
- **Requisitos:** R7, R8
- **Criterios de aceptación:** C17, C18, C19
- **Estado:** Hecho

## H8 · Repartir el asado en una pantalla
- **Como** quien hizo el asado
- **quiero** cargar lo que puso cada uno en una página y ver quién le transfiere a quién
- **para** pasarle el resultado a todos sin abrir la terminal.
- **Requisitos:** R9
- **Criterios de aceptación:** [NO COMPROBABLE con pytest]
- **Estado:** En curso