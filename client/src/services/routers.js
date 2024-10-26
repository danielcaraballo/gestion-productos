import Navigo from 'navigo';

// Crear la instancia de Navigo
const router = new Navigo('/', { hash: false });

// Función para cargar las páginas dinámicamente
function loadPage(page, target = 'main-content') {
    const container = document.getElementById(target);
    
    if (!container) {
        console.error(`Elemento con id "${target}" no existe.`);
        return;
    }
    
    fetch(page)
        .then(response => {
            if (!response.ok) {
                throw new Error('Error al cargar la página: ' + response.statusText);
            }
            return response.text();
        })
        .then(html => {
            container.innerHTML = html;
        })
        .catch(error => console.error('Error al cargar la página:', error));
}

// Definir las rutas principales
router.on({
    '/sign-in': () => {
        loadPage('/src/pages/sign-in.html');  // Página de inicio de sesión
    },
    '/dashboard': () => {
        loadPage('/src/pages/dashboard.html');  // Página principal del dashboard
    },
    '/productos': () => {
        loadPage('/src/pages/products.html');  // Página de productos
    },
    '/configuracion': () => {
        loadPage('/src/pages/settings.html');  // Página de configuración
    },
    '*': () => {
        loadPage('/src/pages/404.html');  // Página no encontrada
    }
}).resolve();

// Asegúrate de que Navigo maneje los enlaces con data-navigo
router.updatePageLinks();
