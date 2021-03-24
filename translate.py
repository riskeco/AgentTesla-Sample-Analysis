
import argparse
import re


if __name__ == '__main__':
    """Point d'entrée du programme."""

    parser = argparse.ArgumentParser(description='Process a C# file.', add_help=False)

    parser.add_argument('-h', '--help', action='store_true', help='Display the command line options')

    parser.add_argument('-b', '--build', action='store_true', help='Build a list of encryption identifiers')
    parser.add_argument('filename', type=str, help='source code file to process')

    args = parser.parse_args()

    if args.help:
        parser.print_help()
        sys.exit(1)

    if not(args.build):

        new_content = ''

        translations = {}

        with open('decrypted-strings.txt', 'rb') as fd:
            content = fd.read()

        for line in content.split(b'\r\n'):

            if len(line) == 0:
                continue

            try:

                parts = line.split(b':')
                index = int(parts[0].decode('ascii'))

                translations[index] = parts[1][1:].decode('utf8')

            except:
                translations[index] = "TO DO"
                print('ERROR for: ', parts[1][1:])
                #import sys
                #sys.exit(0)


    with open(args.filename, 'r') as fd:
        lines = fd.read()

    #if True:

        #line='xma.xfs = Conversions.ToString(xwd.cgj(Strings.Split(Strings.Split(text, <Module>.smethod_0(117028), -1, CompareMethod.Binary)[1], <Module>.smethod_0(117068), -1, CompareMethod.Binary)[0]));'
    for line in lines.split('\n'):

        if args.build:

            for m in re.finditer(r'<Module>.smethod_0\(([0-9]*)\)', line):

                print('%s,' % m.group(1))

        else:

            m = re.search(r'<Module>.smethod_0\(([0-9]*)\)', line)

            while m:

                index = int(m.group(1))

                if index in translations.keys():

                    dec = '"%s"' % translations[index]

                else:

                    dec = '<no decrypted string>'

                line = line[:m.start()] + dec + line[m.end():]

                m = re.search(r'<Module>.smethod_0\(([0-9]*)\)', line)

            #print(line)
            
            new_content += line + '\r\n'

    if not(args.build):

        with open(args.filename, 'w') as fd:
            fd.write(new_content)
