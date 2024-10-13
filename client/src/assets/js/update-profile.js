import CONFIG from "./config.js";

// Función para actualizar el perfil del usuario
async function updateProfile(profileData) {
  try {
    const response = await axios.put(
      `${CONFIG.API_BASE_URL}/usuarios/update-profile/`,
      profileData,
      {
        headers: {
          Authorization: `Bearer ${localStorage.getItem("token")}`,
        },
      }
    );
    console.log("Perfil actualizado:", response.data);
  } catch (error) {
    console.error("Error al actualizar el perfil:", error.response.data);
  }
}

// Captura el formulario de actualización de perfil
document
  .getElementById("updateProfileForm")
  .addEventListener("submit", async function (event) {
    event.preventDefault(); // Evita que el formulario se envíe de manera convencional

    const profileData = {
      username: document.getElementById("username").value,
      first_name: document.getElementById("first_name").value,
      last_name: document.getElementById("last_name").value,
      email: document.getElementById("email").value,
    };

    await updateProfile(profileData);
  });

// Función para cambiar la contraseña
async function changePassword(passwordData) {
  try {
    const response = await axios.post(
      `${CONFIG.API_BASE_URL}/usuarios/change-password/`,
      passwordData,
      {
        headers: {
          Authorization: `Bearer ${localStorage.getItem("token")}`,
        },
      }
    );
    console.log("Contraseña cambiada:", response.data);
  } catch (error) {
    console.error("Error al cambiar la contraseña:", error.response.data);
  }
}

// Captura el formulario de cambio de contraseña
document
  .getElementById("changePasswordForm")
  .addEventListener("submit", async function (event) {
    event.preventDefault();

    const passwordData = {
      old_password: document.getElementById("old_password").value,
      new_password: document.getElementById("new_password").value,
      confirm_password: document.getElementById("confirm_password").value,
    };

    await changePassword(passwordData);
  });

// Función para cambiar el correo
async function changeEmail(emailData) {
  try {
    const response = await axios.put(
      `${CONFIG.API_BASE_URL}/usuarios/change-email/`,
      emailData,
      {
        headers: {
          Authorization: `Bearer ${localStorage.getItem("token")}`,
        },
      }
    );
    console.log("Correo actualizado:", response.data);
  } catch (error) {
    console.error("Error al cambiar el correo:", error.response.data);
  }
}

// Captura el formulario de cambio de correo
document
  .getElementById("changeEmailForm")
  .addEventListener("submit", async function (event) {
    event.preventDefault();

    const emailData = {
      email: document.getElementById("new_email").value,
    };

    await changeEmail(emailData);
  });
