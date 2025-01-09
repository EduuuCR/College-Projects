import java.io.IOException;
import java.util.ArrayList;
import java.util.Scanner;
import java.util.Stack;

public class Hanoi
{  
    public static void clearScreen() {  
    System.out.print("\n\n\n\n\n");  
    }  
    static void printTowers(Stack<Integer> fTower,Stack<Integer> sTower,Stack<Integer> tTower)
    {  
        System.out.print("\n\t  1\t\t       2\t\t     3\n");
        
        // da pra colocar tudo isso aqui em uma lista pra nao ficar essa aberrazao mas preguiza
        for(int i=1; i<6; i++)
        {
            int temp = fTower.pop();
            System.out.print(" ".repeat(10-temp));
            System.out.print("#".repeat(temp));
            System.out.print("|");
            System.out.print("#".repeat(temp));
            System.out.print(" ".repeat(10-temp));
            temp = sTower.pop();
            System.out.print(" ".repeat(10-temp));
            System.out.print("#".repeat(temp));
            System.out.print("|");
            System.out.print("#".repeat(temp));
            System.out.print(" ".repeat(10-temp));
            temp = tTower.pop();
            System.out.print(" ".repeat(10-temp));
            System.out.print("#".repeat(temp));
            System.out.print("|");
            System.out.print("#".repeat(temp));
            System.out.print(" ".repeat(10-temp));
            System.out.print("\n");
            
        }
        System.out.print("\n");
    }
    public static void main(String args[]) throws IOException
    {
        Stack<Integer> t1 = new Stack<>();
        Stack<Integer> t2 = new Stack<>();
        Stack<Integer> t3 = new Stack<>();
        

        ArrayList<Stack> towers = new ArrayList<>();
        towers.add(t1);
        towers.add(t2);
        towers.add(t3);               

        for(int i=5; i>0; i--)
        {
            t1.push(i);
            t2.push(0);
            t3.push(0);
        }
        Stack<Integer> win = (Stack<Integer>) t1.clone();
        String input = "null";
        Scanner sc = new Scanner(System.in);
        printTowers((Stack<Integer>) t1.clone(),(Stack<Integer>) t2.clone(),(Stack<Integer>) t3.clone());       
        
        do
        {
            clearScreen();
            
            System.out.print("Current tower target tower EX: 1 3 |  nothing to quit\n");
            input = sc.nextLine();
            if(!input.isEmpty())
            {
                
                if(input != "null")
                {
                String[] inputSplit = input.split("\\s+");
                int current = Integer.parseInt(inputSplit[0]) -1;
                int target = Integer.parseInt(inputSplit[1]) -1 ;
                removeZero(t1,t2,t3);
                

                if((int)towers.get(current).peek() == 0)
                {
                    System.out.println("Empty tower");
                    addZero(t1,t2,t3);
                }
                else if((int)towers.get(target).peek() == 0)
                {
                    towers.get(target).pop();
                    int temp = (int) towers.get(current).pop();
                    towers.get(target).push(temp);
                    addZero(t1,t2,t3);
                }
                else if((int)towers.get(current).peek() < (int)towers.get(target).peek())
                {
                    int temp = (int) towers.get(current).pop();
                    towers.get(target).push(temp);
                    addZero(t1,t2,t3);
                }
                else
                {
                    System.out.println("Invalid move");
                    addZero(t1,t2,t3);
                }
            }
            else{
                System.out.print("Wrong input, try again\n ");
                }
            }
            printTowers((Stack<Integer>) t1.clone(),(Stack<Integer>) t2.clone(),(Stack<Integer>) t3.clone());
            if(t2.equals(win) || t3.equals(win))
            {
                System.out.println("GG, you win");
                System.exit(0);
            }
            
        }while(!input.isEmpty());
        System.out.println("Bye, GL next time");
    }

    private static void removeZero(Stack<Integer> t1, Stack<Integer> t2, Stack<Integer> t3) {
        while(!t1.empty() && t1.peek() == 0 && t1.size() != 1 )
        {
            t1.pop();
        }
        while(!t2.empty() && t2.peek() == 0 && t2.size() != 1  )
        {
            t2.pop();
        }
        while(!t3.empty() && t3.peek() == 0 && t3.size() != 1 )
        {
            t3.pop();
        }
    }

    private static void addZero(Stack<Integer> t1, Stack<Integer> t2, Stack<Integer> t3) {
        while(t1.size() != 5)
        {
            t1.push(0);
        }
        while(t2.size() != 5)
        {
            t2.push(0);
        }
        while(t3.size() != 5)
        {
            t3.push(0);
        }
    }
}
