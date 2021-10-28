"""
Pytorch is an open source machine learning and deep learning library associated with the torch api.
One of the fundamental class fucntion of torch is Tensor, used to create tensor (an algebraic object used to reference with the vector space).
I want to share 5 important Tensor operationi think is the best everyone should know about!
"""

# Import torch and other required modules (Make sure you have pytorch installed.)
import torch


# THE RANDOM FUNCTION
# The randn() function is a very interesting function used to generate a tensor matrix whose mean of every elements will be 0 and variance will be 1 and takes row as the first arguement and the column as the second arguement.
tensor = torch.randn(2, 3)
print(tensor)

# It will cause error if you put a decimalvalue in the row or column's place or a negetive number.


# =======================================================================================================================================

# THE EYE FUNCTION
# Eye() is simply the function to generate an identity matrix. Identity matrix is a well known fundamental matrix in the fieldof Linear Algebra. It's also very handy for scientist doing research using pytorch.
mtrx1 = 1 * torch.eye(3)
print(mtrx1)

mtrx2 = -25 * torch.eye(5)
print(mtrx2)

"""
the ouput will look like this:

tensor([[1., 0., 0.],
        [0., 1., 0.],
        [0., 0., 1.]])

tensor([[-25.,  -0.,  -0.,  -0.,  -0.],
        [ -0., -25.,  -0.,  -0.,  -0.],
        [ -0.,  -0., -25.,  -0.,  -0.],
        [ -0.,  -0.,  -0., -25.,  -0.],
        [ -0.,  -0.,  -0.,  -0., -25.]])

Do you see the pattern? One could easily create an identity matrix with for loops and fucntions, but for the sake of basicity of idenity matrix, there exist the eye() function.
"""


# =======================================================================================================================================

# THE TRANSPOSE FUNCTION
# t() function is used to get the transpose of a tensor matrix. As once my teacher said to us in my highschool. For the sake of simplicity, tarnspose of a matrixis just rotating the matrix in such a way so, row becomescolumn and column becomes row.
tensor = torch.tensor([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("Real matrix: \n", tensor)

transpose = tensor.t()
print("Transpose: \n", transpose)

# As said in the documentation when using t() as a tensor construction function instead of a object function of that particluar tensor instance, only tensors should be passed, anything else like lists wont workout.


# =======================================================================================================================================

# THE MEAN FUNCTION
# Mean() is used to find the mean value of all the elements collectively in the tensor matrix
# Example of mean
tensor = torch.tensor([2, 3, 4, 5.0])
print(tensor)
print("Mean: ", torch.mean(tensor))

# If you use a caclculator you will see the mean to be 3.5. The function will raise an error if you put only inetegr values in the tensor


# =======================================================================================================================================

# THE SORT FUNCTION
# The sort function is as it sounds. It sorts the elements inside the tensor matris in descending or ascending order only in that row. The function outputs two values, the index and the ordered matrix
tensor = torch.tensor([[1, 3, 2], [6, 5, 4], [8, 9, 7]])
print("Real matrix: \n", tensor)

# descending order
order, index = torch.sort(tensor, dim=0, descending=True)
print("order: \n", order)
print("index: \n", index)

# ascending order
order, index = torch.sort(tensor, dim=-1, descending=False)
print("order: \n", order)
print("index: \n", index)

"""
The output would look like:

Real matrix: 
 tensor([[1, 3, 2],
        [6, 5, 4],
        [8, 9, 7]])
order: 
 tensor([[8, 9, 7],
        [6, 5, 4],
        [1, 3, 2]])
index: 
 tensor([[2, 2, 2],
        [1, 1, 1],
        [0, 0, 0]])
order: 
 tensor([[1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]])
index: 
 tensor([[0, 2, 1],
        [2, 1, 0],
        [2, 0, 1]])

 In the example the dim is the kwarg which explcitly lets us define which number would we want as the first number in the index. The dim couldbe only, -2, -1, 0 and 1.

Anything different than that throws an error. Its a very good process to be used in data analysis to mine insights!
"""

# =======================================================================================================================================
