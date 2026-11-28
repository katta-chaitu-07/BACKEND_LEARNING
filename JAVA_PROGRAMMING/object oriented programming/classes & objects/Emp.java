
class emp
{
    // properties of the emp classes

    String name;

    int employeeid;

    double salary;

    String department;

    // methods of the emp classes

    void displayDetails()
    {
        System.out.println("Emp id : " + name);

        System.out.println("Employee id : " + employeeid);

        System.out.println("salary : "+ salary );

        System.out.println("Employee department : "+department);
    }

    void increaseSalary(double salary)
    {
        System.out.println("Increase Salary : " + salary * 2);
    }

    void displayAnnualSalary(double salary)
    {
        System.out.println("Yearly salary : " + 12 * salary);
    }
}

public class Emp {
    
    public static void main(String args[])
    {
        emp e1 = new emp();

        e1.name = "chaitu";

        e1.employeeid = 101;
  
        e1.salary = 40000;

        e1.department = "Engineering";

        e1.displayDetails();

        e1.increaseSalary(e1.salary);

        e1.displayAnnualSalary(e1.salary);

        System.out.println("-----------------------------------------");

        //for employee two

        emp e2 = new emp();

        e2.name = "Rahul";

        e2.employeeid = 102;

        e2.salary = 35000;

        e2.department = "HR";

        e2.displayDetails();

        e2.increaseSalary(e2.salary);

        e2.displayAnnualSalary(e2.salary);

    

    }


}
