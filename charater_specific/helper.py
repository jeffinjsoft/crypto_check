from itertools import product
import crypt
from optparse import OptionParser


def parse_options():
    """
    Handle command-line options with optparse.OptionParser.

    Return list of arguments, largely for use in `parse_arguments`.
    """

    # Initialize
    parser = OptionParser(usage="main options --file")

    parser.add_option(
        '-f', '--file',
        dest="file",
        default=None,
        help="Give /etc/shadow file"
    )
    parser.add_option(
        '-u', '--user',
        dest="user",
        default=None,
        help="Give lookup username"
    )
    parser.add_option(
        '-m', '--max',
        dest="max_lookup",
        type=int,
        default=4,
        help="Give lookup max count"
    )
    parser.add_option(
        '-c', '--cha',
        dest="char_limit",
        type=int,
        default=4,
        help="Give lookup charater"
    )


    # Finalize
    # Return three-tuple of parser + the output from parse_args (opt obj, args)
    opts, args = parser.parse_args()
    return parser, opts, args



def check_hash(p,s,sha):
    c_pass = crypt.crypt(p,s)
    if c_pass == sha:
        return 1
    else:
        return 0

def split_arr(arr, size):
     arrs = []
     while len(arr) > size:
         pice = arr[:size]
         arrs.append(pice)
         arr   = arr[size:]
     arrs.append(arr)
     return arrs


def comp(nu):

    alphabets_l = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    alphabets_u = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']


    alphabets = alphabets_l+alphabets_u+numbers
    # print keywords

    keywords = [''.join(i) for i in product(alphabets, repeat = nu)]
    return keywords
