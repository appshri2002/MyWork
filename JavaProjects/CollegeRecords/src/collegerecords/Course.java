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
public class Course {
    
    String courseid = null;
    String coursename= null;
    String coursedpt = null;
    
    
    
    public Course(){}

public String getname()
  {return coursename;
      
  }
  
  public String getid(){
      return courseid;
  }
  
  public String getdpt(){
      return coursedpt;
  }
  
 
    
 
  
  
  
  public void setname(String cname){
      coursename = cname;
  }
    
  public void setid (String cid){
      courseid=cid;
      
  }
   
  public void setdpt(String cdpt){
      coursedpt=cdpt;
  }
  
}
    
