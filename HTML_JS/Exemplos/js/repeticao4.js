// REPETICAO4.JS
window.onload = function () {
    //Declaração de array com 5 elementos.
    var aLinguagens = ["JavaScript", "Java", "PHP", "Python"];
	
    var objDivSaida = document.getElementById("saida");
    //Estrutura for..of
    for (sLinguagem of aLinguagens) {
        objDivSaida.innerHTML += sLinguagem + "<br>";
    }
}