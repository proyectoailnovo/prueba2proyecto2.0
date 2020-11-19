# prueba2proyecto2.0
Proyecto prueba 2 Desarrollo aplicaciones web y Mobile

Proyecto Tienda web/blog sobre componentes PC

El proyecto a desarrollar tiene por propósito principal la venta de componentes y accesorios para PC, proveer información a los usuarios y crear los medios para que estos puedan interactuar entre ellos y con nosotros. La página provee la posibilidad que los usuarios se registren en la misma e interactúen con otros usuarios por medio de un blog, donde podrán exhibir imágenes y comentarios. A su turno, podrán visualizar distintas imágenes en galería, como por ejemplo, las "setups" que hemos propuestos. Tiene un apartado para visualizar información corporativa y un medio para contactarnos a nosotros directamente.

Para los administradores, las herramientas para manejar la información sobre los usuarios, posts u otras cuestiones de orden administrativo

Si bien el apartado de compraventa es un elemento muy importante, aún se encuentra en desarrollo. Es un elemento crucial que no debe presentar falencias, por lo que su presentación en este momento representa una negligencia. Por lo anterior, preferimos garantizar que el mismo estará disponible para la entrega final de este proyecto, de forma completa y suficiente.


Resultado pruebas

De las pruebas diseñadas 7
Errores=0
Failures=1

Se probaron principalmente Forms y Models de las distintas funcionalidades que ofrece la web.

El fallo se presenta en AIL: test_form_validation_for_blank_items (blog.tests.Testblank2), debido a que se solicita que el campo no este vacío, y se deja intencionalmente vacío para que presente el error.
