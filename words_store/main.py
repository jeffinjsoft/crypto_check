
from helper import comp_words


def generate_words(limit):
    k = comp_words(limit)
    print str(limit) + "--> "+str(len(k))

def main():
    print 'Staring main'
    for i in range(5):
        generate_words(i)



if __name__ == '__main__':
    main()
