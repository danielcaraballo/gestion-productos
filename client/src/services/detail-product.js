import CONFIG from "./config.js";

document.addEventListener("DOMContentLoaded", () => {
  document.body.addEventListener("click", (event) => {
    const target = event.target.closest(".open-modal");

    if (target) {
      const productId = target.getAttribute("data-product-id");

      // Obtener los elementos del modal
      const modalTitle = document.querySelector("#modal-simple .modal-title");
      const modalDescription = document.querySelector("#modal-description");
      const modalReleaseDate = document.querySelector("#modal-release-date");
      const modalCategory = document.querySelector("#modal-category");
      const modalRequester = document.querySelector("#modal-requester");
      const modalStatus = document.querySelector("#modal-status");
      const modalTechnologies = document.querySelector("#modal-technologies");
      const modalResponsibles = document.querySelector("#modal-responsibles");
      const modalUrlButton = document.querySelector("#modal-url-button");

      if (!modalTitle) {
        console.error("No se encontraron los elementos del modal.");
        return;
      }

      axios
        .get(`${CONFIG.API_BASE_URL}/productos/productos/${productId}/detail/`)
        .then((response) => {
          const productData = response.data;
          console.log(response.data); // Inspecciona la estructura de los datos

          // Llenar el modal con los datos del producto
          modalTitle.textContent = productData.nombre;
          modalDescription.textContent = productData.descripcion;
          modalReleaseDate.textContent = productData.fecha_lanzamiento;
          modalCategory.textContent = productData.categoria.nombre;

          // Formato del solicitante
          const requesterName =
            productData.solicitante.nombre || "Solicitante no asignado";
          const requesterLastName = productData.solicitante.apellido || " ";
          const requesterDepartment =
            productData.solicitante.dependencia.nombre ||
            "Dependencia no asignada";
          modalRequester.textContent = `${requesterName} ${requesterLastName} (${requesterDepartment})`;

          modalStatus.textContent = productData.estatus.nombre;
          modalTechnologies.textContent = productData.tecnologias
            .map((t) => t.nombre)
            .join(", ");

          // Manejar la relación con responsables desde la tabla intermedia
          if (
            Array.isArray(productData.responsables) &&
            productData.responsables.length > 0
          ) {
            modalResponsibles.textContent = productData.responsables
              .map((r) => r.nombre)
              .join(", ");
          } else {
            modalResponsibles.textContent = "No responsables asignados";
          }

          // Configurar el enlace del botón
          modalUrlButton.href = productData.direccion_url;
        })
        .catch((error) => {
          console.error("Error al obtener los detalles del producto:", error);
        });
    }
  });
});
