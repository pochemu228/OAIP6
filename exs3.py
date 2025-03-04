def circuit_resistance(*resistances: int, connection: str = 'serial', conductivity: bool = False) -> float:
    if connection not in ['serial', 'parallel']:
        raise ValueError("Неверный тип соединения. Допускаются только 'serial' или 'parallel'.")

    if connection == 'serial':
        total_resistance = sum(resistances)

    elif connection == 'parallel':
        reciprocal_sum = sum(1 / r for r in resistances)
        total_resistance = 1 / reciprocal_sum if reciprocal_sum != 0 else float('inf')

    if conductivity:
        total_conductance = 1 / total_resistance if total_resistance != 0 else float('inf')
        return round(total_conductance, 4)
    else:
        return round(total_resistance, 4)

data = [10, 20, 30]
print(circuit_resistance(*data))

data_parallel = [30, 30, 30]
print(circuit_resistance(*data_parallel, connection='parallel'))

print(circuit_resistance(*data, conductivity=True))

print(circuit_resistance(*data_parallel, connection='parallel', conductivity=True))
