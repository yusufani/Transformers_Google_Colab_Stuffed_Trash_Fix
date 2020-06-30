# Transformers_Google_Colab_Stuffed_Trash_Fix
 When you train a model  in Google Colab with transformers api, you probably encountered Stuffed Google Drive Trash. Because of Google Drive extra manually confirm for deleting trash bin  ,you model will stop due to hasn't enough disk avaiable. I just change delete method  : I do not delete models, just replace a empty file :D

# Usage

![Alt text](images/1.png?raw=true "SS")

![Alt text](images/2.png?raw=true "SS")

![Alt text](images/3.png?raw=true "SS")

![Alt text](images/4.png?raw=true "SS")

![Alt text](images/5.png?raw=true "SS")

![Alt text](images/6.png?raw=true "SS")

Path : /usr/local/lib/python3.6/dist-packages/transformers/trainer.py
