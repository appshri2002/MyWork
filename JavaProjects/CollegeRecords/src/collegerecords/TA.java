/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package collegerecords;

/**
 *
 * @author Apoorva Shrivastava
 */
public class TA extends Student {
    String taprofessor =null;
    String tacourse =null;
 
    
    
    
    public String getProf(){
        return taprofessor;
    }
    
    public String getTacourse(){
        return tacourse;  
    }
    

    
    
    public void setProf(String tap){
        taprofessor = tap;
    }
    
    public void setTacourse(String tac){
        tacourse= tac;
    }
}


