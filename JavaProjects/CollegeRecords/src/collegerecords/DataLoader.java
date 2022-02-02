 /*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package collegerecords;
/**
 *
 * @author Apoorva
 */
public class DataLoader {
    
    Student[] students = new Student[5];
    Professor[] professors = new Professor[3];
    Course[] courses =new Course[3];
    TA[] TA = new TA[3];
    
    public DataLoader(){
        loadStdents();
        loadProfessors();
        loadCourses();
        loadTA();
        
    }
    public String [][] getTA(){
        String[][] data =new String[TA.length][4];
        
        int i;
        int j;
        TA ta;
        
        for (i=0; i<TA.length; i++){
            ta = TA[i];
        data[i][0] = ta.getName();
        data[i][1] = ta.getProf();   
        data[i][2] = ta.getTacourse();
        data[i][3] = ta.getID();
       
       
        
        }
        return data;
    }
    
    public String [][] getTA1(){
        String[][] data =new String[TA.length][4];
        
        int i;
        int j;
        TA ta;
        
        for (i=0; i<TA.length; i++){
            ta = TA[i];
        data[i][0] = ta.getName();
        data[i][1] = ta.getProf();   
        data[i][2] = ta.getTacourse();
        data[i][3] = ta.getID();
       
       
        
        }
        return data;
    }
 public void loadTA(){
    
     TA ta = new TA();
        ta.setName("Tyler Oakly");
        ta.setProf("Harry Smith");
        ta.setTacourse("CNIT 315");
        ta.setID("10932");
       
               
        TA[0]=ta;
        
      ta= new TA();
        ta.setName("Will Solace");
        ta.setProf("Melody Carry");
        ta.setTacourse("MA 230 ");
        ta.setID("209123");
        
        
       
        TA[1]=ta;
        
       ta = new TA();
        ta.setName("Samantha Rickers");
        ta.setProf("William Krammer");
        ta.setTacourse("CS 250");
        ta.setID("30291");
      
       
        TA[2]=ta;
        
       
    
}
 
 public void printTA()
    {
        int i;
        TA ta;
        
        for (i = 0; i < TA.length; i++) {
  
            // accessing each element of array
            
            ta = TA[i];
            
            System.out.println("TA Name"+ta.getName());
            System.out.println("Professor Name "+ ta.getProf());
            System.out.println("Course "+ ta.getTacourse());
            System.out.println("TA ID"+ta.getID());
           
            
            
        }
               
    }
 
 
 public String [] getTACol()
    {
        String[] col = {"Name","Professor","Course","ID"}; 
        return col; 
         }
  public String [] getTACol1()
    {
        String[] col = {"Name","Professor","Course","ID"}; 
        return col; 
         }
 
    public String [][] getCourses(){
        String[][] data =new String[courses.length][3];
        
        int i;
        int j;
        Course co;
        
        for (i=0; i<courses.length; i++){
            co = courses[i];
        data[i][0] = co.getname();   
        data[i][1] = co.getid();
        data[i][2] = co.getdpt();
        }
        return data;
    }
    
    public void loadCourses(){
    
     Course co = new Course();
        co.setname("Java Programing");
        co.setid("255");
        co.setdpt("CNIT");
       
        courses[0]=co;
        
      co = new Course();
        co.setname("Cybersecurity Fundamentals");
        co.setid("270");
        co.setdpt("CNIT");
       
        courses[1]=co;
        
       co = new Course();
        co.setname("Hardware Architecture");
        co.setid("210");
        co.setdpt("CS");
       
        courses[2]=co;
        
       
    
}
    
   public void printCourses()
    {
        int i;
        Course co;
        
        for (i = 0; i < courses.length; i++) {
  
            // accessing each element of array
            
            co = courses[i];
            System.out.println("Course Name "+ co.getname());
            System.out.println("Course ID "+ co.getid());
            System.out.println("Course Department "+ co.getdpt());
            
        }
               
    }
     
   public String [] getcoursesCol()
    {
        String[] col = {"NAME","ID","Department"}; 
        return col; 
         }
    
    
    public String [][] getStudents()
    {
        String[][] data = new String[students.length][4];
    
        
        
        int i;
        int j;
        Student st;
        
        for (i = 0; i < students.length; i++) {
            
            st = students[i];
        
        data[i][0] = st.getName();
        data[i][1] = st.getDOB();
        data[i][2] = st.getID();
        data[i][3] = st.getMajor();
        
            
        }
        
        return data;
    }
    
    public void loadStdents()
    {
        Student st = new Student();
        st.setName("James Stuard");
        st.setDOB("02/14/2001");
        st.setID("23232");
        st.setMajor("Cybersecurity");
        students[0]=st;
        
        st = new Student();
        st.setName("Pieter England");
        st.setDOB("12/19/2003");
        st.setID("14232");
        st.setMajor("Networking");
        students[1]=st;
        
        st = new Student();
        st.setName("Kim Tylor");
        st.setDOB("08/01/2001");
        st.setID("23772");
        st.setMajor("Computer Science");
        students[2]=st;
        
        st = new Student();
        st.setName("Tim Dexter");
        st.setDOB("03/21/2002");
        st.setID("34232");
        st.setMajor("Cybersecurity");
        students[3]=st;
        
        st = new Student();
        st.setName("Marry Colton");
        st.setDOB("06/11/2004");
        st.setID("34332");
        st.setMajor("Networking");
        students[4]=st;       
    }
    
    public void printStdents()
    {
        int i;
        Student st;
        
        for (i = 0; i < students.length; i++) {
  
            // accessing each element of array
            
            st = students[i];
            System.out.println("Student Name "+ st.getName());
            System.out.println("Student DOB "+ st.getDOB());
            System.out.println("Student ID "+ st.getID());
            
        }
               
    }
    
    
    public String [] getStudentsCol()
    {
        String[] col = {"NAME","DOB","ID","Major"}; 
        return col; 
         }
    
    
    public void loadProfessors()
    {
        Professor pro = new Professor();
        pro.setName("Harry Smith");
        pro.setDOB("12/12/1974");
        pro.setID("102918");
        pro.setDepartment("CNIT");
        professors[0]=pro;
        
        pro = new Professor();
        pro.setName("Melody Carry");
        pro.setDOB("10/23/1980");
        pro.setID("119082");
        pro.setDepartment("MA");
        professors[1]=pro;
        
        pro = new Professor();
        pro.setName("William Krammer");
        pro.setDOB("05/01/1970");
        pro.setID("908201");
        pro.setDepartment("CS");
        professors[2]=pro;
        
       
    }
    
    public void printProfessors()
    {
        int i;
        Professor pro;
        
        for (i = 0; i < professors.length; i++) 
        {
  
            // accessing each element of array
            
            pro = professors[i];
            System.out.println("Professor Name "+ pro.getName());
            System.out.println("Professor DOB "+ pro.getDOB());
            System.out.println("Professor ID"+pro.getID());
            System.out.println("Professor Department"+ pro.getDepartment());
            
    }
    }
    
    public String[] getProfCols()
    {
     
        
        String[] col = {"NAME","DOB","ID","Department"}; 
        return col; 
      
    }
    
    public String[][] getProfData(){
    //String data[][] = new String[][]
    String[][] data = new String[professors.length][4];
    
        
        
        int i;
        Professor pro;
        
        for (i = 0; i < professors.length; i++) 
        {
            
            pro = professors[i];
        
        data[i][0] = pro.getName();
        data[i][1] = pro.getDOB();
        data[i][2] = pro.getID();
        data[i][3] = pro.getDepartment();     
        
        }
    return data;
    }
    
    
    
    
    
    public static void main(String[] args) {  
        
        DataLoader dl = new DataLoader();
        dl.printProfessors();
        dl.printStdents();
        dl.printCourses();
        dl.printTA();
        String [][] prodata = dl.getTA();
        int i;
        int j;
        for (i = 0; i < prodata.length; i++)
        {
            for (j = 0; j < 2; j++)
            {
                System.out.println(prodata[i][j]);
            }
        }
        
        
        
}  
    
    
    
}
