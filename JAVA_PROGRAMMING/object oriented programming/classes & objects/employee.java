class emp
{
    int emp_id;

    String emp_name;

    double emp_salary;

    int emp_experience;

    void emp_details()
    {
        System.out.println("Emp_id : " + emp_id);

        System.out.println("Emp_name : " + emp_name);

        System.out.println("Emp_salary : " + emp_salary);

        System.out.println("Emp_experience : " + emp_experience);
    }
}


public class employee {
    
    public static void main(String args[])
    {
        emp e1 = new emp();

        // for e1 employee

        e1.emp_id = 1;
        e1.emp_name = "abc";
        e1.emp_salary = 90000.00;
        e1.emp_experience = 5;

        e1.emp_details();

        
    }
}
