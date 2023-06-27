
window.addEventListener('load', () => {
    let lon
    let lat
    let temperaturaValor = document.getElementById('temperatura-valor')
    let temperaturaDescripcion = document.getElementById('temperatura-descripcion')
    let ubicacion = document.getElementById('ubicacion')
    let vientoVelocidad = document.getElementById('viento-velocidad')
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(posicion => {
            console.log(posicion)

            lon = posicion.coords.longitude
            lat = posicion.coords.latitude
            const url = `https://api.openweathermap.org/data/2.5/weather?&lang=es&lat=${lat}&lon=${lon}&appid=1d19a88a0ed188f82a8212ec59d71032`
            //const url = `https://api.openweathermap.org/data/2.5/weather?q=Santiago&lang=es&units=metric&appid=1d19a88a0ed188f82a8212ec59d71032`

            console.log(url)

            fetch(url)
                .then(response => { return response.json() })
                .then(data => {

                    let temp = Math.round(data.main.temp - 273)
                    temperaturaValor.textContent = temp + ' C'
                    console.log(data)
                    let desc = data.weather[0].description
                    temperaturaDescripcion.textContent = desc.toUpperCase()
                    ubicacion.textContent = data.name

                    vientoVelocidad.textContent = `${data.wind.speed} m/s`

                    console.log(data.weather[0].main)
                    switch (data.weather[0].main) {
                        case 'Thunderstorm':
                            console.log('TORMENTA');
                            break;
                        case 'Drizzle':
                            console.log('LLOVIZNA');
                            break;
                        case 'Rain':
                            console.log('LLUVIA');
                            break;
                        case 'Snow':
                            console.log('NIEVE');
                            break;
                        case 'Clear':
                            console.log('LIMPIO');
                            break;
                        case 'Atmosphere':
                            console.log('ATMOSFERA');
                            break;
                        case 'Clouds':
                            console.log('NUBES');
                            break;

                    }
                })
                .catch(error => {
                    console.log(error)

                })
        })
    }
})







$("#btnenviar").click(function (e) {
    var errores = validar();
    if (errores !== "") {
        Swal.fire("Error de envío", errores, "error");
    } else {
        Swal.fire("Datos Validos", "Bienvenido", "success")
            .then(function () {
                window.location.href = "{% url 'index' %}";

            });
    }
    e.preventDefault();
});


function validar() {
    var html = "";
    var nombre = $("#txtNombre").val().trim();
    var apellido = $("#txtApellido").val().trim();
    var NombreUsuario = $("#txtNombreUsuario").val().trim();
    var correo = $("#txtCorreo").val().trim();
    var NumTel = $("#NumTelefonico").val().trim();
    var password = $("#txtPassword").val().trim();
    var valpassword = $("#txtValPassword").val().trim();
    var radio = document.querySelector("#ValTerms");

    if (nombre === "") {
        html += "+ Debe ingresar el nombre \n";
    } else if (!nombre.length > 2) {
        html += "+ El nombre debe tener al menos 3 caracteres \n";
    }

    if (apellido === "") {
        html += "+ Debe ingresar el/los apellido/s\n";
    } else if (!apellido.length > 3) {
        html += "+ El/los apellido/s deben tener al menos 4 caracteres \n";
    }

    if (NombreUsuario === "") {
        html += "+ Debe ingresar el nombre de usuario \n";
    } else if (!NombreUsuario.length > 7) {
        html += "+ El nombre de usuario debe tener al menos 8 caracteres \n";
    }

    if (correo === "") {
        html += "+ Debe ingresar el correo electrónico \n";
    }

    if (NumTel === "" || parseInt(NumTel) > 99999999 || parseInt(NumTel) < 10000000) {
        html += "+ El número telefónico debe tener 8 o 9 dígitos \n";
    }

    if (password === "") {
        html += "+ Debe ingresar la contraseña\n";
    } else if (!password.length > 8) {
        html += "+ La contraseña debe tener al menos 8 caracteres \n";
    }

    if (valpassword === "") {
        html += "+ Debe ingresar nuevamente la contraseña \n";
    } else if (valpassword !== password) {
        html += "+ Las contraseñas no coinciden \n";
    }

    if (!radio.checked) {
        html += "+ Debe aceptar los términos y condiciones \n";
    }

    return html;
}

$("#btnenviarL").click(function (e) {
    var erroresL = validarL();
    if (erroresL !== "") {
        Swal.fire("Error de envío", erroresL, "error");
    } else {
        Swal.fire("Datos Validos", "Bienvenido", "success")
            .then(function () {
                window.location.href = "{% url 'index' %}";

            });
    }
    e.preventDefault();
});

function validarL() {
    var htmlL = "";
    var nombreL = $("#txtNombreUsuarioL").val();
    var passwordL = $("#txtcontraseñaL").val();

    if (nombreL === "") {
        htmlL += "+Debe ingresar el nombre de usuario \n";
    }

    if (passwordL === "") {
        htmlL += "+Debe ingresar la contraseña \n";
    }

    return htmlL;
}

$("#btnenviarA").click(function (e) {
    var erroresA = validarA();
    if (erroresA !== "") {
        Swal.fire("Error en su compra", erroresA, "error");
    } else {
        Swal.fire("Gracias Por su compra", "Disfrute", "success")
    }
    e.preventDefault();
});

function validarA() {
    var htmlA = "";
    var Direccion = $("#txtDireccionA").val()
    var NumrutA = $("#numRutA").val()
    var NumtotalA = $("#numTotalA").val()
    var radioS = document.querySelector("#rbtnSI");
    var radioN = document.querySelector("#rbtnNO");

    if (Direccion === "") {
        htmlA += " Debe ingresar su direccion -  \n";
    }
    if (NumtotalA === "") {
        htmlA += "   \n";
    }
    if (NumrutA === "" || parseInt(NumrutA) > 99999999 || parseInt(NumrutA) < 10000000) {
        htmlA += " su rut debe tener 8 o 9 dígitos - \n";
    }
    if (!radioS.checked && !radioN.checked) {
        htmlA += " Debe aceptar si desea el seguro o no \n";
    }
    return htmlA;
}


$("#btnenviarC").click(function (e) {
    var erroresC = validarC();
    if (erroresC !== "") {
        Swal.fire("Error de envío", erroresC, "error");
    } else {
        Swal.fire("Datos Validos", "Formulario enviado", "success")

    }
    e.preventDefault();
});

function validarC() {
    var htmlC = "";
    var nombreC = $("#txtNombresC").val();
    var apellidoC = $("#txtApellidosC").val();
    var correoC = $("#txtCorreoC").val();
    var comunaC = $("#ComunaC").val();
    var radioA = document.querySelector("#rbtDudas");
    var radioB = document.querySelector("#rbtConsulta");
    var comentarioC = $("#comentarioC").val();

    if (nombreC === "") {
        htmlC += "+Debe ingresar el nombre de usuario \n";
    } else if (nombreC < 3) {
        htmlC += "+Debe contener el nombre al menos 3 caracteres \n";
    }

    if (apellidoC === "") {
        htmlC += "+Debe ingresar la apellido  \n";
    } else if (apellidoC < 4) {
        htmlC += "+Debe contener el apellido al menos 4 caracteres \n";
    }

    if (correoC === "") {
        htmlC += "+Debe ingresar el correo";
    }

    if (comunaC == "0") {
        htmlC += "+Debe seleccionar una comuna";
    }

    if (!radioA.checked && !radioB.checked) {
        htmlC += "+Debe seleccionar un boton";
    }

    if (comentarioC.trim().length < 25) {
        htmlC += "+Debe ingresar al menos 25 caracteres en comentario"
    }
    return htmlC;
}

