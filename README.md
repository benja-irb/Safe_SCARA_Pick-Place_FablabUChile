# Safe_SCARA_Pick-Place_FablabUChile

-----Git en desarrollo-----

Este repositorio incluye los códigos principales de funcionamiento del proyecto.

## Importante: 
requiere el uso de Python 3.11.5 o equivalente en el que funcionen las librerías:
- Mediapipe (mediapipe 0.10.8)
- Numpy (numpy 1.26.0)
- OpenCV (opencv-contrib-python 4.6.0.66)

## El proyecto...

Consiste en una rutina de pick & place realizada por un brazo robótico SCARA que es parte del Fablab de la Universidad de Chile. 

El objetivo principal es que el pick & place incluya una parte de visión computacional en la cual se detecta la pose de un objeto en una posición no definida usando como referencia marcadores AruCo. Además se implementa un sistema de seguridad con una segunda cámara la cual detecta manos mediante la librería OpenCV y Mediapipe con al finalidad de que si detecta alguna dentro del espacio de trabajo del robot, la rutina se detenga para que no exista riesgo de accidentes.

Este proyecto es realizado en el marco del curso ME5150-Robótica impartido por el profesor Harold Valenzuela, Ulises Campodónico, Leslie Cárdenas y Karen Quezada en el Departamento de Ingeniería Mecánica de la Universidad de Chile.
