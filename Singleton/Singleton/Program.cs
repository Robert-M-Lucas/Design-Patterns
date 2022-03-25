using System;

// Singletons could be very useful in Unity where some features such as a server connection manager will only exist once

namespace Singleton
{
    class Program
    {
        static void Main(string[] args)
        {
            // MySingleton this_should_fail = new MySingleton(); - Inaccessible due to protection level

            MySingleton single = MySingleton.getInstance();

            single.count();
            single.count();
            single.count();
        }
    }
}
