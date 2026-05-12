Playwright & Python - Full-Stack Automation Framework 🚀
========================================================

Este repositorio contiene una arquitectura de pruebas automatizadas de nivel profesional, diseñada para ser escalable, mantenible y de alto rendimiento. El framework cubre tanto la interfaz de usuario (UI) como la validación de servicios web (API).

🚀 Características Principales
------------------------------

*   **Page Object Model (POM):** Desacoplamiento completo entre la lógica de la aplicación y los scripts de prueba para facilitar el mantenimiento.
    
*   **Pruebas de API (REST):** Cobertura completa de métodos HTTP (**GET, POST, PUT, DELETE**) utilizando Playwright Request Context.
    
*   **Gestión de Evidencias:** Captura automatizada de **Screenshots y Videos** ante fallos para una depuración rápida.
    
*   **Pipeline CI/CD:** Integración total con GitHub Actions (Node.js 24 / Python 3.11) para ejecución automática en cada push.
    
*   **Reportes Profesionales:** Generación de reportes HTML detallados y autocontenidos después de cada ejecución.
    

📂 Estructura del Proyecto
--------------------------

*   .github/workflows/: Configuración del pipeline de Integración Continua (CI).
    
*   pages/: Clases Page Object que encapsulan los elementos y acciones de la UI (e.g., LoginPage, InventoryPage).
    
*   tests/: Suites de pruebas categorizadas:
    
    *   test\_ui\_login.py: Flujos de autenticación (casos positivos y negativos).
        
    *   test\_ui\_purchase.py: Flujo de fin a fin (E2E) de compra en la tienda.
        
    *   test\_api.py: Validaciones de servicios REST.
        
    *   test\_connectivity.py: Smoke tests de conectividad inicial.
        
    *   test\_trigger\_failure.py: Test de control diseñado para validar la captura de evidencias.
        
*   requirements.txt: Lista de dependencias del proyecto.
    
*   pytest.ini: Configuración global de ejecución y evidencias.
    

🛠️ Instalación y Uso Local
---------------------------

1.  Bashgit clone https://github.com/gokayeris/playwright-python-automation.gitcd playwright-python-automation
    
2.  Bashpip install -r requirements.txtplaywright install
    
3.  PlaintextSAUCE\_USER=standard\_userSAUCE\_PASSWORD=secret\_sauce
    
4.  Bash# Ejecutar todos los tests y generar reportepytest --html=reporte\_final.html --self-contained-html
    

📈 Gestión de Evidencias
------------------------

El framework está configurado para proporcionar visibilidad total sobre los fallos:

*   **Screenshots:** Se guardan automáticamente en la carpeta screenshots/ cuando un test falla.
    
*   **Videos:** Se retienen grabaciones de la sesión ante fallos en la carpeta test-results/.
    
*   **Test de Validación:** El archivo test\_trigger\_failure.py asegura que el sistema de reportes esté siempre operativo.
    

Desarrollado por **Gokay Eris** - QA Automation Engineer.