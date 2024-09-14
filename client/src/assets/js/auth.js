// auth.js Maneja la autenticación general del usuario

// token.js contiene funciones para gestionar el token de autenticación
import { getToken, isAuthenticated, removeToken } from './token.js';

// Función para inicializar la página al cargar
function initPage() {
  // Verificar si el usuario está autenticado
  if (!isAuthenticated()) {
    redirectToSignIn();
  } else {
    console.log('Usuario autenticado');
    // Cargar datos protegidos de la API si es necesario
    fetchProtectedData();
  }
}

// Función para redirigir al usuario a la página de inicio de sesión
function redirectToSignIn() {
  window.location.href = '../pages/sign-in.html';
}

// Función para obtener datos protegidos de la API
function fetchProtectedData() {
  axios.get('http://localhost:8000/api/productos/', {
    headers: {
      'Authorization': `Bearer ${getToken()}`  // Incluir el token en el encabezado
    }
  })
    .then(response => {
      console.log('Datos protegidos:', response.data);
      // Procesar los datos y actualizar la página si es necesario
      updatePageWithData(response.data);
    })
    .catch(error => {
      console.error('Error al acceder a los datos protegidos:', error);
      handleAuthError(error);
    });
}

// Función para manejar errores de autenticación
function handleAuthError(error) {
  // Si el token es inválido o ha expirado, eliminarlo y redirigir al inicio de sesión
  removeToken();
  redirectToSignIn();
}

// Función para actualizar la página con datos protegidos
function updatePageWithData(data) {
  // Aquí puedes implementar la lógica para mostrar los datos en la página
  console.log('Actualizando la página con datos:', data);
}

// Función para manejar el cierre de sesión
function setupSignOutButton() {
  const signoutButton = document.getElementById('signout-button');

  if (signoutButton) {
    signoutButton.addEventListener('click', () => {
      removeToken();
      redirectToSignIn();
    });
  }
}

// Inicializar la lógica de la página cuando se carga
window.onload = function () {
  initPage();
  setupSignOutButton();
};
