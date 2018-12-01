using System;
using System.IO;
using System.Collections.Generic;
using System.Linq;


namespace ChronalCalibration
{
    class Program
    {
        static void Main(string[] args)
        {
            string[] lines = File.ReadAllLines("../data.txt");
            List<int> frequencies = new List<int>();
            foreach (var line in lines) {
                frequencies.Add(Int32.Parse(line));
            }
            Console.WriteLine(frequencies.Sum());

            var currentFrequency = 0;
            List<int> seenFrequencies = new List<int>();
            int count = 0;
            while (true)
            {
                foreach (int frequency in frequencies) {
                    currentFrequency += frequency;
                    if (seenFrequencies.Contains(currentFrequency)) {
                        Console.WriteLine(currentFrequency);
                        Environment.Exit(0);
                    }
                    seenFrequencies.Add(currentFrequency);
                }
                count += 1;
                Console.WriteLine(String.Format("pass {0} {1}", count, seenFrequencies.Count()));
            }
        }
    }
}
