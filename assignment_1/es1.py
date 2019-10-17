import os
import argparse
import logging
import time
import matplotlib
import matplotlib.pyplot as plt
logging.basicConfig(level=logging.INFO)

_description = 'Measure the relative frequencies of letter in a text file'

#Per il file di log

def process(file_path):
    """Main processing routine.
    """

    #Start timer
    start_time = time.time()
    
    #Basic sanity cheks
    assert file_path.endswith('.txt')
    assert os.path.isfile(file_path)

    #Good to go---open the input filr
    logging.info('Opening file %s...', file_path)
    with open(file_path) as input_file:
        data = input_file.read()
    logging.info('Done. %d character(s) found.', len(data))

    #Initialize a dictionary with all the lowercase letters.
    letters = 'abcdefghijklmnopqrstuvwxyz'
    frequency_dict = {}
    for ch in letters:
        frequency_dict[ch] = 0

    #Loop over the actual data
    logging.info('Looping over the input text')
    for ch in data.lower():
        if ch in letters:
            frequency_dict[ch] += 1

    num_characters = float(sum(frequency_dict.values()))

    #Normalize the occurences.
    for ch in letters:
        frequency_dict[ch] = frequency_dict[ch]/num_characters
            
    # We're done---print the glorious output. (And here it is appropriate to
    # use print() instead of logging.)
    for ch, freq in frequency_dict.items():
        print('{}: {:.3f}%'.format(ch, freq * 100.))

    if args.plot:
        matplotlib.use( 'Qt5Agg' )
        plt.bar(*zip(*frequency_dict.items()))

    #if args.stats:

    #Stop timer
    stop_time = time.time()
    elapsed_time = stop_time - start_time

    message_time = f"Elapsed time: {elapsed_time}s"
    print(message_time)

    if args.plot:
        #plt.ion()
        plt.show()
    
#Se questo script e il programma principale (main) definisco le opzioni di lunch
#altrimenti se la devo importare come funzione
#non voglio che abbia le opzioni

if __name__ == '__main__':
   parser = argparse.ArgumentParser(description=_description)
   parser.add_argument('infile', help='path to the input txt file')
   parser.add_argument("-p", "--plot", help="plot a histogram of the frequencies", action="store_true")
   parser.add_argument("-b", "--body", help="processes only the text pertaining the book", action="store_true")
   parser.add_argument("-s", "--stats", help="print out the basic book stats", action="store_true")
   args = parser.parse_args()
   process(args.infile)
