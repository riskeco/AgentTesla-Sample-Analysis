
using System;
using System.Collections;
using System.Drawing;
using System.Globalization;
using System.IO;
using System.Reflection;
using System.Resources;
using System.Text;
using System.Runtime.Serialization.Formatters.Binary;


namespace DotNetExtraction
{
    public class DotNetExtractor
    {
	private static void storeContent(string basedir, string basename, string key, string ext, byte [] content) {

	    int length = basename.Length;

	    while (length > 0) {

		string filename = basename.Substring(0, length);

		string target = "res-" + filename + "-" + key + "." + ext;

		try {

		    using(FileStream stream = new FileStream(target, FileMode.Create)) {

			stream.Write(content);

		    }

		    break;

		}

		catch (System.IO.PathTooLongException) {

		    length--;


		}

	    }

	}

	public static void Main(string[] args)
	{
	    CultureInfo culture = CultureInfo.InvariantCulture;

	    foreach (string arg in args) {

		string basename = Path.GetFileNameWithoutExtension(arg);

		string basedir = Path.GetDirectoryName(arg);

		Console.WriteLine("");

		Console.WriteLine("[*] ------ Processing " + basename + " ------");

		ResourceManager rm = ResourceManager.CreateFileBasedResourceManager(basename, basedir, null);

		ResourceSet rs = rm.GetResourceSet(culture, true, true);

		if (rs != null) {

		    IDictionaryEnumerator dict = rs.GetEnumerator();

		    while (dict.MoveNext()) {

			string key = (string) dict.Key;

			if (dict.Value is byte[]) {

			    Console.WriteLine("[i] Extracting resource '{0}' as bytes", key);

			    storeContent(basedir, basename, key, "bin", (byte [])rs.GetObject(key));

			}

			else if (dict.Value is System.Drawing.Bitmap) {

			    Console.WriteLine("[i] Extracting resource '{0}' as image data", key);

			    System.Drawing.Bitmap img = (Bitmap)rs.GetObject(key);

			    ImageConverter converter = new ImageConverter();

			    storeContent(basedir, basename, key, "img", (byte [])converter.ConvertTo(img, typeof(byte [])));

			}

			else
			    Console.WriteLine("[!] Unhandled resource type for '{0}': {1}", key, dict.Value);

		    }

		}

	    }

	}
 
    }

}
