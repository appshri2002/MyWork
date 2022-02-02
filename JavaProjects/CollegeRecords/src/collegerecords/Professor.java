/*
 * To change this license header, choose License Headers in Project Properties.)
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package collegerecords;

/**
 *
 * @author Apoorva Shrivastava
 */
public class Professor implements Person{
   public String name = null;
  public String dob = null;
  public String id = null;
  public String department =null;
  public Professor(){}
  
  
  // implementing set name method from Person interface
  public String getName()
  {return name;
      
  }
  
  public String getDOB(){
      return dob;
  }
  
  public String getID(){
      return id;
  }
  
  
  public String getDepartment(){
      return department;
  }
    
  
  public void setName(String sname){
      name = sname;
  }
    
  public void setDOB (String sdob){
      dob=sdob;
      
  }
   
  public void setID(String sid){
      id= sid;
  }
    
  public void setDepartment(String dpt){
      department=dpt;
  }
    
}


