package br.com.healthTrack;


/** Classe que abstrai um Amigo
 * @author ronaldominholidias
 * @version 1.0
 */

public class Amigos {
	
	String amigo;
	
//	Atributos de classe
	protected int id;
	protected String nome;
	protected String sobrenome;
	protected String email;
	protected String cidade;
	protected String pais;


	//Construtor padrao
	public Amigos() {
	
	}
	
	
//	Construtor de classe - Classe Amigos
	public Amigos(String nome, String sobrenome, String email, String cidade, String pais) {
		this.nome = nome;
		this.sobrenome = sobrenome;
		this.email = email;
		this.cidade = cidade;
		this.pais = pais;
		
		
		
	}
	
//	Métodos
	/** Adicionar amigo
	 * 
	 * @param descricao
	 */
	
	public void adicionarAmigo(String nome, String sobrenome, String email, String cidade, String pais) {
		this.nome = nome;
		this.sobrenome = sobrenome;
		this.email = email;
		this.cidade = cidade;
		this.pais = pais;
	}

	public void editarAmigo(String nome, String sobrenome, String email, String cidade, String pais) {
		this.nome = nome;
		this.sobrenome = sobrenome;
		this.email = email;
		this.cidade = cidade;
		this.pais = pais;
	}

	
	

}
