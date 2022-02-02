/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package collegerecords;
import javax.swing.*;

/**
 *
 * @author Apoorva Shrivastava
 */
public class TAUI {
    JFrame f ;
    
    
        TAUI(){
        f = new JFrame();
       // String[] columns = {"Name","DOB","ID"} ;
        DataLoader1 dl= new DataLoader1();
        String data [][]= dl.getTA();
        String[] columns =dl.getTACol();
        //String data[][] = {{"AMt","01/12/2001","19128"},{"SAM","08/05/2008","232"},{"John","03/18/2004","2323"}};
        JTable table = new JTable(data,columns);
        JScrollPane sp = new JScrollPane(table);
        f.add(sp);
        f.setSize(600,300);
        f.setVisible(true);
            
    }
    
    public static void main(String[] args)
    {
        new TAUI();
    }
    
    
}
