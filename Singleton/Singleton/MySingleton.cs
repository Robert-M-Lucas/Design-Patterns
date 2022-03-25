using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Singleton
{
    public class MySingleton
    {
        private MySingleton() { } // Prevents instantiation

        private static MySingleton instance = new MySingleton();

        public static MySingleton getInstance()
        {
            return instance;
        }


        private int counter = 0;

        public void count()
        {
            Console.WriteLine(counter);
            counter++;
        }
    }
}
