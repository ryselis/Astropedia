package file_spam;

import java.io.BufferedWriter;
import java.io.FileWriter;
import java.io.IOException;
import java.util.Random;

/**
 *
 * @author Paulius Kaunietis
 */
public class File_spam {

    public static void main(String[] args) throws IOException {
        System.out.println("Paulius Kaunietis © 2014");
        String a = "./ups_";
        String b = ".py";
        Random r = new Random(System.nanoTime());        
        while(true){
            String fn = a + System.nanoTime() + r.nextInt(1000000) + r.nextInt(1000000)  + b;
            System.out.println(fn);
            BufferedWriter bw = new BufferedWriter(new FileWriter(fn));
            for (int i = 0; i < r.nextInt(200); i++) {
                bw.write(fn);
            }            
            bw.close();
        }
        // TODO code application logic here
    }

}
