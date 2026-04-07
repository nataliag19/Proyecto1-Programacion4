# Proyecto 1: Desacoplamiento de software: Principios para gestionar y aislar dependencias - Programación 4

Juan Carlos Mejía Cano\
Natalia Gallego Barrero

Docente: Alejandro Rodas Vásquez\
Universidad Tecnológica de Pereira

4 de abril del 2026

\
**Proyecto: Sistema "NutriUTP"**

La cafetería estudiantil requiere un software para administrar la entrega de almuerzos
diarios. El sistema debe gestionar un menú que cambia cada día, ofreciendo siempre una
opción vegetariana. Además, debe procesar los subsidios estudiantiles, donde el precio final
depende del perfil socioeconómico del alumno. El reto de diseño consiste en crear un sistema
donde el cambio en las reglas de negocio (ej. nuevos tipos de subsidio o cambios en los
ingredientes del menú) no obligue a reescribir todo el código, gestionando las dependencias
para que el software sea fácil de mantener y evolucionar.

\
El proyecto está organizado en múltiples archivos para garantizar la separación de responsabilidades:

📁 Proyecto\
│\
├── ClasesGenerales\
│   ├── plato.py\
│   ├── menuDelDia.py\
│   ├── comensal.py\
│   └── procesadorDeVenta.py\
│\
├── UI\
│   └── sistema.py\
│\
└── nutriUTPmain.py

\
**nutriUTPmain.py:** Inicializa el sistema y ejecuta la aplicación.
