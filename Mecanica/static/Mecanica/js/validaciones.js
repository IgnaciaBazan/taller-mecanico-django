(function () {
    const formulario = document.getElementById("form-vehiculo");
    if (!formulario) return;

    function mostrarError(idCampo, mensaje) {
        const span = document.getElementById("error-" + idCampo);
        span.textContent = mensaje;
    }

    function limpiarError(idCampo) {
        mostrarError(idCampo, "");
    }

    formulario.addEventListener("submit", function (evento) {
        let esValido = true;

        // Validación 1: campo obligatorio
        const patente = document.getElementById("patente").value.trim();
        if (patente === "") {
            mostrarError("patente", "La patente es obligatoria.");
            esValido = false;
        } else {
            limpiarError("patente");
        }

        // Validación 2: formato (patente chilena: 4 letras + 2 números, o 2 letras + 4 números)
        const formatoPatente = /^([A-Z]{4}\d{2}|[A-Z]{2}\d{4})$/;
        if (patente !== "" && !formatoPatente.test(patente.toUpperCase())) {
            mostrarError("patente", "Formato de patente inválido (ej: ABCD12).");
            esValido = false;
        }

        // Validación 3: rango numérico
        const anio = parseInt(document.getElementById("anio").value, 10);
        const anioActual = new Date().getFullYear();
        if (isNaN(anio) || anio < 1980 || anio > anioActual + 1) {
            mostrarError("anio", `El año debe estar entre 1980 y ${anioActual + 1}.`);
            esValido = false;
        } else {
            limpiarError("anio");
        }

        // Validación 4: selección obligatoria en un desplegable
        const marca = document.getElementById("marca").value;
        if (marca === "") {
            mostrarError("marca", "Debes seleccionar una marca.");
            esValido = false;
        } else {
            limpiarError("marca");
        }

        if (!esValido) {
            evento.preventDefault();   // esto es lo que bloquea el envío
        }
    });
})();

(function () {
    const formulario = document.getElementById("form-login");
    if (!formulario) return;

    formulario.addEventListener("submit", function (evento) {
        let esValido = true;

        const username = document.getElementById("id_username").value.trim();
        if (username === "") {
            document.getElementById("error-username").textContent = "El usuario es obligatorio.";
            esValido = false;
        } else {
            document.getElementById("error-username").textContent = "";
        }

        const password = document.getElementById("id_password").value;
        if (password === "") {
            document.getElementById("error-password").textContent = "La contraseña es obligatoria.";
            esValido = false;
        } else {
            document.getElementById("error-password").textContent = "";
        }

        if (!esValido) {
            evento.preventDefault();
        }
    });
})();