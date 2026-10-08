Feature: Inicio de sesión
  Como usuario del sistema
  Quiero iniciar sesión con mis credenciales
  Para acceder a las funciones protegidas

  Scenario: Inicio de sesión exitoso
    Given que estoy en la página de inicio de sesión
    When ingreso el correo "usuario@demo.com"
    And ingreso la contraseña "Demo1234"
    And presiono el botón "Iniciar sesión"
    Then debería ver el mensaje "Bienvenido al sistema"

  Scenario: Contraseña incorrecta
    Given que estoy en la página de inicio de sesión
    When ingreso el correo "usuario@demo.com"
    And ingreso la contraseña "Incorrecta123"
    And presiono el botón "Iniciar sesión"
    Then debería ver el mensaje "Credenciales incorrectas"

  Scenario: Usuario inexistente
    Given que estoy en la página de inicio de sesión
    When ingreso el correo "otro@demo.com"
    And ingreso la contraseña "Demo1234"
    And presiono el botón "Iniciar sesión"
    Then debería ver el mensaje "Credenciales incorrectas"

  Scenario: Correo vacío
    Given que estoy en la página de inicio de sesión
    When dejo el correo vacío
    And ingreso la contraseña "Demo1234"
    And presiono el botón "Iniciar sesión"
    Then debería ver el mensaje "El correo es obligatorio"

  Scenario: Contraseña vacía
    Given que estoy en la página de inicio de sesión
    When ingreso el correo "usuario@demo.com"
    And dejo la contraseña vacía
    And presiono el botón "Iniciar sesión"
    Then debería ver el mensaje "La contraseña es obligatoria"

  Scenario: Correo y contraseña vacíos
    Given que estoy en la página de inicio de sesión
    When dejo el correo vacío
    And dejo la contraseña vacía
    And presiono el botón "Iniciar sesión"
    Then debería ver el mensaje "El correo y la contraseña son obligatorios"
