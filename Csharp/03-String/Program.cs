
using System;

class StringExample
{
    string text;

    // Constructor
    public StringExample(string text)
    {
        this.text = text;
    }

    public void Display()
    {
        Console.WriteLine("Original String : " + text);

        // 1. Length
        Console.WriteLine("Length           : " + text.Length);

        // 2. ToUpper()
        Console.WriteLine("Uppercase        : " + text.ToUpper());

        // 3. ToLower()
        Console.WriteLine("Lowercase        : " + text.ToLower());

        // 4. Trim()
        Console.WriteLine("Trim             : " + text.Trim());

        // 5. Contains()
        Console.WriteLine("Contains 'C#'    : " + text.Contains("C#"));

        // 6. StartsWith()
        Console.WriteLine("StartsWith 'I'   : " + text.StartsWith("I"));

        // 7. EndsWith()
        Console.WriteLine("EndsWith '!'     : " + text.EndsWith("!"));

        // 8. IndexOf()
        Console.WriteLine("IndexOf 'C#'     : " + text.IndexOf("C#"));

        // 9. LastIndexOf()
        Console.WriteLine("LastIndexOf 'a'  : " + text.LastIndexOf("a"));

        // 10. Replace()
        Console.WriteLine("Replace           : " + text.Replace("C#", "Java"));

        // 11. Substring()
        Console.WriteLine("Substring         : " + text.Substring(0, 5));

        // 12. Insert()
        Console.WriteLine("Insert            : " + text.Insert(0, "Hello "));

        // 13. Remove()
        Console.WriteLine("Remove            : " + text.Remove(0, 2));

        // 14. Equals()
        Console.WriteLine("Equals            : " + text.Equals("I Love C#!"));

        // 15. Compare()
        Console.WriteLine("Compare           : " + string.Compare(text, "I Love C#!"));

        // 16. IsNullOrEmpty()
        Console.WriteLine("IsNullOrEmpty     : " + string.IsNullOrEmpty(text));

        // 17. IsNullOrWhiteSpace()
        Console.WriteLine("IsNullOrWhiteSpace : " + string.IsNullOrWhiteSpace(text));

        // 18. Split()
        string[] words = text.Split(' ');

        Console.WriteLine("Split Words:");
        foreach (string word in words)
        {
            Console.WriteLine(word);
        }

        // 19. Join()
        Console.WriteLine("Join              : " + string.Join("-", words));

        // 20. Concat()
        Console.WriteLine("Concat            : " + string.Concat(text, " Welcome"));

        // 21. PadLeft()
        Console.WriteLine("PadLeft           : " + text.PadLeft(20, '*'));

        // 22. PadRight()
        Console.WriteLine("PadRight          : " + text.PadRight(20, '*'));
    }
}

class Program
{
    static void Main()
    {
        StringExample obj = new StringExample("I Love C#!");

        obj.Display();
    }
}