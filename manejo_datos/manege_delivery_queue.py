from collections import deque


def manage_delivery_queue() -> deque:
    # Crea una cola para gestionar entregas de productos
    delivery_queue = deque(["order_1", "order_2", "order_3"])
    delivery_queue.append("order_4")  # Agrega un nuevo pedido al final de la cola
    delivery_queue.appendleft("order_0")  # Agrega un nuevo pedido al inicio de la cola
    delivery_queue.pop()  # Elimina el último pedido de la cola
    delivery_queue.popleft()  # Elimina el primer pedido de la cola
    return delivery_queue


queue = manage_delivery_queue()
print(queue)  # Output: deque(['order_0', 'order_1', 'order_2', 'order_3', 'order_4'])
