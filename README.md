# shpconverter
Python script to convert from a Shapefile to jQuery Vector Map script.

Son 3 scripts pythons, myConverter.py, converter.py y formatter.py

1- myConverter.py -> ejecutarlo desde consola python myConverter.py. Ejecutará en batch todos los archivos .shp contenidos en todas las carpetas dentro del directorio donde se ejecuta. Se crea un directorio "out" y luego creará un directorio dentro de "out" con el nombre del directorio donde está contenido el .shp y creará 100 js por cada 1 shp, luego elegirá el mejor dado que no tiene logica de predicción y creará un directorio "best". Allí se guardarán los js elegidos como mejores.

2- converter.py -> El script python importado, mejorado y ajustado para todos los casos detectados. Este no se ejecuta por consola, el script anterior se encarga de invocarlo tantas veces como sea necesario con los parámetros apropiados.

3- formatter.py -> (Opcional) Ejecutarlo en consola con python formatter.py. Aplica el formato legible a todos los archivos pero añadiéndole .fix como extensión. No es necesario pero ya está creado. Podés renombrarlos todos luego con TotalCmd con el renombrador múltiple (CTRL+M)
