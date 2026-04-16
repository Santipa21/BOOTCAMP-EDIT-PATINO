class Alumno:
    """Representa a un alumno con identificador único, nombre, apellido y cantidad de cursos."""

    def __init__(self, id: int, nombre: str, apellido: str, cantidad_cursos: int):
        self._id = id
        self._nombre = nombre
        self._apellido = apellido
        self._cantidad_cursos = cantidad_cursos
        self._validar()

    def _validar(self) -> None:
        """Valida que los datos del alumno sean consistentes."""
        if not isinstance(self._id, int) or self._id <= 0:
            raise ValueError("id debe ser un entero positivo")
        if not isinstance(self._nombre, str) or not self._nombre.strip():
            raise ValueError("nombre debe ser un string no vacío")
        if not isinstance(self._apellido, str) or not self._apellido.strip():
            raise ValueError("apellido debe ser un string no vacío")
        if not isinstance(self._cantidad_cursos, int) or self._cantidad_cursos < 0:
            raise ValueError("cantidad_cursos debe ser un entero no negativo")

    @property
    def id(self) -> int:
        """Retorna el identificador único del alumno."""
        return self._id

    @property
    def nombre(self) -> str:
        """Retorna el nombre del alumno."""
        return self._nombre

    @nombre.setter
    def nombre(self, valor: str) -> None:
        """Establece el nombre del alumno con validación."""
        if not isinstance(valor, str) or not valor.strip():
            raise ValueError("nombre debe ser un string no vacío")
        self._nombre = valor

    @property
    def apellido(self) -> str:
        """Retorna el apellido del alumno."""
        return self._apellido

    @apellido.setter
    def apellido(self, valor: str) -> None:
        """Establece el apellido del alumno con validación."""
        if not isinstance(valor, str) or not valor.strip():
            raise ValueError("apellido debe ser un string no vacío")
        self._apellido = valor

    @property
    def cantidad_cursos(self) -> int:
        """Retorna la cantidad de cursos del alumno."""
        return self._cantidad_cursos

    @cantidad_cursos.setter
    def cantidad_cursos(self, valor: int) -> None:
        """Establece la cantidad de cursos con validación."""
        if not isinstance(valor, int) or valor < 0:
            raise ValueError("cantidad_cursos debe ser un entero no negativo")
        self._cantidad_cursos = valor
