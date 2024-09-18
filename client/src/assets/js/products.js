import CONFIG from "./config.js";

document.addEventListener('DOMContentLoaded', function() {
    fetchProducts();
});

// Función para obtener los productos desde la API
function fetchProducts() {
    axios.get(`${CONFIG.API_BASE_URL}/productos/productos/`)
        .then(response => {
            const products = response.data;
            if (products.length > 0) {
                populateTable(products);
            } else {
                showEmptyMessage();
            }
        })
        .catch(error => {
            console.error("Error al cargar los productos:", error);
            showErrorMessage();
        });
}

// Mostrar mensaje si no hay productos
function showEmptyMessage() {
    const tableBody = document.querySelector('.table-tbody');
    tableBody.innerHTML = '<tr><td colspan="7">No hay productos disponibles.</td></tr>';
}

// Mostrar mensaje de error en la UI
function showErrorMessage() {
    const tableBody = document.querySelector('.table-tbody');
    tableBody.innerHTML = '<tr><td colspan="7">Error al cargar los productos. Inténtalo de nuevo más tarde.</td></tr>';
}

// Función para generar una fila de la tabla
function generateRowHTML(product) {
    const tecnologiaTags = product.tecnologias.map(tecnologia => `
        <span class="tag">
          ${tecnologia.nombre}
        </span>
      `).join('');
    
    return `
      <tr>
        <td class="sort-nombre">${product.nombre}</td>
        <td class="sort-categoria">${product.categoria.nombre}</td>
        <td class="sort-tecnologias">
            <div class="tags-list">
                ${tecnologiaTags}
            </div>
        </td>
        
        <td class="sort-estatus">${product.estatus}</td>
        <td class="sort-url">${product.direccion_url}</td>
      </tr>
    `;
}

// Función para popular la tabla
function populateTable(products) {
    const tableBody = document.querySelector('.table-tbody');
    tableBody.innerHTML = ''; // Limpiar la tabla

    const fragment = document.createDocumentFragment();
    products.forEach(product => {
        const row = document.createElement('tr');
        row.innerHTML = generateRowHTML(product);
        fragment.appendChild(row);
    });

    tableBody.appendChild(fragment);
}

// Función para formatear la fecha Unix a un formato legible
function formatDate(unixTimestamp) {
    const date = new Date(unixTimestamp * 1000);
    return date.toLocaleDateString(); // Ajusta el formato según tus necesidades
}
