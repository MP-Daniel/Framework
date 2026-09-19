// Tu SDK Key de ConfigCat (reemplázala si tienes una cuenta real, si no, es para efectos visuales del Taller)
const configCatKey = "YOUR_CONFIGCAT_SDK_KEY"; 
let isRestaEnabled = false;

// Inicializamos el cliente de ConfigCat
const logger = configcat.createConsoleLogger(configcat.LogLevel.Info);
const configCatClient = configcat.createClient(configCatKey, { logger: logger });

// Consultamos si el feature flag "resta_habilitada" está encendido
configCatClient.getValueAsync("resta_habilitada", false).then(value => {
    isRestaEnabled = value;
    
    // Si está encendido, mostramos el botón de Restar en la Interfaz (UI actualizada)
    if (isRestaEnabled) {
        document.getElementById("btnResta").style.display = "inline-block";
        console.log("Feature flag 'resta' activado (rollout 10%). Botón expuesto.");
    } else {
        console.log("Feature flag 'resta' apagado. Botón oculto.");
    }
});

function calcularSuma() {
    const a = parseInt(document.getElementById('numA').value) || 0;
    const b = parseInt(document.getElementById('numB').value) || 0;
    document.getElementById('resultado').innerText = `Resultado: ${a + b}`;
}

async function calcularResta() {
    if (!isRestaEnabled) return; // Doble validación por seguridad
    
    const a = parseInt(document.getElementById('numA').value) || 0;
    const b = parseInt(document.getElementById('numB').value) || 0;
    
    // Simulando la conexión al endpoint (backend) que creamos en el issue anterior
    console.log(`Conectando al endpoint de resta... enviando a=${a} y b=${b}`);
    
    document.getElementById('resultado').innerText = `Resultado: ${a - b}`;
}
