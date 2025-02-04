from typing import Union


def process_salary(salary: Union[int, float]) -> float:
    """
    Procesa un salario que puede ser entero o flotante y lo devuelve como flotante.

    Parámetros:
    Salary (Union[int, float]): Un salario que puede ser un entero o flotante.

    Retorna:
    float: El salario procesado como flotante.
    """
    return float(salary)
