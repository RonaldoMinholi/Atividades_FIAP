package br.com.healthTrack;

import java.util.Date;


/** Classe que abstrai um Troféu
 * @author ronaldominholidias
 * @version 1.0
 */

public class Trofeus {
	
	protected int id;
	protected String descricao;
	protected Date dataConquista;
	
	//Construtor padrao
		public Trofeus() {
		
		}
	
//		Construtor de classe - Classe Trofeus
		public Trofeus(String descricao, Date dataConquista) {
			this.descricao = descricao;
			this.dataConquista = dataConquista;
			
			
		}
		
//		Métodos
		/** Consultar consulta de troféus
		 * 
		 * @param consultar troféus
		 */
		
		public void consultarTrofeu(String descricao, Date dataConquista) {
			this.descricao = descricao;
			this.dataConquista = dataConquista;
		}
	
	
	
	
	

}
