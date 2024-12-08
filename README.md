# Proyecto: Bot de Publicación en Fansly

Este proyecto es un bot automatizado que utiliza Selenium para realizar publicaciones en la plataforma de Fansly. El bot selecciona un archivo aleatorio desde una carpeta, genera una descripción personalizada y realiza la publicación automáticamente.

## Características Principales

1. **Automatización de Publicaciones:** Publica contenido en Fansly de forma automatizada.
2. **Selección Aleatoria de Archivos:** Selecciona imágenes o videos de una carpeta para subir.
3. **Generación de Descripciones:** Crea descripciones genéricas para las publicaciones.
4. **Interacción Simulada:** Emula interacciones humanas para evitar ser detectado como bot.
5. **Gestión de Errores:** Registra errores en un archivo de log y guarda el HTML de la página para depuración.

## Requisitos del Sistema

- **Sistema Operativo:** Compatible con Windows.
- **Python:** Versión 3.7 o superior.
- **Librerías Python:**
  - `selenium`
  - `logging`
- **Navegador:** Brave (configurado para funcionar con el perfil del usuario).

## Instalación

1. **Instala Python:** Asegúrate de tener Python instalado en tu sistema. Descárgalo desde [python.org](https://www.python.org/).
2. **Instala las dependencias necesarias:**
   ```bash
   pip install selenium
   ```
3. **Descarga el Driver de Chrome:**
   - Descarga el driver desde [ChromeDriver](https://chromedriver.chromium.org/downloads).
   - Asegúrate de que la versión coincida con tu navegador Brave.
   - Configura la ruta del driver en la variable `CHROME_DRIVER_PATH`.
4. **Configura Brave:**
   - Asegúrate de que `BRAVE_USER_DATA` y `BRAVE_PATH` estén correctamente configurados en el código.
5. **Configura la carpeta de archivos:**
   - Define la ruta a la carpeta que contiene los archivos a publicar en la variable `IMAGES_FOLDER`.

## Uso

1. **Ejecuta el bot:**
   - Abre una terminal en el directorio del script y ejecuta:
     ```bash
     python fansly_bot.py
     ```
2. **Proceso:**
   - El bot iniciará sesión en Fansly utilizando el perfil del navegador Brave.
   - Seleccionará un archivo aleatorio de la carpeta configurada.
   - Generará una descripción para el archivo.
   - Publicará el archivo en tu perfil de Fansly.

## Estructura del Código

### 1. `iniciar_sesion()`

- **Propósito:** Inicia sesión en Fansly utilizando el perfil del navegador Brave.
- **Detalles:**
  - Abre la página de inicio de sesión y espera a que los elementos necesarios estén disponibles.

### 2. `seleccionar_archivo_azar(carpeta)`

- **Propósito:** Selecciona un archivo aleatorio de una carpeta.
- **Detalles:**
  - Filtra archivos válidos (imágenes y videos).
  - Retorna la ruta del archivo seleccionado.

### 3. `escribir_descripcion_y_publicar(archivo, descripcion)`

- **Propósito:** Sube un archivo, escribe una descripción y publica en Fansly.
- **Detalles:**
  - Emula interacción humana para escribir descripciones y presionar botones.
  - Registra cada acción en el log.

### 4. `generar_descripcion()`

- **Propósito:** Genera una descripción genérica para las publicaciones.
- **Detalles:**
  - Devuelve una descripción atractiva y profesional.

### 5. `guardar_html()`

- **Propósito:** Guarda el HTML de la página actual en caso de error.
- **Detalles:**
  - Útil para depurar problemas durante la ejecución del bot.

## Personalización

- **Extensiones Válidas:** Ajusta las extensiones permitidas en la función `seleccionar_archivo_azar`.
- **Mensajes Personalizados:** Modifica la función `generar_descripcion` para cambiar las descripciones predeterminadas.

## Notas Importantes

- **Sesión Activa:** Asegúrate de que el perfil de Brave configurado esté activo y tenga acceso a Fansly.
- **Gestión de Errores:** Revisa el archivo `fansly_bot_logs.txt` para depurar errores.
- **HTML Guardado:** Si ocurre un error, consulta el archivo `error_page.html` para más información sobre el estado de la página.


