# Ejemplo de uso
W = [0.2, 0.5, 0.4, 0.7, 0.1, 0.8, 0.3, 0.9]
bin_capacity = 1
result = bin_packing_approximation(W, bin_capacity)
print(f"Contenedores utilizados: {len(result)}")
print(f"Distribución en contenedores: {result}")