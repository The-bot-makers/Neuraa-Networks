import tensorflow as tf
import pandas as pd
#reading the dataset. keep your dataset path in the quotes
doc=pd.read_excel('')
#get the needed data here



#convert stuff to tensorflow readable arrays. x_train is the data while y_train is the labels.
x_train=[]
y_train=[]



#add layers in the model by model.add(<layer>)
model = tf.keras.models.Sequential()




#compile the model. you may keep your preffered choices here.
model.compile(optimizer='adam',
              loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
              metrics=['accuracy'])
#train the model. keep your values here if you like.
model.fit(x_train, y_train, epochs=200, batch_size=50)
#save the model in your computer. specify the path.
model.save('<path here(replace this)>')