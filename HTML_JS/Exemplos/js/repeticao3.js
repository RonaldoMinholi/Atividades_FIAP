// REPETICAO3.JS
window.onload = function () {
    var objDivSaida = document.getElementById("saida");

    for (var i = 1; i <= 10; i++) {
        objDivSaida.innerHTML += i + "<br>";
    }
}