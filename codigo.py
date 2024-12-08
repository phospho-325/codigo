import os
import random
import logging
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time

# Configuración de logs
LOG_FILE = "fansly_bot_logs.txt"
logging.basicConfig(filename=LOG_FILE, level=logging.INFO, format="%(asctime)s - %(message)s")

# Rutas importantes
CHROME_DRIVER_PATH = r"D:\010111010\python\bot-fansly\chromedriver-win64\chromedriver-win64\chromedriver.exe"
IMAGES_FOLDER = r"D:\010111010\algo\de nuevo\imagenes probidia"

BRAVE_USER_DATA = r"C:\Users\jesus\AppData\Local\BraveSoftware\Brave-Browser\User Data"
BRAVE_PATH = r"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe"

# Configuración de ChromeDriver con Brave
options = Options()
options.binary_location = BRAVE_PATH
options.add_argument(f"--user-data-dir={BRAVE_USER_DATA}")
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument("--start-maximized")

service = Service(CHROME_DRIVER_PATH)
driver = webdriver.Chrome(service=service, options=options)

def seleccionar_archivo_azar(carpeta):
    """Selecciona un archivo al azar de una carpeta."""
    archivos = [f for f in os.listdir(carpeta) if f.endswith(('.jpg', '.jpeg', '.png', '.gif', '.mp4'))]
    if archivos:
        archivo_seleccionado = random.choice(archivos)
        logging.info(f"Archivo seleccionado: {archivo_seleccionado}")
        return os.path.join(carpeta, archivo_seleccionado)
    logging.error("No se encontraron archivos válidos en la carpeta.")
    return None

def iniciar_sesion():
    """Inicia sesión en Fansly."""
    try:
        driver.get("https://fansly.com")
        logging.info("Página cargada correctamente.")

        # Esperar que el área de texto esté disponible
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "textarea"))
        )
        logging.info("Sesión detectada, listo para proceder.")
    except Exception as e:
        logging.error(f"Error durante la sesión: {e}")
        guardar_html()
        finalizar_bot()

def escribir_descripcion_y_publicar(archivo, descripcion):
    """Escribe la descripción, sube el archivo y publica en Fansly."""
    try:
        # Seleccionar el área de texto para escribir la descripción
        textarea = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "textarea"))
        )
        logging.info("Área de texto encontrada.")
        
        # Escribir la descripción simulando interacción humana
        actions = ActionChains(driver)
        actions.move_to_element(textarea).click().send_keys(descripcion).perform()
        time.sleep(2)  # Pausa para asegurar escritura

        # Subir el archivo
        file_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "input[type='file']"))
        )
        file_input.send_keys(archivo)
        logging.info(f"Archivo {archivo} cargado correctamente.")
        time.sleep(5)  # Esperar a que se cargue el archivo

        # Presionar el botón "Cargar"
        cargar_boton = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button.upload-confirm-btn"))
        )
        cargar_boton.click()
        logging.info("Botón 'Cargar' presionado.")
        time.sleep(3)  # Esperar después de cargar

        # Presionar el botón "Publicar"
        publicar_boton = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button.btn.new-post-btn"))
        )
        publicar_boton.click()
        logging.info("Publicación realizada con éxito.")
    except Exception as e:
        logging.error(f"Error durante la publicación: {e}")
        guardar_html()

def generar_descripcion():
    """Genera una descripción genérica para la publicación."""
    descripcion = "🌟 Descubre contenido exclusivo y provocador. ¡No te lo pierdas! 🌟"
    logging.info(f"Descripción generada: {descripcion}")
    return descripcion

def guardar_html():
    """Guarda el HTML de la página actual para depuración."""
    try:
        with open("error_page.html", "w", encoding="utf-8") as f:
            f.write(driver.page_source)
        logging.info("HTML de la página guardado para depuración.")
    except Exception as e:
        logging.error(f"Error al guardar el HTML: {e}")

def finalizar_bot():
    """Deja el navegador abierto para inspección."""
    logging.info("Bot finalizado. El navegador permanecerá abierto.")
    input("Presiona Enter para cerrar el navegador...")
    driver.quit()

if __name__ == "__main__":
    logging.info("Iniciando bot de publicación en Fansly...")
    try:
        iniciar_sesion()
        archivo = seleccionar_archivo_azar(IMAGES_FOLDER)
        if archivo:
            descripcion = generar_descripcion()
            escribir_descripcion_y_publicar(archivo, descripcion)
    except Exception as e:
        logging.error(f"Error inesperado: {e}")
    finally:
        finalizar_bot()
