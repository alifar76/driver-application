# Driver-application

Background
------

Driver Coding assignment

System specs & required packages
------

All analysis were done on MacBook Pro, OS X El Capitan, Version 10.11.4. I used Python 2.7.12 with Anaconda 4.1.1. The built-in Python libraries used were:

- ```itertools```
- ```string```
- ```datetime```
- ```argparse```

How to use
------

There's a single script to perform this task and is present in the ```src``` folder. The script is called:

- ```reads_assembler.py```

To see help with script, simply type the following in the terminal:

```python reads_assembler.py -h```

An example on how to run the script is:

```python reads_assembler.py -i input_reads.txt -o genome_assembled.txt```

As seen from the example, the script takes in two arguments. The -i is the name of input file, which is FASTA file with the sequenced reads and -o is the name of the output file which is produced when the reads are assembled.

Algorithm Details
------

As can be seen in the ```reads_assembler.py```, there are 4 Python functions in the script. They are:

- ```fasta_iter```
- ```reverse_complement```
- ```find_overlap```
- ```generate_assembly```

The description of each of these functions/methods is provided in the docstring along with the expected parameters and the output.

Briefly, the algorithm works as follows:

1. The ```fasta_iter``` method is called first to read the FASTA file and store the sequences in a dictionary.
2. The ```generate_assembly``` method is next called on the input sequences from FASTA file to generate the assmbled sequence.
3. The ```find_overlap``` method is called internally from ```generate_assembly``` to find the overlap. ```generate_assembly``` then internally joins the two given sequences together based on the overlap.
4. The ```reverse_complement``` method is additionally called on the input/output of ```generate_assembly```, so as to take into account the fact that the input DNA sequence can come from either forward or reverse DNA strand.
