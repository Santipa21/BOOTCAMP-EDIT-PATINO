from alumno import Alumno
from repositorio_alumnos import RepositorioAlumnos


class ServicioAlumnos:
    def __init__(self) -> None:
        self._repositorio = RepositorioAlumnos()
        # Agregar el alumno inicial si la base de datos está vacía
        if self._repositorio.contar() == 0:
            self._repositorio.agregar(Alumno("Esteban", "Calabria", 3))

    def listar(self) -> list[Alumno]:
        return self._repositorio.listar()

    def obtener_por_indice(self, indice: int) -> Alumno:
        return self._repositorio.obtener_por_indice(indice)

    def agregar(self, nombre: str, apellido: str, cursos: int) -> Alumno:
        nuevo = Alumno(nombre, apellido, cursos)
        return self._repositorio.agregar(nuevo)

    def eliminar_por_indice(self, indice: int) -> Alumno:
        return self._repositorio.eliminar_por_indice(indice)

    def modificar_por_indice(self, indice: int, nombre: str, apellido: str, cursos: int) -> Alumno:
        return self._repositorio.modificar_por_indice(indice, nombre, apellido, cursos)