# In this homework, you will write a Python program to make some calculations on 3D pixels of some images.
# We will use the ppm image format for reading image files. You are provided with two functions:
# read_ppm_file(f) which (is a function you are familiar with from the lectures) will enable you to read .ppm files to a 3d list.
# img_printer(img) which is a function that prints 3d lists in a readable manner. You will use this and only this to output your results.
# Two of the inputs you need are taken for you, filename and operation.
# filename is the name of the .ppm file you will read, and operation is a specific operation which you will apply to the image you read.
# The rest of the inputs you take will depend on the operation. filename will always belong to files in src folder, so you can directly use them with the filename #variable.
# operation will always be an integer between 1-7, both inclusive. The details of the operations are as follows:
# operation == 1
# When operation input is 1, you will apply min-max normalization.
# In this case you will require two additional inputs: minimum and maximum, which you will also get from the user once this option is chosen.
# Each input will be given in separate lines. You can assume that these two values are integers.
# The formula for min-max normalization is as follows:

![minmax_norm](https://user-images.githubusercontent.com/124915257/221966306-b292f2ac-57bd-4422-af3a-49a78957ff16.png)
