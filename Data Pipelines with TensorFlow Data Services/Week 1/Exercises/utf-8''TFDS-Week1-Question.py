#!/usr/bin/env python
# coding: utf-8

# # Rock, Paper, Scissors
# 
# In this week's exercise you will be working with TFDS and the rock-paper-scissors dataset. You'll do a few tasks such as exploring the info of the dataset in order to figure out the name of the splits. You'll also write code to see if the dataset supports the new S3 API before creating your own versions of the dataset.

# ## Setup

# In[1]:


# Use all imports
from os import getcwd

import tensorflow as tf
import tensorflow_datasets as tfds


# ## Extract the Rock, Paper, Scissors Dataset
# 
# In the cell below, you will extract the `rock_paper_scissors` dataset and then print its info. Take note of the splits, what they're called, and their size.

# In[11]:


# EXERCISE: Use tfds.load to extract the rock_paper_scissors dataset.

filePath = f"{getcwd()}/../tmp2"
# YOUR CODE HERE (Include the following argument in your code: data_dir=filePath)
data, info = tfds.load("rock_paper_scissors",data_dir=filePath, with_info=True)
print(info)


# In[12]:


# EXERCISE: In the space below, write code that iterates through the splits
# without hardcoding any keys. The code should extract 'test' and 'train' as
# the keys, and then print out the number of items in the dataset for each key. 
# HINT: num_examples property is very useful here.

for set in data:# YOUR CODE HERE:
  print(set,":",info.splits[set].num_examples) # YOUR CODE HERE

# EXPECTED OUTPUT
# test:372
# train:2520


# ## Use the New S3 API
# 
# Before using the new S3 API, you must first find out whether the `rock_paper_scissors` dataset implements the new S3 API. In the cell below you should use version `3.*.*` of the `rock_paper_scissors` dataset.

# In[16]:


# EXERCISE: In the space below, use the tfds.builder to fetch the
# rock_paper_scissors dataset and check to see if it supports the
# new S3 API. 
# HINT: The builder should 'implement' something

# YOUR CODE HERE (Include the following arguments in your code: "rock_paper_scissors:3.*.*", data_dir=filePath)
rps_builder = tfds.builder("rock_paper_scissors:3.*.*",data_dir=filePath)

print(rps_builder.version.implements(tfds.core.Experiment.S3))# YOUR CODE HERE)

# Expected output:
# True


# ## Create New Datasets with the S3 API
# 
# Sometimes datasets are too big for prototyping. In the cell below, you will create a smaller dataset, where instead of using all of the training data and all of the test data, you instead have a `small_train` and `small_test` each of which are comprised of the first 10% of the records in their respective datasets.

# In[17]:


# EXERCISE: In the space below, create two small datasets, `small_train`
# and `small_test`, each of which are comprised of the first 10% of the
# records in their respective datasets.

# YOUR CODE HERE (Include the following arguments in your code: "rock_paper_scissors:3.*.*", data_dir=filePath)
small_train = tfds.load("rock_paper_scissors:3.*.*", split='train[:10%]',data_dir=filePath)
# YOUR CODE HERE (Include the following arguments in your code: "rock_paper_scissors:3.*.*", data_dir=filePath)
small_test = tfds.load("rock_paper_scissors:3.*.*", split='test[:10%]',data_dir=filePath)

# No expected output yet, that's in the next cell


# In[18]:


# EXERCISE: Print out the size (length) of the small versions of the datasets.

# YOUR CODE HERE)
print(len(list(small_train)))

# YOUR CODE HERE)
print(len(list(small_test)))

# Expected output
# 252
# 37


# The original dataset doesn't have a validation set, just training and testing sets. In the cell below, you will use TFDS to create new datasets according to these rules:
# 
# * `new_train`: The new training set should be the first 90% of the original training set.
# 
# 
# * `new_test`: The new test set should be the first 90% of the original test set.
# 
# 
# * `validation`: The new validation set should be the last 10% of the original training set + the last 10% of the original test set.

# In[19]:


# EXERCISE: In the space below, create 3 new datasets according to
# the rules indicated above.

# YOUR CODE HERE (Include the following arguments in your code: "rock_paper_scissors:3.*.*", data_dir=filePath)
new_train = tfds.load("rock_paper_scissors:3.*.*", split='train[:90%]',data_dir=filePath) 
print(len(list(new_train)))

# YOUR CODE HERE (Include the following arguments in your code: "rock_paper_scissors:3.*.*", data_dir=filePath)
new_test = tfds.load("rock_paper_scissors:3.*.*", split='test[:90%]',data_dir=filePath)
print(len(list(new_test)))

# YOUR CODE HERE (Include the following arguments in your code: "rock_paper_scissors:3.*.*", data_dir=filePath)
validation = tfds.load("rock_paper_scissors:3.*.*", split='train[90%:] + test[90%:]',data_dir=filePath)
print(len(list(validation)))


# Expected output
# 2268
# 335
# 289


# # Submission Instructions

# In[ ]:


# Now click the 'Submit Assignment' button above.


# # When you're done or would like to take a break, please run the two cells below to save your work and close the Notebook. This frees up resources for your fellow learners.

# In[ ]:


get_ipython().run_cell_magic('javascript', '', '<!-- Save the notebook -->\nIPython.notebook.save_checkpoint();')


# In[ ]:


get_ipython().run_cell_magic('javascript', '', '<!-- Shutdown and close the notebook -->\nwindow.onbeforeunload = null\nwindow.close();\nIPython.notebook.session.delete();')

