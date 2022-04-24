package br.com.healthTrack;

/** Classe que abstrai um Alimento
 * @author ronaldominholidias
 * @version 1.0
 */
public class Alimentos implementes Serializable {
	
	String alimento;
	
//	Atributos de classe
	private int id;
	private String descricao;
	private int calorias;


	//Construtor padrao
	public Alimentos() {
	
	}
	
	
//	Construtor de classe - Classe Alimentos
	public Alimentos(String descricao, int calorias) {
		this.descricao = descricao;
		this.calorias = calorias;
		
		
	}
	
	
	
//	Métodos
	/** Adicionar consumo de alimento e calorias
	 * 
	 * @param descricao
	 * @param calorias
	 */
	
	public void adicionarConsumo(String descricao, int calorias) {
		this.descricao = descricao;
		this.calorias = calorias;
	}

	public void editarConsumo(String descricao, int calorias) {
		this.descricao = descricao;
		this.calorias = calorias;
	}
	
	
	

}