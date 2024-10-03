import CONFIG from "./config.js";

window.onload = function() {
    // Llamada para obtener los datos de estatus de productos
    axios.get(`${CONFIG.API_BASE_URL}/productos/producto-estatus-count/`)
      .then(response => {
        const data = response.data;
        
        // Actualizar los contadores en el DOM
        document.getElementById('contador-operativos').textContent = `${data.operativo} Productos`;
        document.getElementById('contador-mantenimiento').textContent = `${data.mantenimiento} Productos`;
        document.getElementById('contador-inactivos').textContent = `${data.inactivo} Productos`;
        document.getElementById('contador-retirados').textContent = `${data.retirado} Productos`;
      })
      .catch(error => {
        console.error('Error al obtener los datos de estatus de productos:', error);
      });
  };
