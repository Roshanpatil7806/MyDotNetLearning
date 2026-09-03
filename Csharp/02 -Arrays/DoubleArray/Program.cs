using System;

class Program
{
    static void Main()
    {
        int[,] arr =
        {
            { 10, 20, 30 },
            { 40, 50, 60 },
            { 70, 80, 90 }
        };

        // 1. Display
        Console.WriteLine("Array:");
        for (int i = 0; i < arr.GetLength(0); i++)
        {
            for (int j = 0; j < arr.GetLength(1); j++)
            {
                Console.Write(arr[i, j] + " ");
            }
            Console.WriteLine();
        }

        // 2. Sum
        int sum = 0;
        for (int i = 0; i < arr.GetLength(0); i++)
        {
            for (int j = 0; j < arr.GetLength(1); j++)
            {
                sum += arr[i, j];
            }
        }
        Console.WriteLine("Sum = " + sum);

        // 3. Maximum
        int max = arr[0, 0];

        for (int i = 0; i < arr.GetLength(0); i++)
        {
            for (int j = 0; j < arr.GetLength(1); j++)
            {
                if (arr[i, j] > max)
                    max = arr[i, j];
            }
        }
        Console.WriteLine("Maximum = " + max);

        // 4. Minimum
        int min = arr[0, 0];

        for (int i = 0; i < arr.GetLength(0); i++)
        {
            for (int j = 0; j < arr.GetLength(1); j++)
            {
                if (arr[i, j] < min)
                    min = arr[i, j];
            }
        }
        Console.WriteLine("Minimum = " + min);

        // 5. Search
        int search = 50;
        bool found = false;

        for (int i = 0; i < arr.GetLength(0); i++)
        {
            for (int j = 0; j < arr.GetLength(1); j++)
            {
                if (arr[i, j] == search)
                {
                    found = true;
                }
            }
        }

        Console.WriteLine("Search " + search + ": " +
                          (found ? "Found" : "Not Found"));
    }
}
