class string
{
    public static void main(String args[])
    {
        String a = "java";  // Immutable

        String b = "java"; // immutabe (cannot change)

        // ( == ) checks the reference not the content

        System.out.println(a == b); // prints (true)

         

        // second way to create string by using object 

        String c = new String("Java"); // new reference

        String d = new String("Java"); // new reference

        System.out.println(c == d); // both reference different so it prints false;


    }
}