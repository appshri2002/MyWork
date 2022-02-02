/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package collegerecords;
import java.awt.*;
import java.awt.event.*;
import javax.swing.JOptionPane;
import javax.swing.*;
import javax.swing.table.TableColumn;
import collegerecords.DataLoader;

/**
 *
 * @author Apoorva Shrivastava
 */
public class CRUI2 extends Frame implements ActionListener{
    
     Button student,professor,course,ta,ex;
     JPanel panel=new JPanel();
     JTable jt=new JTable();
     JScrollPane sp=new JScrollPane();

    CRUI2(){
       
    student=new Button("Student");  
    student.setBounds(100,50,90,40); 
    student.addActionListener(this);

    professor=new Button("Professor");  
    professor.setBounds(200,50,90,40);
    professor.addActionListener(this);
    
    
    course=new Button("Course");  
    course.setBounds(300,50,90,40); 
    course.addActionListener(this);
    
    ta=new Button("TA");  
    ta.setBounds(400,50,90,40); 
    ta.addActionListener(this);
    
    ex=new Button("Exit");  
    ex.setBounds(500,50,90,40); 
    ex.addActionListener(this);
    
    this.add(student);
    this.add(professor);
    this.add(course);
    this.add(ta);
    this.add(ex);
    
    panel.setBounds(10,150,800,400);    
    //panel.setBackground(Color.gray); 
    panel.add(sp);
    panel.setVisible(false);
    //this.add(jt);
    this.add(panel);
    
    setSize(800,1000);  
    setLayout(null); 
    this.setTitle("College Records");
    
    setVisible(true);  

    }
    
    
    public void actionPerformed(ActionEvent e){  
        
     if(e.getSource()==student)
     {
         System.out.println("Student Clicked");
            panel.remove(sp);
            DataLoader dl = new DataLoader();
            String data[][] = dl.getStudents();
            String column[] = dl.getStudentsCol();
            jt=new JTable(data,column);    
            jt.setBounds(0,0,600,400); 
            jt.setShowGrid(true);
            
              
            TableColumn c1 = jt.getColumnModel().getColumn(0);
            c1.setMinWidth(100);
            TableColumn c2 = jt.getColumnModel().getColumn(1);
            c2.setMinWidth(100);
            TableColumn c4 = jt.getColumnModel().getColumn(3);
            c4.setMinWidth(150);
            sp=new JScrollPane(jt);
            sp.setVisible(true);
            
            panel.add(sp,BorderLayout.WEST);
            panel.setVisible(true);
            this.revalidate();
            repaint();
     }
      if(e.getSource()==professor)
     {
         System.out.println("Professor  Clicked");
         System.out.println("Student Clicked");
            panel.remove(sp);
            
            DataLoader dl = new DataLoader();
            String data[][] = dl.getProfData();
            String column[] = dl.getProfCols();
            jt=new JTable(data,column);    
            jt.setBounds(0,0,600,400);
            jt.setShowGrid(true);
            
              
            TableColumn c1 = jt.getColumnModel().getColumn(0);
            c1.setMinWidth(100);
            
            TableColumn c2 = jt.getColumnModel().getColumn(1);
            c2.setMinWidth(100);
            TableColumn c4 = jt.getColumnModel().getColumn(3);
            c4.setMinWidth(150);
            sp=new JScrollPane(jt);
            sp.setVisible(true);
            
            panel.add(sp,BorderLayout.WEST);
            panel.setVisible(true);
            this.revalidate();
            repaint();
     }
       if(e.getSource()==course)
     {
         System.out.println("Course  Clicked");
         
           //tf.setText("Welcome to Javatpoint."); 
            panel.remove(sp);
           // sp.remove(jt);
            //this.remove(panel);
            //JPanel panel=new JPanel();
            
            DataLoader dl = new DataLoader();
            String data[][] = dl.getCourses();
            String column[] = dl.getcoursesCol();
            jt=new JTable(data,column);    
            jt.setBounds(0,0,600,400);
            jt.setShowGrid(true);
            
              
            TableColumn c1 = jt.getColumnModel().getColumn(0);
            c1.setMinWidth(200);
             
            TableColumn c2 = jt.getColumnModel().getColumn(1);
            c2.setMinWidth(100);
            TableColumn c4 = jt.getColumnModel().getColumn(2);
            c4.setMinWidth(100);
            sp=new JScrollPane(jt);
            sp.setVisible(true);
            
            panel.add(sp,BorderLayout.WEST);
            panel.setVisible(true);
            
            this.revalidate();
            repaint();
     }
       if(e.getSource()==ta)
     {
         System.out.println("TA  Clicked");
         
            panel.remove(sp);
             
            DataLoader2 dl = new DataLoader2();
            dl.printTA();
            String data[][] = dl.getTA1();
            String column[] = dl.getTACol1();
            jt=new JTable(data,column);    
            jt.setBounds(0,0,800,800);
            jt.setShowGrid(true);
            System.out.println(column);
            TableColumn c1 = jt.getColumnModel().getColumn(0);
            c1.setMinWidth(100);
             
            TableColumn c2 = jt.getColumnModel().getColumn(1);
            c2.setMinWidth(100);
            TableColumn c3 = jt.getColumnModel().getColumn(2);
            c3.setMinWidth(100);
           
            
           TableColumn c4 = jt.getColumnModel().getColumn(3);
           c4.setMinWidth(250);
           
            sp=new JScrollPane(jt);
            sp.setVisible(true);
            
            panel.add(sp,BorderLayout.WEST);
            panel.setVisible(true);
            
            this.revalidate();
            repaint();
     }
        if(e.getSource()==ex)
     {
         dispose();
          System.exit(0);
     }
       
    }
    
    
    public static void main(String[] args){
        CRUI2 cr = new CRUI2();
        System.out.println("Hello World");
    
}
    
}
