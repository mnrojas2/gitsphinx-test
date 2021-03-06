================
README DE PRUEBA
================

Archivo creado para probar la funcionalidad de git como de reStructuredText

.. note::

   Todavía bajo desarrollo.

.. contents::

Formato básico
--------------

Tres tristes tigres trigaban trigo en un trigal. Pedro Pérez Pereira, pobre pintor portugués, pinta preciosos paisajes para poder partir para París.

- Al parecer esto sirve para los items
- Parece ser más fácil que Latex

* Lorem ipsum
* Relleno en otro idioma

+ y = 1 + cos(x) = int(sin(x),x)
+ y0 = y(0)

.. _este:

1. Se pueden enumerar las cosas.
2. Pero no se pueden saltar los números.
#. Pero lo mejor es poner "#." y el número va solo.

  a. Letras también sirven
  #. Como números romanos
  #. Pero poco se utilizarían considerando que solo se puede rellenar con (#.)
  #. Y tal vez igualmente rellene con números


Definición:
    Simplemente indentando la segunda línea

**Listas de campos:**

:Autor: Yo mismo,
        Yo también
        y el que está escribiendo esto
:Version: 0.0.001a
:Dedicado a: Mi futuro yo

Comandos para funciones:

-b       para basarse
-d       para deletear
-a file  para avisparse

Bloques
-------

Literalmente bloques:

A ver chiquillos, antes que nah en el chat, vamos a dar las reglas del chat.

::

  Primero: Prohibido hablar de Huevito Rey.
  Segundo: Prohibido hablar de Mysterion.
  Tercero: Prohibido los insultos.
  Y cuarto: No están permitidos los garabatos y los comu- y el comunismo.
  ¿Estamos de acuerdo? Lo quiero todo a la buena. ¿Estamos de acuerdo?

Después del '::' todo lo que esté indentado forma parte del bloque. Cuando se vuelve a la indentación de esta linea, se acaba el bloque.

::

      Ya les dije nada de insultos por favor.
    BASTA DE HABLAR DE HUEVITO REY;
  EL ESTA PRESO!!

Se pueden crear bloques by >impliying y así no tener que indentar::

> Como esto
> Y esto también

|   Yep, la '|' puede servir para escribir una línea en varias.
    Y parece que también junta líneas en la misma
    si es que tienen la misma indentación,
    sin tener que agregar la '|'.

Se puede escribir código de Python como si fuese el IDLE:

>>> print("Este es, el precio de la historia")
Este es, el precio de la historia

Y lo permite copiar también. Con la librería doctest, se utiliza para evaluar lo que aparece en el ejemplo comentado en la función misma.

Tablas
------

A lo Excel [1]_:

+------------+------------+-----------+
| Header 1   | Header 2   | Header 3  |
+============+============+===========+
| body row 1 | column 2   | column 3  |
+------------+------------+-----------+
| body row 2 | Cells may span columns.|
+------------+------------+-----------+
| body row 3 | Cells may  | - Cells   |
+------------+ span rows. | - contain |
| body row 4 |            | - blocks. |
+------------+------------+-----------+

A lo cuaderno [1]_:

=====  =====  ======
   Inputs     Output
------------  ------
  A      B    A or B
=====  =====  ======
False  False  False
True   False  True
False  True   True
True   True   True
=====  =====  ======

.. [1] En el código original se pueden observar las diferencias. (Aprovecho de usar esta línea para ejemplificar referencias).

Transición: Es una línea horizontal larga. No debe comenzar ni finalizar una sección o documento, ni dos transiciones deben ser inmediatamente adyacentes.

-----------------

En cuanto a referencias y al igual que los items enumerados, estos se pueden completar con '#'. Por ejemplo, este [#]_.

.. [#] Supongo que debe ser la 2da referencia de pie de página.

También se pueden referenciar como en Latex, utilizando un nombre que luego se transforma a número [#ejemplo]_.

.. [#ejemplo] Como en este caso. Lindo verdad?

Citaciones e hipervínculos
--------------------------

Es prácticamente como la parte anterior pero sin el uso del '#' [CIT2022]_. También parece ser innecesario los corchetes para la palabra según CIT2022_.

.. [CIT2022] https://docutils.sourceforge.io/docs/user/rst/quickref.html#citations

Por otra parte los hyperlinks, se escriben de forma similar, pero solo utilizando el '_' en distintas posiciones. Por ejemplo, Python_.

.. _Python: https://www.python.org/

Los hipervínculos también se pueden escribir de la forma antigua (nombre<url>) como en este caso: `La misma página de Python <https://www.python.org/>`_.

También se pueden utilizar para hacer referencia cruzada. Por ejemplo, este_ (enumeración de puntos).

Si se quiere referenciar una sección basta con repetir el nombre de esta con comillas y guión bajo, como en `Citaciones e hipervínculos`_.

Directivas
----------

Funciones especiales asociadas al uso de '::'.

Se pueden cargar algunos elementos externos, como una imagen, con la ubicación relativa a este archivo.

.. image:: images/patito.png

También se pueden crear reemplazos a ciertas palabras con el uso de líneas verticales, como en el caso del |animal|.

.. |animal| replace:: pato

::

    También se pueden crear reemplazos a ciertas palabras con el uso de líneas verticales, como en el caso del |animal|.

    .. |animal| replace:: pato

Eso y más en el `siguiente link`__.

.. _Link : https://docutils.sourceforge.io/docs/ref/rst/directives.html
__ Link_

.. Ese último ejemplo muestra cómo se pueden crear referencia una frase completa, sin tener que llamar a la nueva referencia, como la misma otra vez.
.. Como también estos últimos dos mostrar cómo hacer comentarios a este tipo de archivos.

Extra tips
----------

#. El equivalente a correr ". ./bin/activate" en Windows Powershell es simplemente "./Scripts/activate.ps1"
#. Para agregar direcciones a PATH, únicamente escribir en Powershell: $env:path += '<new directory>' donde <new directory> es la ubicación de la carpeta con el .exe a correr [#]_ [#]_. 

.. [#] Es importante considerar que en PATH las direcciones deben ir separadas con ';', por lo que sería bueno revisar si es que el ';' está al final del string o no.
.. [#] Otra cosa es que esta opción es temporal y dejará de funcionar al cerrar la sesión de Powershell.