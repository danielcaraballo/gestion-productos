import CONFIG from "./config.js";

document.addEventListener("DOMContentLoaded", () => {
  document.body.addEventListener("click", (event) => {
    const target = event.target.closest(".open-modal");

    if (target) {
      // Si el enlace clicado tiene la clase .open-modal, procedemos
      const productId = target.getAttribute("data-product-id");
      console.log("Se hizo clic en el producto con ID:", productId); // Confirmación en consola

      const modalTitle = document.querySelector("#modal-simple .modal-title");
      const modalBody = document.querySelector("#modal-simple .modal-body");

      if (!modalTitle || !modalBody) {
        console.error("No se encontraron los elementos del modal.");
        return;
      }

      axios
        .get(`${CONFIG.API_BASE_URL}/productos/productos/${productId}/`)
        .then((response) => {
          const productData = response.data;
          console.log("Datos del producto obtenidos:", productData); // Imprimir datos obtenidos
          modalTitle.textContent = productData.nombre;
          modalBody.textContent = productData.descripcion;
        })
        .catch((error) => {
          console.error("Error al obtener los detalles del producto:", error);
        });
    }
  });
});
