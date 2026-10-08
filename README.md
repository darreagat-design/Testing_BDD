# Testing y BDD - Login

## Objetivo
Implementar un piloto de inicio de sesión y automatizar sus escenarios mediante BDD, conectando las reglas de negocio con pruebas verificables en el navegador.

## Piloto seleccionado
El flujo crítico seleccionado fue el inicio de sesión de usuario, desde el ingreso del correo y la contraseña hasta la visualización del resultado.

## Taller de los tres amigos
- **Negocio** define las reglas de acceso, los datos válidos y los mensajes esperados.
- **Desarrollo** implementa el formulario web y su comportamiento con HTML, CSS y JavaScript.
- **QA** transforma las reglas en escenarios Gherkin verificables y los automatiza.

## Reglas del login
- **Usuario válido:** `usuario@demo.com`.
- **Contraseña válida:** `Demo1234`.
- **Credenciales incorrectas:** un correo inexistente o una contraseña incorrecta muestra `Credenciales incorrectas`.
- **Correo obligatorio:** si el correo está vacío, muestra `El correo es obligatorio`.
- **Contraseña obligatoria:** si la contraseña está vacía, muestra `La contraseña es obligatoria`.
- **Ambos campos obligatorios:** si ambos están vacíos, muestra `El correo y la contraseña son obligatorios`.
- Cuando ambas credenciales son válidas, muestra `Bienvenido al sistema`.

## Escenarios BDD
El archivo `features/login.feature` define estos seis escenarios:
1. Inicio de sesión exitoso
2. Contraseña incorrecta
3. Usuario inexistente
4. Correo vacío
5. Contraseña vacía
6. Correo y contraseña vacíos

## Automatización
Los escenarios se automatizan con:
- pytest como ejecutor de pruebas.
- pytest-bdd para vincular los escenarios Gherkin con sus pasos automatizados.
- Selenium WebDriver para interactuar con el formulario.
- Chrome en modo headless para ejecutar las pruebas sin mostrar una ventana del navegador.

## Estructura del proyecto
```text
Testing_BDD/
├── .github/
│   └── workflows/
│       └── tests.yml
├── app/
│   ├── login.html
│   ├── login.js
│   └── styles.css
├── features/
│   └── login.feature
├── tests/
│   └── test_login.py
├── requirements.txt
└── README.md
```

## Cómo instalar dependencias
Desde la raíz del proyecto:
```bash
pip install -r requirements.txt
```

## Cómo ejecutar las pruebas
Desde la raíz del proyecto:
```bash
pytest
```

## Resultado esperado
```text
6 passed
```

## Evidencias sugeridas
- Login abierto en el navegador.
- Inicio de sesión exitoso con el mensaje de bienvenida.
- Login con un error y su mensaje correspondiente.
- Archivo `features/login.feature` con los seis escenarios.
- Archivo `tests/test_login.py` con las definiciones de pasos.
- Terminal ejecutando `pytest` y mostrando `6 passed`.

## Revisión tras el sprint
Después de implementar y ejecutar los escenarios, se revisó que las reglas de negocio coincidieran con los escenarios Gherkin. Los seis casos principales del flujo de inicio de sesión quedaron cubiertos correctamente.

## Sprint 4: Integración continua con GitHub Actions
GitHub Actions ejecuta automáticamente las pruebas BDD mediante el workflow `.github/workflows/tests.yml` cada vez que se realiza un `push` o se abre/actualiza un `pull request`. El workflow prepara Python 3.12 y Chrome, instala las dependencias desde `requirements.txt` y corre `pytest`. El resultado esperado es que pasen los 6 escenarios.
