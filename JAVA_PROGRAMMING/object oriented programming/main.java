class Student {

    String name;
    int age;

    void student_data() {

        System.out.println("Student name: " + name);
        System.out.println("Student age: " + age);
    }
}

public class main {

    public static void main(String[] args) {

        // Creating first object
        Student s1 = new Student();

        s1.name = "Chaitanya";
        s1.age = 20;

        // Creating second object
        Student s2 = new Student();

        s2.name = "Rahul";
        s2.age = 22;

        // Calling methods
        s1.student_data();

        System.out.println();

        s2.student_data();
    }
}