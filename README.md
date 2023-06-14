# Agile@Bot: marco de trabajo para el desarrollo de agentes conversacionales

La administración pública española está actualmente inmersa en su proceso de transformación digital. Uno de los ejes estratégicos es la administración orientada a la ciudadanía con la creación de nuevos servicios digitales que mejoren la relación administración – ciudadanía. En este contexto, es donde aparecen los agentes conversacionales (o chatbots) como instrumento que facilita la tramitación administrativa a la ciudadanía.

Los agentes conversacionales no es algo nuevo, llevando tiempo entre nosotros y en constante evolución. En los últimos años, la Inteligencia Artificial ha resurgido de su olvido gracias a la evolución de la capacidad de computación, tanto es así que las técnicas de aprendizaje automático están siendo usadas para su desarrollo.

Las administraciones públicas están optando por los agentes conversacionales con inteligencia artificial como un nuevo canal de comunicación interactivo con la ciudadanía. Así pues, su implantación está siendo a través de la contratación pública, siendo código propietario de la empresa adjudicataria, y afectando la posibilidad de que la reutilización de código beneficie a otras administraciones: como la eficacia y la transferencia de conocimiento entre ellas.

Por otro lado, los proyectos software de desarrollo propio en las administraciones públicas están diseñados mediante modelos predictivos, como el modelo cascada, donde el coste, alcance y tiempo están cerrados de antemano. Además, el usuario hace uso del software al final de su desarrollo y no durante el mismo, mermando la capacidad de retroalimentación de forma frecuente, necesaria para poder cambiar las funcionalidades (requisitos) conforme se van demandando.

# Iterando con Agile@Bot

Va a partirse de la necesidad de un ayuntamiento de implantar un chatbot que proporcione formularios de descarga de los diferentes procedimientos administrativos disponibles en su sede electrónica.

En la reunión inicial de Agile Inception, todos los participantes como los stakeholders y el equipo Scrum definen de forma clara la visión de lo que se quiere realizar marcando unos objetivos y unas metas.

Al comienzo de la primera iteración, el equipo de desarrolladores escoge una historia de usuario priorizada por el Product Owner como la siguiente:

**Como**      Ciudadano

**Quiero**    Obtener un certificado de empadronamiento

**Para**      Tramitar la solicitud de dependencia

Esta historia de usuario será desglosada en diferentes tareas por los desarrolladores para logar alcanzar el objetivo del sprint. Al usar Rasa Open Source se tiene que definir las intenciones del usuario, las respuestas y acciones a ejecutar por el chatbot, añadiendo el código necesario a cada uno de losa archivos mencionados en el apartado anterior.
