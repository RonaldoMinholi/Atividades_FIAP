// EVENTOS1.JS
window.onload = function () {
    var oRetangulo = document.getElementById("retangulo");

    //Pinta o fundo de verde quando o ponteiro do mouse passar por cima
    oRetangulo.onmouseover = function () {
        oRetangulo.style.backgroundColor = "#008000";
    }

    //Restaurar a cor original quando o ponteiro sair
    oRetangulo.onmouseout = function () {
        oRetangulo.style.backgroundColor = "";
    }
}