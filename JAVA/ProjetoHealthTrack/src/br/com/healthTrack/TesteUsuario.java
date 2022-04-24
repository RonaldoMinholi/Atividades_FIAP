package br.com.healthTrack;

import java.util.Date;

public class TesteUsuario {
	
	public static void main(String[] args) {
		
//		Criando instancia de classe
		Usuario assinante = new Usuario();
		assinante.nome = "Andre";
		assinante.sobrenome = "Silva";
		assinante.idade = 30;
		assinante.cidade = "São Paulo";
		assinante.pais = "Brasil";
		assinante.email = "usuario1@teste.com.br";
		assinante.peso = 70.5;
		
		
		Usuario convidado = new Usuario();
		convidado.nome = "Beatriz";
		convidado.sobrenome = "Souza";
		convidado.idade = 25;
		convidado.cidade = "Rio de Janeiro";
		convidado.pais = "Brasil";
		convidado.email = "usuario2@teste.com.br";
		convidado.peso = 65;
		
//		Imprimindo cadastro
		System.out.println(assinante.nome);
		System.out.println(assinante.sobrenome);
		System.out.println(assinante.idade);
		System.out.println(assinante.cidade);
		System.out.println(assinante.pais);
		System.out.println(assinante.email);
		System.out.println(assinante.peso);
		System.out.println();
		
		System.out.println(convidado.nome);
		System.out.println(convidado.sobrenome);
		System.out.println(convidado.idade);
		System.out.println(convidado.cidade);
		System.out.println(convidado.pais);
		System.out.println(convidado.email);
		System.out.println(convidado.peso);
		System.out.println();
		
		
//		Exibindo consumo de alimento
		Alimentos exibeConsumo = new Alimentos();
		exibeConsumo.descricao = "Refeição";
		exibeConsumo.calorias = 2500;
		
		System.out.println(exibeConsumo.descricao);
		System.out.println(exibeConsumo.calorias);
		System.out.println();
		
		
//		Exibindo prática de exercício
		Exercicios exibeExercicio = new Exercicios();
		exibeExercicio.descricao = "Running";
		exibeExercicio.calorias = 500;
		
		System.out.println(exibeExercicio.descricao);
		System.out.println(exibeExercicio.calorias);
		System.out.println();
		
		
		
//		Exibindo conquista de troféu
		Trofeus consultaTrofeu = new Trofeus();
		consultaTrofeu.descricao = "Conquista 10k";
		
		System.out.println(consultaTrofeu.dataConquista);
		System.out.println(consultaTrofeu.descricao);
		System.out.println();
		
		
		
//		Adicionando amigos
		Amigos adicionaAmigo = new Amigos();
		adicionaAmigo.email = "amigo1@java.com.br";
		adicionaAmigo.nome = "Antonio";
		adicionaAmigo.sobrenome = "Silva";
		adicionaAmigo.cidade = "São Paulo";
		adicionaAmigo.pais = "Brasil";
		
		
		System.out.println(adicionaAmigo.email);
		System.out.println(adicionaAmigo.nome);
		System.out.println(adicionaAmigo.sobrenome);
		System.out.println(adicionaAmigo.cidade);
		System.out.println(adicionaAmigo.pais);
		System.out.println();
		
		
		
		
		
	}

}
