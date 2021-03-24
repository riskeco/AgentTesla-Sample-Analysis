
using System;

namespace CyaX_Config
{
    public class CyaX_Config
    {
	public static void Main(string[] args)
	{
	    string k = "4||1||0||0||0||||||0||0||0||0||||||||||||||0||0||0||0||0||0||0||0||v4||0||2883||";

	    string[] aa = k.Split("||"); //, -1, CompareMethod.Binary);

	    Console.WriteLine("InjectValue: " + aa[0]);

	    Console.WriteLine("isStartup: " + aa[1]);

	    Console.WriteLine("UAC: " + aa[2]);

	    Console.WriteLine("Downloader: " + aa[4]);

	    Console.WriteLine("DownloaderFileName: " + aa[6]);

	    Console.WriteLine("DownloaderLink: " + aa[5]);

	    Console.WriteLine("AntiVm: " + aa[7]);

	    Console.WriteLine("AntiSB: " + aa[8]);

	    Console.WriteLine("AntiEm: " +aa[9]);


	}

    }

}
