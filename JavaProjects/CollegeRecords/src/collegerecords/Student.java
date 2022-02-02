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
public class Student implements Person{
   public String name = null;
  public String dob = null;
  public String id = null;
  public String major = null;
  public String[] courses = new String[5];
  
  public Student(){}
  
  
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
  
  public String getMajor(){
      return major;
      
  }
    
  
  public String[] getCourse(){
      return courses;
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
    
 public void setMajor(String m){
     major=m;
 }
 
 public void setCourses(String[] c){
     courses=c;
 }
    
}


