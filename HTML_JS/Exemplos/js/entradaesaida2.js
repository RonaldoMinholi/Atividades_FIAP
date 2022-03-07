// ENTRADAESAIDA2.JS
window.onload = function () {
    var objCxNome = document.getElementById("nome");
    var objBotao = document.getElementById("botao");
    var objDiv = document.getElementById("resultado");
    objBotao.onclick = function () {
        objDiv.innerHTML = "Seu nome é " + objCxNome.value;
    }
}