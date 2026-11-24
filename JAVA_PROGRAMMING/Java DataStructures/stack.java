
import java.util.Stack;

public class stack {
    
    public static void main(String args[])
    {
       
        Stack<Integer> stack = new Stack<>();
        

        //insertion 
        stack.push(10);
        stack.push(20);
        stack.push(30);
        stack.push(40);
        stack.push(50);

       
        // display the elements 

        System.out.println("stack elements : "+ stack);


        // top element

        System.out.println("Peek element : "+stack.peek());

        // iterative elements 

        while(!stack.isEmpty())
        {
            System.out.println(stack.peek());

            stack.pop();
        }



    }
}
