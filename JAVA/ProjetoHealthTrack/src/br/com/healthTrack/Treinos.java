package br.com.healthTrack;

/** Classe que abstrai um Treinos
 * 
 * 
 */

public class Treinos {
	
	String treino;
	
//	Atributos de classe
	protected int id;
	protected String descricao;


	//Construtor padrao
	public Treinos() {
	
	}
	
	
//	Construtor de classe - Classe Treinos
	public Treinos(String descricao) {
		this.descricao = descricao;
	}
	
//	Métodos
	/** Adicionar prática de treinos
	 * 
	 * @param descricao
	 */
	
	public void adicionarTreino(String descricao) {
		this.descricao = descricao;
	}

	public void editarTreinoo(String descricao) {
		this.descricao = descricao;
	}	
	
	
	

}
