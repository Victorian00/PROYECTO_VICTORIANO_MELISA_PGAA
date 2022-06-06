%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

HOLA! Bienvenido a nuestro proyecto, encantado de tenerte por aquí

Nosotros somos Melisa Yanes Guillermo y Victoriano Fernández Tomás, 
dos alumnos del Grado en Ingeniería Aeroespacial de la Universidad 
Politécnica de Madrid. A continuación, vamos a comentarte unas 
cuantas cosas sobre el proyecto y dar un poco de información

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

INFORMACIÓN:

- Nombre del proyecto: Best Friends For Blinds
- Autores: Melisa Yanes Guillermo y Victoriano Fernández Tomás
- Grado: Grado en Ingeniería Aeroespacial 
- Universidad: Universidad Politécnica de Madrid
- Asignatura: Programación Gráfica de Aplicaciones en Python y Javascript
- Curso: 4º Curso 
- Año: 2021/2022
- Profesores: Luis Izquierdo Mesa y Sergio Ávila Sánchez


%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

CARACTERÍSTICAS DEL PROYECTO Y SU ÓPTIMO FUNCIONAMIENTO:

Éste proyecto consiste en una página web en la que puedes, en los distintos 
apartados, por una tomar una foto y recibirla en pantalla tras haber sido analizada 
para señalarte los objetos que aparecen en dicha foto, y por otra parte 
acceder en tiempo real a la cámara de tu teléfono y mostrarte los colores de los 
objetos a los que estás apuntando con la cámara. 

Principalmente, consta de cuatro archivos html referentes a los cuatro apartados de la página y 
un archivo de Phyton referente al servidor que soporta la página web .Cabe destacar que 
la versión en la que se ha realizado este proyecto es Python 3.9.9, y es muy importante 
que si ejecutas el código en tu ordenador, es NECESARIO instalar las extensiones mencionadas 
en la parte superior deel archivo Python, si no las tiene tu PC no funcionará. Lo característico 
de este trabajo es que utiliza funciones de Javascript para obtener permisos para 
acceder a la cámara del dispositivo, por lo que era necesario establecer un servidor 
seguro https para que funcionase correctamente. Por ello, es posible percatarse de los 
archivos "localhost.key", "localhost.pem", "server.key" y "server.csr", archivos 
en los que están escritas las claves necesarias para el funcionamiento correcto 
del servidor. Es por esto que al ejecutar el archivo de Python, nos pide una clave "PEM". 
Dicha clave es una contraseña establecida en el momento en el que se obtuvieron los 
cuatro archivos mencionados anteriormente. En este caso, la contraseña es "12345", en 
mayúsculas, sin comillas y todo junto. Igualmente, la contraseña de este y otros permisos 
se encuentra en el archivo "settings.json" de la carpeta ".vscode".


%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

CÓMO EJECUTAR EL CÓDIGO:

Para ejecutar correctamente el código se seguirás los siguientes pasos:
    - Abrir el archivo "servidor.py" en una ventana de VSCode
    - Cerciorarse de que los paquetes utilizados en la cabecera están instalados
    - Ejecutar el archivo en el terminal
    - Introducir la contraseña requerida (en este caso es 12345)
    - Aparecerá un link, al cuál te redirigirá si pulsas Ctl y clickas en dicho link
    - Si se siguen todos los pasos llegarás a la página deseada
    - Por último, disfruta del contenido mostrado


%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

ACERCA DEL PROYECTO:

Este ptoyecto surgió con la idea de ayudar a las personas ciegas en su día 
a día. Aunque en dicho proyecto, el reconocimiento de imagenes se realiza 
con fotos tomadas por el usuario y con texto escrito, en un futuro se 
pretende implementar la detección de imágenes en tiempo real y la descripción 
de imágenes por voz.





