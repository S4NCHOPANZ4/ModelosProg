from abc import ABC, abstractmethod

# Comp base
class Expression(ABC):
    @abstractmethod
    def evaluate(self) -> float:
        pass

# Nodo (numero)
class NodeNum(Expression):
    def __init__(self,value: float):
        self.value = value
    def evaluate(self) -> float:
        return self.value

class OperatorNode(Expression):
    OPERATORS = {
        '+': lambda a, b: a + b,
        '-': lambda a, b: a - b,
        '*': lambda a, b: a * b,
        '/': lambda a, b: a / b, # b != 0
    }

    def __init__(self, op: str, left: Expression, right: Expression):
        if op not in self.OPERATORS:
            raise ValueError(f"Operador no soportado: {op} soportados + - * /")
        self.op = op
        self.left = left
        self.right = right
    
    def evaluate(self) -> float:
        left_val = self.left.evaluate()
        right_val = self.right.evaluate()
        if right_val == 0:
            raise ValueError(f"0 division not supported")
        return self.OPERATORS[self.op](left_val, right_val)

tree = OperatorNode(
    '*',
    OperatorNode('+', NodeNum(3), NodeNum(1)),
    NodeNum(2)
)

#   Arbol Ejemplo Hardcoded
#       * 
#     /    \
#   2       +
#           |  \
#           3   1 


print(tree.evaluate())