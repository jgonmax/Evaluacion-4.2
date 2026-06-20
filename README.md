Evaluación Sumativa 4.2 - Desarrollo de Software para Hardware (DCSH01)
Información del Estudiante
Nombre: Jesus Gonzalez Mardonez

Asignatura: Desarrollo de Software para Hardware (DCSH01)

Institución: INACAP

Fecha de Entrega: Junio 2026

Resumen del Proyecto
Este proyecto presenta una solución de software basada en Flask, diseñada para funcionar como un centro de control y monitoreo geométrico. La aplicación está optimizada para capturar coordenadas espaciales X e Y enviadas desde una aplicación móvil externa, procesando estos datos en el backend para proyectarlos dinámicamente en una matriz digital de 4x4.

Arquitectura de Navegación Circular
La interfaz ha sido diseñada bajo un modelo de navegación en anillo, conectando tres módulos funcionales para una experiencia de usuario continua:

Dashboard Principal: Portada técnica del proyecto, identificación del estudiante y visualización de la matriz con estado de celdas en tiempo real.

Visualización Alternativa (Radar): Interfaz esférica tipo sonar que utiliza transformaciones CSS para representar los datos de forma inmersiva.

Visualización de Diagnóstico (Panel Industrial): Tabla de gestión de sensores que interpreta las coordenadas recibidas y las categoriza bajo estados lógicos de alerta (OK / CRÍTICO).

Cumplimiento de Especificaciones Técnicas
El desarrollo se ajusta estrictamente a los requerimientos de la rúbrica:

Lógica sin JavaScript: La interactividad y el renderizado se gestionaron exclusivamente mediante el motor de plantillas Jinja en el lado del servidor.

Integración de Estilos: El código CSS fue implementado íntegramente dentro de la etiqueta <head> de cada archivo HTML.

Selectores CSS: Se utilizó un diseño basado exclusivamente en atributos id, descartando el uso de selectores de clase (.) para asegurar la singularidad de los elementos.

Entorno de Red: El servidor fue desplegado bajo una configuración NAT con Reenvío de Puertos (Port Forwarding), asegurando un entorno de ejecución controlado y seguro.

Referencias y Aportes
Visualización de datos y lógica base: Desarrollo original realizado en su totalidad conforme a los requerimientos técnicos y creativos solicitados.
