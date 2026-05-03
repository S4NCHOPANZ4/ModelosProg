from abc import ABC, abstractmethod

# ==========================================
# PATRÓN STRATEGY (El "Cómo" se paga)
# ==========================================

class PaymentStrategy(ABC):
    @abstractmethod
    def collect_details(self):
        pass

    @abstractmethod
    def process_payment(self, amount):
        pass

class CreditCardStrategy(PaymentStrategy):
    def collect_details(self):
        print("[Strategy] Solicitando número de tarjeta y CVV...")

    def process_payment(self, amount):
        print(f"[Strategy] Pagando ${amount} con Tarjeta de Crédito (Pasarela Bancaria).")

class PayPalStrategy(PaymentStrategy):
    def collect_details(self):
        print("[Strategy] Redirigiendo a login de PayPal...")

    def process_payment(self, amount):
        print(f"[Strategy] Pagando ${amount} con PayPal (API REST).")


# ==========================================
# PATRÓN TEMPLATE METHOD (El "Flujo" de compra)
# ==========================================

class OrderProcessor(ABC):
    """Clase base que define el esqueleto del algoritmo."""
    
    def __init__(self, strategy: PaymentStrategy):
        self.payment_strategy = strategy

    # Este es el TEMPLATE METHOD
    def process_order(self, amount):
        self.validate_cart()
        # Aquí se integra la estrategia (Composición dentro de Herencia)
        self.payment_strategy.collect_details()
        self.payment_strategy.process_payment(amount)
        self.notify_customer()
        self.hook_extra_steps() # Paso opcional (Hook)

    def validate_cart(self):
        print("[Template] Validando stock y cupones...")

    def notify_customer(self):
        print("[Template] Enviando factura por correo electrónico.")

    def hook_extra_steps(self):
        """Un hook es un paso que las subclases pueden o no implementar."""
        pass

class DigitalOrder(OrderProcessor):
    """Procesamiento para productos descargables."""
    def hook_extra_steps(self):
        print("[Template - Hook] Generando enlace de descarga instantánea.")

class PhysicalOrder(OrderProcessor):
    """Procesamiento para productos que requieren envío."""
    def hook_extra_steps(self):
        print("[Template - Hook] Generando etiqueta de envío para logística.")


# ==========================================
# EJECUCIÓN DEL PROYECTO
# ==========================================

if __name__ == "__main__":
    print("--- CASO 1: Compra de Software (Digital) con PayPal ---")
    software_order = DigitalOrder(PayPalStrategy())
    software_order.process_order(49.99)

    print("\n--- CASO 2: Compra de Laptop (Física) con Tarjeta ---")
    laptop_order = PhysicalOrder(CreditCardStrategy())
    laptop_order.process_order(1200.00)

    print("\n--- CASO 3: Cambio de estrategia en caliente ---")
    # El mismo pedido físico, pero el cliente decide cambiar a PayPal a mitad de camino
    laptop_order.payment_strategy = PayPalStrategy()
    laptop_order.process_order(1200.00)