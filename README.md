
# Product categorization
##### The main use case is classifying products

# Usage

#### Basic Usage
###### Use this online app: http://13.58.82.53:5000/

>>> import pickle
>>> filename = 'finalized_model.sav'
>>> loaded_model = pickle.load(open(filename, 'rb'))
>>> new_product = """ابرار تمر بالسودانى 400 جم"""
>>> print(loaded_model.predict([new_product])[0])
>>> predicted_lst= loaded_model.predict_proba([new_product])
>>> print("your product belongs to this category with probability of: ", predicted_lst.max())
البسكويت والمقرمشات والكيك
your product belongs to this category with probability of:  0.9706195555761513
