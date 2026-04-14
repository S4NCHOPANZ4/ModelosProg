# Proyectos Modelos de Programación

Participantes grupo:
- Juan David Buitrago - 20242020194
- Andrés Felipe Preciado Castilla - 20241020158

## 1. Modelado De Grupo Musical

```mermaid
classDiagram

%% Interfaz
class Ejecutar {
  <<interface>>
  +tocar() void
  +afinar() void
}

%% Clase abstracta
class Musico {
  <<abstract>>
  -nombre: String
  -edad: int
  +getNombre() String
  +tocar() void
  +afinar() void
  +presentarse() String
}

%% Clases concretas
class Instrumentista {
  -instrumento: Instrumento
  -calidad: int
  +tocar() void
  +afinar() void
  +getInstrumento() Instrumento
}

class Cantante {
  -tesitura: String
  +tocar() void
  +afinar() void
}

class Instrumento {
  -nombre: String
  -tipo: TipoInstrumento
  -marca: String
  +getNombre() String
  +getTipo() Instrumento
}

class Agrupacion {
  -nombre: String
  -genero: String
  -miembros: List~Musico~
  +agregarMiembro(m: Musico) void
  +retirarMiembro(m: Musico) void
  +getMusicos() List~Musico~
}

class Evento {
  -lugar: String
  -fecha: String
  -entretenimiento: Agrupacion
  -aforo: int
  +registrarAgrupacion(a: Agrupacion) void
  +cancelarEvento() void
  +getFecha() LocalDate
  +getLugar() String
}

%% Relaciones
Ejecutar <|.. Musico
Musico <|-- Instrumentista
Musico <|-- Cantante

Instrumentista *-- Instrumento
Agrupacion o-- Musico
Evento --* Agrupacion

```
## 2. Composite - Árbol de Operaciones

```mermaid
classDiagram

class Expression {
  <<abstract>>
  +evaluate(): float*
}

class NodeNum{
    +value: float
    +init(value: float)
    +evaluate(): float
}

class OperatorNode{
    +OPERATORS : dict
    +op : str
    +left : Expression
    +right : Expression
    +init(op: str, left: Expression, right: Expression)
    +evaluate() : float
}

%%Relaciones
Expression <|-- NodeNum : es un
Expression <|-- OperatorNode : es un

Expression --o OperatorNode : left
Expression --o OperatorNode : right

```

