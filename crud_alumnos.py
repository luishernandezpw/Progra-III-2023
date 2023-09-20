import crud_academica
db = crud_academica.crud()

class crud_alumnos:
    def consultar_alumnos(self):
        return db.consultar("select * from alumnos")