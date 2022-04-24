package br.com.healthTrack;

import java.io.Serializable;

/** Classe que abstrai um Usuário
 * @author ronaldominholidias
 * @version 1.0
 */
public class Usuario implements Serializable {
	
/**
	 * 
	 */
	private static final long serialVersionUID = 1L;
	//	Atributos de classe
	private String nome;
	private String sobrenome;
	private byte idade;
	private String cidade;
	private String pais;
	private String email;
	private double peso;
	private float imc;
	private String esporteFavorito;
	private char senha;
	
	
//	Construtor padrao
	public String getUsuario() {
		return nome;
		
	}
	
	public void setUsuario(String nome, String sobrenome, byte idade, String cidade, String pais, String email, double peso) {
		this.nome = nome;
		this.sobrenome = sobrenome;
		this.idade = idade;
		this.cidade = cidade;
		this.pais = pais;
		this.email = email;
		this.peso = peso;
	}
	
	
	
//	Metodos
	/** Cadastrar Usuario
	 * Preencher as informações abaixo para o cadastro do usuário:
	 * @param nome
	 * @param sobrenome
	 * @param idade
	 * @param cidade
	 * @param pais
	 * @param email
	 * @param peso
	 */
	public void cadastrar(String nome, String sobrenome, byte idade, String cidade, String pais, String email, double peso) {
		this.nome = nome;
		this.sobrenome = sobrenome;
		this.idade = idade;
		this.cidade = cidade;
		this.pais = pais;
		this.email = email;
		this.peso = peso;
		
	}
	
	public void editar(String nome, String sobrenome, byte idade, String cidade, String pais, String email, double peso) {
		this.nome = nome;
		this.sobrenome = sobrenome;
		this.idade = idade;
		this.cidade = cidade;
		this.pais = pais;
		this.email = email;
		this.peso = peso;
	}
}