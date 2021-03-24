
import argparse


def unscramble(data):
    """Decrypt data with an embedded key."""

    key = data[:16]

    data = data[16:]

    decrypted = []

    for i in range(len(data)):

        decrypted.append(data[i] ^ key[i % 16])

    return decrypted


def xor_dec(data, key):
    """Decrypt data with an external key."""

    klen = len(key)

    num2 = data[-1] ^ 112

    decrypted = []

    for i in range(len(data)):

        decrypted.append(data[i] ^ num2 ^ key[i % int(klen / 2)])

    return decrypted


def to_big_endian_unicode(data):
    """Emulate a call Encoding.BigEndianUnicode.GetBytes()."""

    big = []

    for d in data:
        big.append(0)
        big.append(ord(d))

    return big


if __name__ == '__main__':
    """Point d'entrée du programme."""

    parser = argparse.ArgumentParser(description='Python translation of the Extra class features', add_help=False)

    parser.add_argument('-h', '--help', action='store_true', help='Display the command line options')

    parser.add_argument('resource', help='Resource file to process', type=str)
    parser.add_argument('--key', type=str, help='Key to use for XOR decryption', required=False)

    args = parser.parse_args()

    with open(args.resource, 'rb') as fd:
        data = fd.read()

    if args.key:

        print('[*] Decrypting %s' % args.resource)

        master_key = to_big_endian_unicode(args.key)

        data = xor_dec(data, master_key)

    print('[*] Unscrambling %s' % args.resource)

    data = unscramble(data)

    output = args.resource + '.plain'

    print('[*] Writing %s...' % output)

    with open(output, 'wb') as fd:
        fd.write(bytes(data))
