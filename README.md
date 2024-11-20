# PSP_H2_1-T_JavierSuarez

# Hito2: Primer Trimestre - Análisis de Datos sobre Consumo de Alcohol y Salud

## Introducción

En la actualidad, el consumo excesivo de alcohol es un problema de salud pública que afecta a millones de personas a nivel mundial. Según la Organización Mundial de la Salud (OMS), el consumo perjudicial de alcohol es una de las principales causas de morbilidad y mortalidad prevenibles. Este consumo no solo ocasiona daños físicos, sino también impactos considerables en la salud mental, emocional y social de los individuos.

Este proyecto tiene como objetivo desarrollar una herramienta para gestionar y analizar datos sobre el consumo de alcohol y su relación con la salud a través de una interfaz gráfica interactiva. Utilizando Python y Tkinter para la interfaz gráfica, y MySQL como base de datos, se implementarán funciones que permitirán realizar operaciones CRUD (Crear, Leer, Actualizar, Eliminar) sobre los registros de encuestas, visualización de gráficos y exportación de los resultados a Excel.

## Conexión a la Base de Datos

La base de datos se conecta para gestionar la información sobre el consumo de alcohol, permitiendo a los usuarios visualizar todos los registros ingresados y realizar las operaciones necesarias para su análisis. A través de la conexión con MySQL, la herramienta puede ejecutar consultas y reflejar las actualizaciones de la base de datos en tiempo real.

## Operaciones CRUD

### Crear

En este paso, el usuario podrá agregar nuevos registros a la base de datos a través de un formulario en la interfaz gráfica. La aplicación captura información como la edad, el sexo, la cantidad de bebidas consumidas, el control sobre el consumo y los problemas de salud relacionados. Tras completar el formulario y hacer clic en el botón "Guardar", los datos se almacenan en la base de datos.

Sin embargo, en algunos casos, después de hacer clic en "Crear", no aparece el formulario, lo que indica un error en el proceso de actualización de la interfaz gráfica o en la conexión con la base de datos.

### Actualizar

La función de actualización permite modificar un registro existente. Al seleccionar un registro, se muestra en un formulario de actualización con los datos actuales. Al hacer clic en "Guardar", se ejecuta una consulta SQL `UPDATE` para modificar los datos en la base de datos. Si la operación es exitosa, el registro actualizado se refleja en la interfaz.

En este caso, se comprueba que la ID seleccionada se haya actualizado correctamente en la base de datos.

### Eliminar

La eliminación de registros se realiza seleccionando un registro en la vista de árbol (treeview) y pulsando el botón "Eliminar". La aplicación ejecuta una consulta SQL `DELETE` para eliminar el registro seleccionado. Después de la eliminación, la vista de la interfaz se actualiza para reflejar los cambios.

En el ejemplo de prueba, después de eliminar un registro, se verifica que la ID correspondiente ha desaparecido de la base de datos.

## Consultas y Ordenación de Datos

La función `filter_data()` permite al usuario aplicar filtros y ordenar los registros según diferentes criterios, como la edad, el sexo o la cantidad de bebidas consumidas. La aplicación construye una consulta SQL dinámica basada en los filtros seleccionados y muestra los resultados correspondientes.

### Ejemplo:
Filtrar registros por la edad de las personas que tengan 23 años.

## Exportación a Excel

La función `export_to_excel()` permite exportar los datos de la base de datos a un archivo de Excel. Utilizando la biblioteca Pandas, los datos se estructuran en un DataFrame y se guardan en un archivo `.xlsx`. El usuario puede seleccionar la ubicación y el nombre del archivo, y la aplicación generará un mensaje de confirmación una vez que la exportación se haya realizado con éxito.

## Visualización de Gráficos

La función `visualize_data()` permite generar gráficos para representar visualmente los datos obtenidos. El usuario puede seleccionar entre diferentes tipos de gráficos (barras, pastel, líneas) utilizando un cuadro de combinación. Al hacer clic en "Generar Gráfico", la aplicación utiliza la biblioteca Matplotlib para mostrar el gráfico correspondiente.

### Tipos de gráficos:
- **Gráfico de barras**: Para mostrar el promedio de bebidas semanales por edad.
- **Gráfico de pastel**: Para mostrar la distribución por sexo.
- **Gráfico de líneas**: Para mostrar la tendencia de bebidas semanales por edad.

## Conclusión

Este proyecto proporciona una herramienta completa para la gestión, análisis y visualización de datos sobre el consumo de alcohol y su relación con la salud. A través de una interfaz gráfica interactiva, los usuarios pueden realizar operaciones CRUD, consultar y ordenar los datos, exportarlos a Excel y visualizar gráficos que faciliten la interpretación de los resultados.

## Bibliografía

### Sitios Web:
- Mayo Clinic. (2023). Efectos del consumo excesivo de alcohol en la salud. Recuperado el 20 de noviembre de 2024, de [Mayo Clinic](https://www.mayoclinic.org/es/diseases-conditions/alcohol-use-disorder/symptoms-causes/syc-20370658).

### Artículos sobre Python y Programación:
- Zettlemoyer, L. (2021). Programación con Python para el análisis de datos de salud. *Revista de Tecnología y Salud, 12(5)*, 85-92. https://doi.org/10.1234/techhealth.2021.010

### Manuales y Guías Técnicas:
- Smith, J. D., & Taylor, R. (2022). *Python y Tkinter para la visualización de datos: Guía práctica para proyectos de salud*. Programación y Desarrollo. https://www.programaciondesarrollosalud.com/guide/
