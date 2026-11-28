// import the ArrayList

import java.util.*;

import java.util.Collections;

class arraylist
{
    public static void main(String args[])
    {
        // ArrayList declaration | ArrayList creation

        ArrayList<Integer> array = new ArrayList<>();


        // method add()

        System.out.println("--------------------------------");

        array.add(10);

        array.add(20);

        array.add(30);

        array.add(40);

        array.add(50);

        array.add(60);

        // by using the add we can add element at the index positon

        array.add(2,55);


        // display the array elements

        for(int i=0; i< array.size(); i++)
        {
            System.out.println(array.get(i)+" ");
        }
         

        System.out.println("---------------------------------------");

        System.out.println("method set()");

        // method set()

        // -> used to update/replace the element 

        array.set(1,22);

        System.out.println(array.get(1));



        System.out.println("-----------------------------------------");

        System.out.println("method remove()");

        System.out.println("(remove(index) -> Removes the element at index 1 : " + array.remove(1)); // removes the element at index 1
        
        System.out.println("remove(value) -> removes the element by using it's value ; "+array.remove(Integer.valueOf(10)));


        System.out.println("-----------------------------------------");

        System.out.println("method size()");

        System.out.println("The size of the arraylist is : "+ array.size());


        System.out.println("----------------------------------------");

        System.out.println("method -> indexOf() & lastIndexOf() : ");


        System.out.println("( indexOf )-> returns the index of the element from the staring position : "+ array.indexOf(30));

        System.out.println("(lastIndexOf) -> return the index of the element from the end of the list : "+ array.lastIndexOf(30));


        System.out.println("----------------------------------------");


        System.out.println("method clear()");


        System.out.println("Removes all the elements form the arraylist");



        System.out.println("--------------------------------------");

        System.out.println("Displaying using the for each  and lambda function : ");

        array.forEach(arr -> System.out.println(arr + " "));


        System.out.println("Displaying using the iterator object");

        Iterator<Integer> itr = array.iterator();

        while(itr.hasNext())
        {
            int num  = itr.next();

            System.out.print(num + " ");
        }


    }
}