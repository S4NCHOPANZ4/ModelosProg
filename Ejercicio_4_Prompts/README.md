# Sistema de Procesamiento de Pagos (Design Patterns Demo)

Este proyecto ejemplifica la implementación y las diferencias clave entre dos de los patrones de diseño más importantes: **Template Method** y **Strategy**, utilizando Python.

## 🚀 Propósito del Proyecto
El objetivo es demostrar cómo estos dos patrones pueden coexistir en una misma arquitectura:
- **Template Method**: Define el esqueleto del flujo de una orden de compra (validación -> pago -> notificación).
- **Strategy**: Permite intercambiar el método de pago (PayPal, Tarjeta de Crédito) de forma dinámica sin alterar el flujo principal.

## 🛠️ Estructura del Código
El proyecto se divide en:
1.  **`PaymentStrategy` (Interfaz Strategy)**: Define el contrato para los métodos de pago.
2.  **Estrategias Concretas**: `CreditCardStrategy` y `PayPalStrategy`.
3.  **`OrderProcessor` (Clase Base Template)**: Define el orden de los pasos del algoritmo.
4.  **Implementaciones de Plantilla**: `DigitalOrder` y `PhysicalOrder` (uso de *hooks*).

## 📜 Historial de Prompts (Evolution Log)

Este proyecto fue desarrollado de forma iterativa siguiendo este flujo de diseño:

1.  **Prompt de Concepto:**
    > "Haciendo uso de python genérame ejemplo gráfico (proycto en codigo) que demuestre las diferencias entre los patrones Strategy y Template Method"
    * *Resultado:* Definición técnica de las bases: **Herencia** para Template Method vs. **Composición** para Strategy.

2.  **Prompt de Consolidación:**
    > "dame un proyecto completo que ejemplifique su uso y funcionamiento"
    * *Resultado:* Creación del sistema integrado de pagos donde el *Template Method* actúa como orquestador y delega en una *Strategy*.

3.  **Prompt de Documentación:**
    > "para un readme pon el historico de prompts que te pedi para crear este proyecto"
    * *Resultado:* Generación de este archivo de trazabilidad para el repositorio.