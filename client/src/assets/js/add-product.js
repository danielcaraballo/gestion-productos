document.addEventListener("DOMContentLoaded", function () {
  const form = document.getElementById("add-product-form");
  let currentStep = 1;

  // Función para manejar el cambio de paso
  const showStep = (step) => {
    // Ocultar todos los pasos
    document.querySelectorAll(".step").forEach((stepDiv) => {
      stepDiv.style.display = "none";
    });

    // Mostrar solo el paso actual
    document.getElementById(`step-${step}`).style.display = "block";
  };

  // Mostrar el primer paso al cargar el modal
  showStep(currentStep);

  // Botón "Siguiente" del Paso 1
  document.getElementById("nextStep1").addEventListener("click", function () {
    currentStep = 2;
    showStep(currentStep);
  });

  // Botón "Siguiente" del Paso 2
  document.getElementById("nextStep2").addEventListener("click", function () {
    currentStep = 3;
    showStep(currentStep);
  });

  // Botón "Anterior" del Paso 2
  document.getElementById("prevStep2").addEventListener("click", function () {
    currentStep = 1;
    showStep(currentStep);
  });

  // Botón "Anterior" del Paso 3
  document.getElementById("prevStep3").addEventListener("click", function () {
    currentStep = 2;
    showStep(currentStep);
  });

  // Manejar el envío del formulario al agregar el producto
  form.addEventListener("submit", function (event) {
    event.preventDefault(); // Prevenir la recarga de la página

    // Obtener los valores del formulario
    const newProduct = {
      nombre: document.getElementById("nombre").value,
      categoria: document.getElementById("categoria").value,
      tecnologias: document.getElementById("tecnologias").value,
      estatus: document.getElementById("estatus").value,
      url: document.getElementById("url").value,
    };

    // Validar los campos (ejemplo básico)
    if (
      !newProduct.nombre ||
      !newProduct.categoria ||
      !newProduct.tecnologias ||
      !newProduct.url
    ) {
      document.getElementById("form-messages").innerText =
        "Todos los campos son obligatorios.";
      return;
    }

    // Enviar la petición a la API
    axios
      .post(`${CONFIG.API_BASE_URL}/productos/productos`, newProduct)
      .then((response) => {
        console.log("Producto agregado:", response.data);
        document.getElementById("form-messages").innerText =
          "Producto agregado exitosamente";
        form.reset(); // Limpiar el formulario
        currentStep = 1; // Reiniciar el formulario al primer paso
        showStep(currentStep); // Volver al paso 1
      })
      .catch((error) => {
        console.error("Error al agregar producto:", error);
        document.getElementById("form-messages").innerText =
          "Error al agregar el producto";
      });
  });
});
