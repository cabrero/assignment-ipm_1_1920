# ASSIGNMENT: PRÁCTICA 1 - INTERFACES GRÁFICAS DE USUARIA CON GTK+ Y PYTHON

## Objetivo

En esta misión (_assignment_) tendrás que desarrollar una aplicación
gráfica de escritorio. Para alcanzar tu objetivo tendrás que usar los
conocimientos adquiridos sobre el desarrollo de interfaces gráficas de
usuaria.

Para llevar a cabo tu cometido dispondrás del lenguaje de programación
`python` y la librería gráfica `Gtk+`.

## Plazo

Se espera que hayas finalizado tu misión antes del día *25/10/2019 a
las 24:00*. Cualquier retraso en la finalización de tu cometido será
penalizado de acuerdo con el reglamento de la asignatura.

## Presentación del _assignment_

Tu empresa ha decidido entrar en el mercado de las aplicaciones de
fitness. Para ello el primer paso es crear una base de datos de
rutinas de ejercicios que ofrecerá a los futuros clientes del servicio
que quiere implantar.

Para el desarrollo y mantenimiento de dicha base de datos el jefe ha
decidio que vas a desarrollar una aplicación de escritorio con
interface gráfica.

El desarrollo seguirá una arquitectura cliente/servidor básica, donde
el servidor ofrece el acceso a la base de datos de rutinas y el
cliente es la aplicación que tienes que desarrollar.

La aplicación también seguirá un modelo convencional tipo CRUD, es
decir, sus funcionalidades será la creación, acceso, actualización y
borrado.

*NOTA:* debido a las restricciones temporales, algunas de las
funcionalidades mencionadas no se incluyen en la presente misión.

La estructura de la información tampoco presenta sorpresas: la BBDD se
compone de una colección de rutinas. Por cada rutina tendremos su
nombre, una imagen asociada, y una fecha de publicacción. A su vez,
cada rutina está conformada por una lista ordenada de ejercicios y por
cada ejercicio disponemos de su denominación, duración, descripción y
una imagen representativa. Como caso especial, en la lista de
ejercicios también podemos encontrar períodos de descanso, para los
cuales la única información disponible es la duración.

## Recursos

Antes de comenzar debes procurarte las siguientes herramientas y
recursos:

* `python` versión >= 3.7
* `Gtk+` versión 3 y bindings para python
* `AT-SPI` y bindings para python
* `Git`
* `PlantUML` ([plantuml.com](plantuml.com))
* Un repositorio en [git.fic.udc.es](git.fic.udc.es) con el nombre
  `ipm1920-p1` configurado como remote del repositorio en el
  directorio de trabajo.

El resto de los recursos necesarios se irán presentando con cada
cometido (_task_), a medida que sean necesarios.


# DISEÑO DE LA IU H1-D1

Debes comenzar la misión por el caso de uso "Ver conjunto de rutinas":

> La usuaria dispone de una vista de las rutinas almacenadas
> en la base de datos.

Para este primer cometido debes, únicamente, diseñar las
*priority guides* correspondientes a la IU.

Para que este cometido se pueda considerar completo debes asegurarte
de haber alcanzado las siguientes condiciones (_requirements_):

* [Existe un único fichero "doc/priority-guides.md"](check:)
* [No hay ficheros pendientes de commit](check:)
* [El último commit tiene la etiqueta "H1-D1"](check:)
* [El nombre del repositorio remote es "ipm1920-p1"](check:)
* [El repositorio remote "ipm1920-p1" está actualizado](check:)

# DISEÑO DE LA IU H1-D2

Continuando con el caso de uso que dejaste abierto, tu siguiente
cometido es diseñar los *wireframes* apropiadas para las priority
guides. Para diseñar los wireframes usaras la herrmaienta PlantUML.

Antes de moverte al siguiente cometido debes cumplir las siguientes
condiciones:

* [Existe al menos un fichero "wireframe*.*" en el directorio "doc/"](check:)
* [PlantUML compila correctamente los ficheros "doc/wireframe*.*"](check:)
* [No hay ficheros pendientes de commit](check:)
* [El último commit tiene la etiqueta "H1-D2"](check:)
* [El nombre del repositorio remote es "ipm1920-p1"](check:)
* [El repositorio remote "ipm1920-p1" está actualizado](check:)

# DISEÑO SOFTWARE H1-I1

Partiendo del patrón MVC o cualquiera de sus variantes, crea un diseño
software que te permita implementar el caso de uso en el que estás
trabajando.

El diseño debe estar expresado según las indicaciones del estándar UML
y debe cubrir tantos los aspectos estáticos como dinámicos del
mismo. Para realizar el diseño usaras la herramienta PlantUML.

En este cometido debes cumplir las siguientes condiciones:

* [Existe al menos un fichero "*.uml" en el directorio "doc/ds/"](check:)
* [PlantUML compila correctamente los ficheros "doc/ds/*.uml"](check:)
* [No hay ficheros pendientes de commit](check:)
* [El último commit tiene la etiqueta "H1-I1"](check:)
* [El nombre del repositorio remote es "ipm1920-p1"](check:)
* [El repositorio remote "ipm1920-p1" está actualizado](check:)

# IMPLEMENTACIÓN H1-I2

Implementa el caso de uso siguiendo los diseños previos. Si es
necesario, corrige los diseños. Para la implementación usarás `python`
y `Gtk+`, también debes asegurarte de tener operativo el servicio
`AT-SPI`.

En la implementación habrá, al menos, un fichero `ipm-p1.py` que
lanzará la aplicación, y, por tanto, debe ser ejecutable.

El título de la ventana principal será "IPM P1", y al cerrar dicha
ventana la aplicación terminará.

Este cometido no puede terminar si no se cumplen las siguientes
condiciones:

* [Existe un fichero "ipm-p1.py" y es ejecutable](check:)
* [Después de ejecutar "ipm-p1.py", se muestra una ventana "IPM P1"](check:)
* [No hay ficheros pendientes de commit](check:)
* [El último commit tiene la etiqueta "H1-I2"](check:)
* [El nombre del repositorio remote es "ipm1920-p1"](check:)
* [El repositorio remote "ipm1920-p1" está actualizado](check:)


# DISEÑO DE LA IU H2-D1

Una vez completados los cometidos anteriores, te enfrentarás al
siguiente caso de uso "Ver rutina":

> La usuaria dispone de una vista detallada de los ejercicios, y su
> información, para una rutina determinada. La usuaria selecciona la
> rutina para la cual se le ofrece dicha vista.

Actualiza las *priority guides* con los elementos necesarios para
incluir este caso de uso nuevo.

Para que este cometido se pueda considerar completo debes asegurarte
de haber alcanzado las siguientes condiciones:

* [El fichero "doc/priority-guides.md" está actualizado respecto a la versión "H1-I2"](check:)
* [No hay ficheros pendientes de commit](check:)
* [El último commit tiene la etiqueta "H2-D1"](check:)
* [El nombre del repositorio remote es "ipm1920-p1"](check:)
* [El repositorio remote "ipm1920-p1" está actualizado](check:)

# DISEÑO DE LA IU H2-D2

Continúa con el caso de uso abierto actualizando el diseño de los
*wireframes*.

Antes de moverte al siguiente cometido debes cumplir las siguientes
condiciones:

* [Los ficheros "doc/wireframe*." están actualizados respecto a la versión "H1-I2"](check:)
* [PlantUML compila correctamente los ficheros "doc/wireframe*.*"](check:)
* [El último commit tiene la etiqueta "H2-D2"](check:)
* [El nombre del repositorio remote es "ipm1920-p1"](check:)
* [El repositorio remote "ipm1920-p1" está actualizado](check:)

# DISEÑO SW E IMPLEMENTACIÓN H2-I1

Actualiza el diseño software para abarcar el nuevo caso de
uso, e implementa los cambios. Asegurate de cumplir las condiciones:

* [Los ficheros "doc/ds/*.uml" están actualizados respecto a la versión "H1-I2"](check:)
* [PlantUML compila correctamente los ficheros "doc/ds/*.uml"](check:)
* [Existe un fichero "ipm-p1.py" y es ejecutable](check:)
* [Después de ejecutar "ipm-p1.py", al cerrar la ventana "IPM P1", termina la ejecución](check:)
* [No hay ficheros pendientes de commit](check:)
* [El último commit tiene la etiqueta "H2-I1"](check:)
* [El nombre del repositorio remote es "ipm1920-p1"](check:)
* [El repositorio remote "ipm1920-p1" está actualizado](check:)

# PRUEBAS H2-T1

Para cerrar el caso de uso, escribe una prueba *e2e* (_end to end_)
para el siguiente escenario:

> Dado que la aplicación se está ejecutando
> Y        la base de datos contiene la rutina "Core avanzado de pilates" con 10 ejercicios
> Cuando   la usuaria selecciona la rutina "Core avanzado de pilates"
> Entonces la vista de detalle muestra 10 ejercicios

Implementa la prueba en un fichero ejecutable `test/prueba-01.py`. No
es necesario que emplees ningún framework de pruebas como unittest,
pytest o lettuce.

Antes de moverte al siguiente cometido debes cumplir las siguientes
condiciones:

* [Existe un fichero "test/prueba-01.py" y es ejecutable](check:)
* [No hay ficheros pendientes de commit](check:)
* [El último commit tiene la etiqueta "H2-T1"](check:)
* [El nombre del repositorio remote es "ipm1920-p1"](check:)
* [El repositorio remote "ipm1920-p1" está actualizado](check:)

# DISEÑO DE LA IU H3-D1

El siguiente caso de uso al que te enfrentarás es "Eliminar rutina":

> La usuaria puede eleminar una rutina seleccionada

Está permitido que incluyas uno o más mecanismos de borrado, como por
ejemplo un botón de borrar, un menú contextual, la tecla de suprimir
y/o retroceso, etc. Pero en cualquer caso tienes que incluir, al
menos, un botón de borrado.

Actualiza las *priority guides* y los *wireframes* para dar cobertura
a este nuevo caso de uso.

Antes de moverte al siguiente cometido debes cumplir las siguientes
condiciones:

* [El fichero "doc/priority-guides.md" está actualizado respecto a la versión "H2-T1"](check:)
* [Los ficheros "doc/wireframe*." están actualizados respecto a la versión "H2-T1"](check:)
* [PlantUML compila correctamente los ficheros "doc/wireframe*.*"](check:)
* [No hay ficheros pendientes de commit](check:)
* [El último commit tiene la etiqueta "H3-D1"](check:)
* [El nombre del repositorio remote es "ipm1920-p1"](check:)
* [El repositorio remote "ipm1920-p1" está actualizado](check:)

# DISEÑO SW E IMPLEMENTACIÓN H3-I1

Completa el caso de uso actualizando el diseño software y la
implementación. Asegurate de cumplir las siguientes condiciones:

* [Los ficheros "doc/ds/*.uml" están actualizados respecto a la versión "H2-T1"](check:)
* [PlantUML compila correctamente los ficheros "doc/ds/*.uml"](check:)
* [Existe un fichero "ipm-p1.py" y es ejecutable](check:)
* [Después de ejecutar "ipm-p1.py", al cerrar la ventana "IPM P1", termina la ejecución](check:)
* [No hay ficheros pendientes de commit](check:)
* [El último commit tiene la etiqueta "H3-I1"](check:)
* [El nombre del repositorio remote es "ipm1920-p1"](check:)
* [El repositorio remote "ipm1920-p1" está actualizado](check:)


# USER EXPERIENCE UX-1

Una vez completado el caso de uso anterior, vamos a arreglar los
errores de usabilidad que puedas haber dejado atrás.

Respecto al botón de borrado asegurate de seguir las siguientes directrices:

* Make invalid buttons insensitive, rather than popping up an error
  message when the user clicks them.
  
* Buttons which have a destructive consequence, such as removing or
  deleting a content item, can be given a destructive style. This
  highlights the button by coloring it, and acts as a warning to the
  user.
  
Estas directrices también las puedes consultar en:
[https://developer.gnome.org/hig/stable/buttons.html.es](https://developer.gnome.org/hig/stable/buttons.html.es)

Escribe en el fichero "doc/hig.txt" las partes del código que aseguran
el cumplimiento de dichas directrices.

* [Existe un fichero "doc/hig.txt"](check:)
* [No hay ficheros pendientes de commit](check:)
* [El último commit tiene la etiqueta "UX-1"](check:)
* [El nombre del repositorio remote es "ipm1920-p1"](check:)
* [El repositorio remote "ipm1920-p1" está actualizado](check:)

# USER EXPERIENCE UX-2

Continuando con el cometido anterior, tendrás que cumplir la siguiente
directriz:

* After pressing a button, the user should expect to see the result of
  their action within 1 second.
  
A esto hemos de añadir:

* La interface no debe quedar bloqueada nunca.

Puesto que no conocemos a priori cuanto tiempo tardará el borrado en
la base de datos, ni tenemos garantía de que sea menos de 1 segundo:

* Las operaciones contra la base de datos se deben realizar de manera
  concurrente.
  
* Tras lanzar la operación, se debe proporcionar a la usuaria el
  feedback oportuno a modo de resultado de la acción de pulsar el
  botón de borrado.
  
* Las operaciones de red pueden fallar. En tal caso debes informar
  convenientemente a la usuaria.

Crea un diagrama de secuencia de una operación de borrado concurrente
en el fichero "doc/ds/concurrencia.*"

Enumera los cambios por los que pasa la interface durante la
operación, p.e. desactivar botón de borrar, eliminar rutina de la
vista, mostrar spinner o barra de progeso, etc.

Estudia la lista de pasos y determina si es posible alguna secuencia
de lugar a fallos, p.e.:

* El usuario pulsa dos veces borrar con la misma rutina seleccionada.

* La rutina se elimina de la vista, pero no del servidor, o viceversa.

Ten en cuenta que algunos errores pueden manifestarse sólo si la
usuaria lanza varias operaciones de borrado consecutivas.

Describe en un fichero "doc/concurrencia.txt" los resultados del
estudio que acabas de realizar. Si hay posibles errores, haz un
commit, vuelve al principio del cometido y arréglalos.

Asegurate de cumplir las condiciones:

* [Existe un fichero "doc/ds/concurencia.*"](check:)
* [PlantUML compila correctamente los ficheros "doc/ds/*.uml"](check:)
* [Existe un fichero "doc/concurrencia.txt"](check:)
* [No hay ficheros pendientes de commit](check:)
* [El último commit tiene la etiqueta "UX-2"](check:)
* [El nombre del repositorio remote es "ipm1920-p1"](check:)
* [El repositorio remote "ipm1920-p1" está actualizado](check:)

# USER EXPERIENCE UX-3

Continuando con las mejoras en la usabilidad, vas a internacionalizar
la aplicación. Además debes localizarla a los siguientes *locales*:

* es_ES.utf8
* en_US.utf8

No olvides ningún elemento afectado por la i18n: idioma, fechas,
números, etc. Y comprueba que se cumplen las condiciones:

* [Es posible ejecutar "ipm-p1.py" con el locale "es_ES.utf8"](check:)
* [Es posible ejecutar "ipm-p1.py" con el locale "en_US.utf8"](check:)
* [No hay ficheros pendientes de commit](check:)
* [El último commit tiene la etiqueta "UX-3"](check:)
* [El nombre del repositorio remote es "ipm1920-p1"](check:)
* [El repositorio remote "ipm1920-p1" está actualizado](check:)


# DISEÑO DE LA IU H4-D1

Para terminar la misión, tendrás que abordar el caso de uso:
"Reordenar ejercicios":

> Dentro de la vista de detalle de una rutina, la usuaria puede
> cambiar el orden de los ejercicios que forman parte de la rutina en
> cuestión.

Actualiza las *priority guides* y los *wireframes* para dar cobertura
a este nuevo caso de uso.

Antes de moverte al siguiente cometido debes cumplir las siguientes
condiciones:

* [El fichero "doc/priority-guides.md" está actualizado respecto a la versión "UX-3"](check:)
* [Los ficheros "doc/wireframe*.*" están actualizados respecto a la versión "UX-3"](check:)
* [PlantUML compila correctamente los ficheros "doc/wireframe*.*"](check:)
* [No hay ficheros pendientes de commit](check:)
* [El último commit tiene la etiqueta "H4-D1"](check:)
* [El nombre del repositorio remote es "ipm1920-p1"](check:)
* [El repositorio remote "ipm1920-p1" está actualizado](check:)

# DISEÑO SW E IMPLEMENTACIÓN H4-I1

Completa el caso de uso actualizando el diseño software y la
implementación. Asegurate de cumplir las siguientes condiciones:

* [Los ficheros "doc/ds/*.uml" están actualizados respecto a la versión "UX-3"](check:)
* [PlantUML compila correctamente los ficheros "doc/ds/*.uml"](check:)
* [Existe un fichero "ipm-p1.py" y es ejecutable](check:)
* [Después de ejecutar "ipm-p1.py", al cerrar la ventana "IPM P1", termina la ejecución](check:)
* [No hay ficheros pendientes de commit](check:)
* [El último commit tiene la etiqueta "H4-I1"](check:)
* [El nombre del repositorio remote es "ipm1920-p1"](check:)
* [El repositorio remote "ipm1920-p1" está actualizado](check:)
