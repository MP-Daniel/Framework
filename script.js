// Tu SDK Key de ConfigCat (o clave simulada para efectos del Taller)
const configCatKey = "YOUR_CONFIGCAT_SDK_KEY"; 

// Flag al 100% de rollout: todas las operaciones avanzadas e historial activas
let isAllFeaturesEnabled = true;
let historial = [];

// Inicializamos el cliente de ConfigCat
try {
    if (typeof configcat !== "undefined") {
        const logger = configcat.createConsoleLogger(configcat.LogLevel.Info);
        const configCatClient = configcat.createClient(configCatKey, { logger: logger });

        // Consultamos el feature flag con rollout al 100%
        configCatClient.getValueAsync("operaciones_completas", true).then(value => {
            isAllFeaturesEnabled = value !== false;
            actualizarEstadoFeatures();
        }).catch(() => {
            // Si no hay conexión a ConfigCat o la key es placeholder, mantenemos el flag al 100%
            isAllFeaturesEnabled = true;
            actualizarEstadoFeatures();
        });
    } else {
        actualizarEstadoFeatures();
    }
} catch (e) {
    actualizarEstadoFeatures();
}

function actualizarEstadoFeatures() {
    console.log("🚦 Feature Flag: 100% Rollout Activo. Operaciones avanzadas e historial habilitados.");
    const flagStatus = document.getElementById("flagStatus");
    if (flagStatus) {
        flagStatus.innerHTML = "🚦 Feature Flag: <strong>100% Rollout Activo</strong> (Todas las operaciones e historial habilitados)";
    }
    
    // Todos los controles habilitados
    document.getElementById("btnResta").style.display = "inline-block";
    document.getElementById("btnMultiplicar").style.display = "inline-block";
    document.getElementById("btnDividir").style.display = "inline-block";
    document.getElementById("seccionHistorial").style.display = "block";
}

function agregarAlHistorial(texto) {
    historial.push(texto);
    const lista = document.getElementById("listaHistorial");
    if (lista) {
        const li = document.createElement("li");
        li.textContent = texto;
        lista.appendChild(li);
    }
}

function calcularSuma() {
    const a = parseFloat(document.getElementById('numA').value) || 0;
    const b = parseFloat(document.getElementById('numB').value) || 0;
    const res = a + b;
    document.getElementById('resultado').innerText = `Resultado: ${res}`;
    agregarAlHistorial(`${a} + ${b} = ${res}`);
}

async function calcularResta() {
    if (!isAllFeaturesEnabled) return;
    const a = parseFloat(document.getElementById('numA').value) || 0;
    const b = parseFloat(document.getElementById('numB').value) || 0;
    const res = a - b;
    console.log(`Conectando al endpoint de resta... enviando a=${a} y b=${b}`);
    document.getElementById('resultado').innerText = `Resultado: ${res}`;
    agregarAlHistorial(`${a} - ${b} = ${res}`);
}

async function calcularMultiplicacion() {
    if (!isAllFeaturesEnabled) return;
    const a = parseFloat(document.getElementById('numA').value) || 0;
    const b = parseFloat(document.getElementById('numB').value) || 0;
    const res = a * b;
    console.log(`Conectando al endpoint de multiplicación... enviando a=${a} y b=${b}`);
    document.getElementById('resultado').innerText = `Resultado: ${res}`;
    agregarAlHistorial(`${a} * ${b} = ${res}`);
}

async function calcularDivision() {
    if (!isAllFeaturesEnabled) return;
    const a = parseFloat(document.getElementById('numA').value) || 0;
    const b = parseFloat(document.getElementById('numB').value) || 0;
    
    if (b === 0) {
        document.getElementById('resultado').innerText = "Resultado: Error (No se puede dividir por cero)";
        alert("Error: No se puede dividir por cero");
        return;
    }
    
    const res = a / b;
    console.log(`Conectando al endpoint de división... enviando a=${a} y b=${b}`);
    document.getElementById('resultado').innerText = `Resultado: ${res}`;
    agregarAlHistorial(`${a} / ${b} = ${res}`);
}

function limpiarHistorial() {
    historial = [];
    const lista = document.getElementById("listaHistorial");
    if (lista) {
        lista.innerHTML = "";
    }
}
