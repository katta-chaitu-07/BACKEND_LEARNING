
public class student {
    
      int id; // instance variable

      String name; // instance variable 

      double percentage; // instance variable 


      void student_details()
      {

         System.out.println("Id : " + id);
         System.out.println("Name : " + name);
         System.out.println("Percentage : " + percentage);
      }

      void study()
      {
        System.out.println("Name : " + name + "is studying java");
      }

      public static void main(String args[])
    {
        student s1 = new student();

        // for student s1 

        s1.id = 1;
        s1.name = "chaitu";
        s1.percentage = 95.5;

        s1.student_details();

        s1.study();

        // for student s2 

        student s2 = new student();

        s2.id = 2;

        s2.name = "chandu";

        s2.percentage = 97.75;

        s2.student_details();

        s2.study();
    }
}

