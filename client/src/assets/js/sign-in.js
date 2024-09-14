import { setToken } from './token.js';

// Función para manejar el envío del formulario
function handleFormSubmit(event) {
  event.preventDefault();  // Evitar comportamiento por defecto del formulario

  const username = document.getElementById('username').value.trim();  // Obtener y limpiar el valor del nombre de usuario
  const password = document.getElementById('password').value.trim();  // Obtener y limpiar el valor de la contraseña

  if (!username || !password) {
    displayError('Por favor, complete todos los campos.');
    return;
  }

  // Hacer la petición POST para iniciar sesión
  loginUser(username, password);
}

// Función para iniciar sesión y manejar la respuesta
function loginUser(username, password) {
  axios.post('http://localhost:8000/api/token/', { username, password })
    .then(response => {
      const { access: token } = response.data;  // Desestructurar el token de la respuesta
      setToken(token);  // Guardar el token usando la función de token.js

      // Redirigir a una página protegida tras el inicio de sesión exitoso
      window.location.href = 'dashboard.html';
    })
    .catch(error => {
      console.error('Error en la autenticación:', error);
      displayError('Usuario o contraseña incorrectos');
    });
}

// Función para mostrar mensajes de error en la interfaz
function displayError(message) {
  const errorMessageElement = document.getElementById('error-message');
  if (errorMessageElement) {
    errorMessageElement.innerText = message;
  } else {
    console.warn('Elemento de mensaje de error no encontrado.');
  }
}

// Configurar el evento de envío del formulario
document.getElementById('form-signin').addEventListener('submit', handleFormSubmit);
