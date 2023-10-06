import crud_academica
db = crud_academica.crud()

class crud_alumnos:
    def consultar_alumnos(self, buscar):
        return db.consultar("select * from alumnos where codigo like'%"+ buscar["buscar"] 
            +"%' or nombre like'%"+ buscar["buscar"] +"%'")
    
    def administrar(self, alumnos):
        if alumnos["accion"] == "nuevo":
            sql = """
                INSERT INTO alumnos (codigo, nombre, direccion, telefono)
                VALUES (%s, %s, %s, %s)
            """
            val = (alumnos["codigo"], alumnos["nombre"], alumnos["direccion"], alumnos["telefono"])
        elif alumnos["accion"] == "modificar":
            sql = """
                UPDATE alumnos
                    SET codigo=%s, nombre=%s, direccion=%s, telefono=%s
                WHERE idAlumno=%s
            """
            val = (alumnos["codigo"], alumnos["nombre"], alumnos["direccion"], alumnos["telefono"], alumnos["idAlumno"])
        elif alumnos["accion"] == "eliminar":
            sql = """
                DELETE FROM alumnos
                WHERE idAlumno=%s
            """
            val = (alumnos["idAlumno"],)
        return db.ejecutar_consultas(sql, val)