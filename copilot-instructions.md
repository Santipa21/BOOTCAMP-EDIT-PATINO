---
applyTo: "**/*.py"
description: "Usar cuando se creen o modifiquen clases Python. Aplicar POO disciplinada, encapsulamiento, validacion de invariantes, constructores que solo creen objetos consistentes y preguntas de negocio cerradas si faltan reglas."
---
# Estilo para clases Python
Cuando generes o refactorices clases Python en este proyecto, segui estas reglas:

## Setters, Getters y Validaciones (OBLIGATORIO)

- **Toda clase DEBE usar `@property` para getters** cuando exponga atributos. Aunque sea solo lectura, usa `@property`.
- **Usar `@property` con setter** para validación en escritura. El setter DEBE validar datos antes de asignarlos.
- **Validar en el setter**, no dejar que el objeto quede en estado inválido.
- **Atributos privados con guion bajo**: `_atributo`. Nunca exposición directa de atributos públicos que sean mutables.
- **Si hay validación compleja**, extraer a método privado `_validar_algo()`.

### Ejemplo obligatorio:
```python
class Alumno:
    def __init__(self, nombre: str, edad: int):
        self._nombre = nombre
        self._edad = edad
        self._validar()  # Validar en constructor

    def _validar(self):
        if not isinstance(self._nombre, str) or not self._nombre.strip():
            raise ValueError("nombre debe ser string no vacío")
        if not isinstance(self._edad, int) or self._edad < 0:
            raise ValueError("edad debe ser entero >= 0")

    @property
    def nombre(self) -> str:
        return self._nombre

    @nombre.setter
    def nombre(self, valor: str) -> None:
        if not isinstance(valor, str) or not valor.strip():
            raise ValueError("nombre debe ser string no vacío")
        self._nombre = valor

    @property
    def edad(self) -> int:
        return self._edad

    @edad.setter
    def edad(self, valor: int) -> None:
        if not isinstance(valor, int) or valor < 0:
            raise ValueError("edad debe ser entero >= 0")
        self._edad = valor
```

## Niveles de visibilidad

- `_atributo`: privado (convención Python)
- métodos públicos: sin guion bajo
- `_metodo_privado()`: solo para uso interno, validaciones reutilizables

## Reglas generales

Cuando generes o refactorices clases Python en este proyecto, segui estas reglas:
- Aplicar buenas practicas de programacion orientada a objetos y un estilo de Python disciplinado.
- Toda clase debe proteger su estado interno. No expongas atributos mutables de forma publica salvo que haya un motivo explicito.
- Los objetos deben nacer validos. El constructor debe aceptar solo datos que permitan crear una instancia consistente.
- Validar entradas en el constructor y en toda operacion publica que pueda romper invariantes.
- Si un dato no es valido para el dominio, fallar temprano con una excepcion clara (`ValueError`, `TypeError` o una excepcion de dominio si ya existe).
- Mantener encapsulamiento. Preferir atributos con guion bajo y exponer acceso controlado mediante metodos o `@property` solo cuando aporte una API mas clara.
- No usar setters que permitan estados intermedios invalidos. Toda modificacion publica debe dejar el objeto consistente al terminar.
- Si la clase tiene reglas de consistencia complejas, extraer validaciones a metodos privados con nombres claros.
- Evitar clases anemicas o contenedores triviales de datos cuando el objeto deba proteger invariantes o tener comportamiento propio.
- No usar `dataclass` para entidades con invariantes importantes o encapsulamiento fuerte, salvo pedido explicito.
- Usar nombres claros, type hints y metodos pequenos con una unica responsabilidad.
- Evitar logica duplicada entre constructor, propiedades y metodos mutadores. Centralizar validaciones reutilizables.
- No agregar comentarios redundantes. El codigo debe ser legible por estructura y nombres.
# Criterios de diseno
- Cada metodo publico debe preservar la consistencia del objeto.
- No dejar objetos parcialmente inicializados.
- Si hay colecciones internas mutables, no devolver referencias mutables directas salvo que sea intencional; preferir copias o vistas inmutables.
- Las decisiones de modelado deben priorizar claridad del dominio antes que conveniencia superficial.
# Cuando falten reglas de negocio
- Si faltan reglas de negocio concretas, hacer preguntas cerradas, de si o no, de a una.
- Si no conviene frenar el trabajo, asumir la regla mas logica y conservadora, e indicar la suposicion de forma breve.
# Resultado esperado
Al crear una clase nueva, el resultado debe mostrar:
- Encapsulamiento real.
- Validacion explicita.
- Invariantes protegidas.
- Constructor seguro.
- API publica pequena y coherente.