// 100/100

import java.io.*;
import java.util.*;
import java.util.Arrays;

public class Solution {

    public static void main(String[] args) {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */
        Scanner scanner = new Scanner(System.in);/// input
        int N = scanner.nextInt(); 
        
        int [][] square = new int [N][N];
        int temp = 0;
        for (int i = 0; i < N; ++i) {
            for(int j = 0; j < N; j++){
                // Read from the STDIN an Int and put in square[i][j]
                temp = scanner.nextInt();
                square[i][j] = temp;
            }
        }
        
        int counter = 0;
        int [] print = new int [(N+N)+ 2 + 1];
        
        int mainD = 0;
        int antiD = 0;
        // initialzing mainD and antiD
        for(int i=0; i<N; i++){
            for(int j=0; j<N; j++){
                if (i == j) { 
                    mainD += square[i][j];
                }
                if ((N-1-i) == j) { 
                    antiD += square[i][j];
                }
            } 
        }
        
        int row = 0;
        // checking rows
        for(int i=0; i<N; i++){
            for(int j=0; j<N; j++){
                row += square[i][j];
            }
            if (row != mainD) { 
                print[counter]= i+1;
                // System.out.print(print[counter]);
                counter ++;
            }
            row = 0;    
        }
        
        int col = 0;
        // checking colomns
        for(int i=0; i<N; i++){
            for(int j=0; j<N; j++){
                col += square[j][i];
            }
            if (col != mainD){
                print[counter]= -(i+1);
                // System.out.print(print[counter]);
                counter ++;
            }
            col = 0;
        }
        
        if (mainD != antiD){
            print[counter]= 0;
            counter++;
        }
        
        Arrays.sort(print, 0, counter);
        
        System.out.println(counter);
        if(counter == 0) return;
        else {
            // System.out.println("\n");
            for(int i=0; i<counter; i++){
               System.out.println(print[i]);
            }
        }
    }
}