import os 

path = "/scratch/fs45/nlu/data/blimp/data/blimptask/"
filenames = [path+'superlative_quantifiers_2.txt',
             path+'superlative_quantifiers_1.txt',
             path+'existential_there_quantifiers_2.txt']
with open(os.path.join(path, 'concat_quantifier_train.txt'), 'w') as outfile:
    for fname in filenames:
        with open(fname) as infile:
            for line in infile:
                outfile.write(line)
