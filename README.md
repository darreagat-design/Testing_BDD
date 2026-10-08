# Testing y BDD - Login

**Repositorio:** Pegar aquí la URL del repositorio.

## Objetivo
Construir un piloto web de inicio de sesión y automatizar su flujo crítico con escenarios BDD y Selenium.

El login usa las credenciales de demostración `usuario@demo.com` y `Demo1234`. Informa el acceso exitoso, las credenciales incorrectas y los campos obligatorios vacíos.

## Escenarios
Los seis escenarios de `features/login.feature` cubren:
- Inicio de sesión exitoso.
- Contraseña incorrecta.
- Usuario inexistente.
- Correo vacío.
- Contraseña vacía.
- Correo y contraseña vacíos.

## Instalación y ejecución
Instalar dependencias:
```bash
pip install -r requirements.txt
```

Ejecutar las pruebas desde la raíz del proyecto:
```bash
pytest
```

Resultado esperado: `6 passed`.

## CI/CD
GitHub Actions ejecuta `pytest` automáticamente en cada `push` y `pull_request`. El workflow configura Ubuntu, Python 3.12 y Chrome. Configuración: `.github/workflows/tests.yml`.

## Evidencias
Las capturas de ejecución de tests y CI/CD están en `Evidencias/`:
- [Pruebas pytest exitosas](Evidencias/Tests_exitosos_pytest.png)
- [Workflow CI/CD en ejecución](Evidencias/Workflow_CICD_corriendo.png)
- [Workflow CI/CD completado](Evidencias/Workflow_CICD_completado.png)
