** Documento de dispersión**

En base a la reducida información proporcionada se mantendran como pendientes ciertas herramientas 
de desarrollo y otras se darán por sentado

---

## Problemas detectados

1. Definir infraestructura para el desarrollo
	1.a Definir tipo de desarrollo,
		¿Hay algo desarrollado previamente?, no especificado pero se deduce que no hay ningún tipo de desarrollo
	1.b Lenguaje o framework a utilizar, no especificado se dejará a libre disposición
	1.c Servidor
		1.c.i Qué tipo de servidores se utilizará (S. Operativo, si se cuenta con uno propio) No especificado
		1.c.ii ¿Se necesitará un balanceo de carga? No especificado
		1.c.iii ¿Se necesitará un Servidor espejo? (Necesario cuando se deban hacer mantenciones o falla) No especificado
	1.d Base de datos, se utilizara un DBMS para el guardado de datos, dependerá de cada cuanto tiempo se guardarán
	los registros, en caso de ser una base de datos convencional se utilizara MySQL, de lo contrario se utilizará
	Redis o similar
		1.d.1 Política de Respaldos: Cuán a menudo se realizarán los respaldos y los protocolos de los mismos, 
		también dependera de cuan a menudo se actualizan los datos

2. Metodologia de desarrollo
	Se basará en Sprints cortos y tareas a realizar, determinadas por el dashboard implementado

3. Tareas principales (ordenadas por relevancia)
	3.a Modelar la base de datos
		3.a.i Crud de cada cliente (ya que cada uno tendrá una forma diferente de enviar sus configuraciones)
		3.b.i Crud de datos de cada vehículo, determinados por una API
		3.c.i Agregar cualquier tabla en caso de tener una mayor segmentación los parámetros 
	3.b Recepción de parámetros
	3.c Envío de comandos a vehiculo
	3.d Separación de modelo de capas
		3.d.i Aspecto visual
		
4. Resumen de forma de desarrollo:
	A continuación se entregará la forma de desarrollo, dada la acotada  información entregada
	- Servidor de deploy Fedora Workstation o Ubuntu Server
    - Contenedor Docker para desarrollo
    - Versionado en git
	- Desarrollo en Python (Django o Flask aún por definir)
	- DBMS: MySQl o Redis (aún por definir)
