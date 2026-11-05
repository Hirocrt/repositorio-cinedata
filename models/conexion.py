import oracledb

class ConexionDB:

    def __init__(self):
        try:
            # Conexión apuntando explícitamente a localhost
            self.conexion = oracledb.connect(
                user="ALEX", 
                password="inacap123", 
                host="localhost",
                port=1521,          # Puerto por defecto de Oracle
                service_name="xe"   # Cambia a sid="xe" si tu base de datos lo requiere
            )
            self.cursor = self.conexion.cursor()
            print("Conexión exitosa a localhost.")
            
        except Exception as e:
            print(f"ERROR CRÍTICO DE CONEXIÓN: Detalle: {e}")
            self.conexion = None
            self.cursor = None