using System;

class Student
{
    
    public int Id;
    public string Name;
    public int Age;

    
    public Student(int id, string name, int age)
    {
       this.Id =id;
       this.Name =name;
       this.Age =age;
    }

    
    public void Display()
    {
        Console.WriteLine("Student ID: " + Id);
        Console.WriteLine("Student Name: " + Name);
        Console.WriteLine("Student Age: " + Age);
    }
}

class Program
{
    static void Main()
    {
        
        Student s1 = new Student(101, "Roshan", 22);

        
        s1.Display();
    }
}
