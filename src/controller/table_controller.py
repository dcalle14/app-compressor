class TableController:
    
    def __init__(self):
        # Supongamos que tienes una lista de datos en formato [(nombre, valor), ...]
        self.data = [
            ("Elemento1", 45),
            ("Elemento2", 60),
            ("Elemento3", 30),
            ("Elemento4", 75)
        ]

    def get_data(self):
        return self.data

    def filter_data_by_value(self, min_value):
        # Filtra las filas donde el valor (segundo elemento de cada tupla) es >= min_value
        return [row for row in self.data if row[1] >= min_value]


    def get_data(self):
        """Devuelve una lista de tuplas como datos de ejemplo para la tabla."""
        # Datos de ejemplo. En un caso real, esto podría venir de una base de datos
        return [
            ("Producto A", 100),
            ("Producto B", 200),
            ("Producto C", 150),
            ("Producto D", 300),
        ]

