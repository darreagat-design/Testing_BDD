const validEmail = 'usuario@demo.com';
const validPassword = 'Demo1234';

const form = document.getElementById('login-form');
const emailInput = document.getElementById('correo');
const passwordInput = document.getElementById('password');
const message = document.getElementById('message');

form.addEventListener('submit', (event) => {
  event.preventDefault();

  const email = emailInput.value.trim();
  const password = passwordInput.value;

  if (!email && !password) {
    showMessage('El correo y la contraseña son obligatorios', 'error');
  } else if (!email) {
    showMessage('El correo es obligatorio', 'error');
  } else if (!password) {
    showMessage('La contraseña es obligatoria', 'error');
  } else if (email === validEmail && password === validPassword) {
    showMessage('Bienvenido al sistema', 'success');
  } else {
    showMessage('Credenciales incorrectas', 'error');
  }
});

function showMessage(text, type) {
  message.textContent = text;
  message.className = `message ${type}`;
}
