#IMPORTANT! Create a file called NeuralNNTf.xlsx. This is the file where your dataset will be made.
import pandas as pd
doc=pd.read_excel('NeuralNNTf.xlsx')
#Read a raw data file here

#get/convert data to the thing you will put in the dataset here

#this is the line to append your data to the dataframe, edit it.
doc=doc.append(pd.DataFrame('''Put your information as a 2d list here(replace this)''',columns=['''column names here(replace this)''']))
#Don't forget to keep some inputs you give as training data and loop over the read data file till it ends.
#save the dataset after all is done
doc.to_excel('NeuralNNTf.xlsx')
#keep checkpoints if your data file is huge