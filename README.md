# QA Automation - SauceDemo Testing

## Propósito del Proyecto

Este proyecto implementa pruebas automatizadas tanto para la interfaz web como para la API. Las pruebas cubren funcionalidades clave como:

UI: Login exitoso, login incorrecto (escenario negativo), navegación del catálogo, agregar productos al carrito y el proceso completo de checkout en SauceDemo (https://www.saucedemo.com/).

API: Pruebas de endpoints públicos (JSONPlaceholder) usando los métodos GET, POST y DELETE para validar que los servicios respondan correctamente.

## Tecnologías Utilizadas

- **Python**: Lenguaje de programación principal
- **Selenium WebDriver**: Para automatización de navegador web
- **Requests**: Para hacer las peticiones y pruebas de la API
- **pytest**: Framework de testing para Python
- **pytest-html**: Para generar el reporte visual en HTML
- **webdriver-manager**: Gestión automática de drivers de navegador
- **Chrome Browser**: Navegador utilizado para las pruebas
- **Faker**: Para generar datos aleatorios en las pruebas


## Estructura del proyecto
├── data/               # Fuentes de datos y archivos de configuración para pruebas

├── logs/               # Registros históricos del sistema de logging (.log)

├── page/               # Clases y localizadores de Page Object Model (UI)

├── reporte/            # Reporte de Pytest y capturas de pantalla (.html y .png)

│   └── screenshots/    # Evidencias automáticas ante fallas de tests

├── test/               # Casos de prueba automatizados (UI y API)

├── utils/              # Helpers y configuración de drivers (get_driver)

├── conftest.py         # Configuración global de fixtures, hooks y capturas de Pytest

├── pytest.ini          # Parámetros de ejecución por defecto de Pytest

└── requirements.txt    # Lista de dependencias del proyecto

## Instalación de Dependencias

### Prerrequisitos
- Python 3.10 o superior instalado.

- Google Chrome instalado en el sistema.


### Instalación

1. Clona o descarga este repositorio
2. Abrir la terminal en la raíz del proyecto y ejecutar:

pip install -r requirements.txt


## Ejecución de las Pruebas

Para ejecutar todas las pruebas, abrir la terminal y ejecutar el siguiente comando estando en la raíz del proyecto:

pytest -v


(El proyecto esta preparado para en caso de fallar algun test generar el screenshot,
para testearlo modificar algun valor en los test, de modo tal que el test falle para
poder comprobar esto, yo deje todos los test para que pasen)
