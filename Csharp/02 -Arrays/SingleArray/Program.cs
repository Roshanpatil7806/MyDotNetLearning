using System;

class Program
{
    static void Main()
    {
        int[] numbers = { 50, 20, 40, 10, 30 };

        // Display
        Console.WriteLine("Array Elements:");
        for (int i = 0; i < numbers.Length; i++)
        {
            Console.Write(numbers[i] + " ");
        }

        // Sum
        int sum = 0;
        for (int i = 0; i < numbers.Length; i++)
        {
            sum += numbers[i];
        }
        Console.WriteLine("\n\nSum = " + sum);

        // Average
        double average = (double)sum / numbers.Length;
        Console.WriteLine("\nAverage = " + average);

        // Maximum
        int max = numbers[0];
        for (int i = 1; i < numbers.Length; i++)
        {
            if (numbers[i] > max)
                max = numbers[i];
        }
        Console.WriteLine("\nMaximum = " + max);

        // Minimum
        int min = numbers[0];
        for (int i = 1; i < numbers.Length; i++)
        {
            if (numbers[i] < min)
                min = numbers[i];
        }
        Console.WriteLine("\nMinimum = " + min);

        // Search
        int search = 40;
        bool found = false;

        for (int i = 0; i < numbers.Length; i++)
        {
            if (numbers[i] == search)
            {
                found = true;
                break;
            }
        }

        Console.WriteLine("\nSearch " + search + ": " +
                          (found ? "Found" : "Not Found"));

        // Sort
        Array.Sort(numbers);
        Console.WriteLine("Sorted Array:");
        foreach (int n in numbers)
        {
            Console.Write(n + " ");
        }

        // Reverse
        Array.Reverse(numbers);
        Console.WriteLine("\nReverse Array:");
        foreach (int n in numbers)
        {
            Console.Write(n + " ");
        }
    }
}