package br.com.healthTrack;


/** Classe que abstrai um Exercicios
 * @author ronaldominholidias
 * @version 1.0
 */

public class Exercicios {
	
	String exercicio;
	
//	Atributos de classe
	protected int id;
	protected String descricao;
	protected int calorias;


	//Construtor padrao
	public Exercicios() {
	
	}
	
	
//	Construtor de classe - Classe Exercicios
	public Exercicios(String descricao, int calorias) {
		this.descricao = descricao;
		this.calorias = calorias;
		
		
	}
	
//	Métodos
	/** Adicionar prática de exercícios
	 * 
	 * @param descricao
	 */
	
	public void adicionarPraticaExercicio(String descricao, int calorias) {
		this.descricao = descricao;
		this.calorias = calorias;
	}

	public void editarPraticaExercicio(String descricao, int calorias) {
		this.descricao = descricao;
		this.calorias = calorias;
	}
	
	
	
	
	
	

}
