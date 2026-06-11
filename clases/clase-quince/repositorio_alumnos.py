import sqlite3
from typing import List, Optional
from alumno import Alumno


class RepositorioAlumnos:
    def __init__(self, db_path: str = "alumnos.db") -> None:
        self._db_path = db_path
        self._inicializar_db()

    def _inicializar_db(self) -> None:
        """Crea la tabla de alumnos si no existe."""
        with sqlite3.connect(self._db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS alumnos (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nombre TEXT NOT NULL,
                    apellido TEXT NOT NULL,
                    cantidad_cursos INTEGER NOT NULL CHECK (cantidad_cursos >= 0)
                )
            """)
            conn.commit()

    def _alumno_from_row(self, row: tuple) -> Alumno:
        """Convierte una fila de la base de datos a un objeto Alumno."""
        id_alumno, nombre, apellido, cantidad_cursos = row
        alumno = Alumno(nombre, apellido, cantidad_cursos)
        # Asignar el ID de la base de datos al objeto Alumno
        alumno._id = id_alumno
        return alumno

    def agregar(self, alumno: Alumno) -> Alumno:
        """Agrega un nuevo alumno a la base de datos."""
        with sqlite3.connect(self._db_path) as conn:
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO alumnos (nombre, apellido, cantidad_cursos) VALUES (?, ?, ?)",
                (alumno.nombre, alumno.apellido, alumno.cantidad_cursos)
            )
            alumno._id = cursor.lastrowid
            conn.commit()
        return alumno

    def listar(self) -> List[Alumno]:
        """Retorna todos los alumnos de la base de datos."""
        with sqlite3.connect(self._db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT id, nombre, apellido, cantidad_cursos FROM alumnos ORDER BY id")
            rows = cursor.fetchall()
            return [self._alumno_from_row(row) for row in rows]

    def obtener_por_id(self, id_alumno: int) -> Optional[Alumno]:
        """Retorna un alumno por su ID o None si no existe."""
        with sqlite3.connect(self._db_path) as conn:
            cursor = conn.cursor()
            cursor.execute(
                "SELECT id, nombre, apellido, cantidad_cursos FROM alumnos WHERE id = ?",
                (id_alumno,)
            )
            row = cursor.fetchone()
            return self._alumno_from_row(row) if row else None

    def obtener_por_indice(self, indice: int) -> Alumno:
        """Retorna un alumno por su posición en la lista ordenada por ID."""
        alumnos = self.listar()
        if 0 <= indice < len(alumnos):
            return alumnos[indice]
        raise IndexError("Índice fuera de rango")

    def modificar(self, alumno: Alumno) -> Alumno:
        """Actualiza los datos de un alumno existente."""
        with sqlite3.connect(self._db_path) as conn:
            cursor = conn.cursor()
            cursor.execute(
                "UPDATE alumnos SET nombre = ?, apellido = ?, cantidad_cursos = ? WHERE id = ?",
                (alumno.nombre, alumno.apellido, alumno.cantidad_cursos, alumno.id)
            )
            if cursor.rowcount == 0:
                raise ValueError(f"No se encontró el alumno con ID {alumno.id}")
            conn.commit()
        return alumno

    def modificar_por_indice(self, indice: int, nombre: str, apellido: str, cursos: int) -> Alumno:
        """Modifica un alumno por su índice en la lista."""
        alumnos = self.listar()
        if 0 <= indice < len(alumnos):
            alumno = alumnos[indice]
            alumno.actualizar_datos(nombre, apellido, cursos)
            return self.modificar(alumno)
        raise IndexError("Índice fuera de rango")

    def eliminar_por_id(self, id_alumno: int) -> bool:
        """Elimina un alumno por su ID. Retorna True si se eliminó, False si no existía."""
        with sqlite3.connect(self._db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM alumnos WHERE id = ?", (id_alumno,))
            eliminado = cursor.rowcount > 0
            conn.commit()
            return eliminado

    def eliminar_por_indice(self, indice: int) -> Alumno:
        """Elimina un alumno por su índice y retorna el alumno eliminado."""
        alumnos = self.listar()
        if 0 <= indice < len(alumnos):
            alumno = alumnos[indice]
            self.eliminar_por_id(alumno.id)
            return alumno
        raise IndexError("Índice fuera de rango")

    def contar(self) -> int:
        """Retorna la cantidad total de alumnos."""
        with sqlite3.connect(self._db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT COUNT(*) FROM alumnos")
            return cursor.fetchone()[0]

    def limpiar_todo(self) -> None:
        """Elimina todos los registros de la tabla."""
        with sqlite3.connect(self._db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM alumnos")
            conn.commit()
