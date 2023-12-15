const progress = document.getElementById('progress');
let percentaje = document.getElementById('percentaje');
let contador = 0;
let cantidad = 630;
let resta = cantidad / 100 
let refresh = 80;

let tiempo = setInterval(() => {
    contador += 1;
    let value = Math.ceil(cantidad -= resta);
    percentaje.textContent = `${contador}%`;
    progress.style.strokeDashoffset = value;

    if (contador === 100) {
        clearInterval(tiempo);
         // Redirigir a otra página después de que el intervalo termine
         setTimeout(() => {
            window.location.href = "../login/";
        }, 1000); // Tiempo en milisegundos antes de redirigir (en este caso, 1000 ms o 1 segundo)
    }
}, refresh);