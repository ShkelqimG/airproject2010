from svmutil import *

y,x = svm_read_problem('../heart_scale')
print type(svm_parameter('-c 4 -b 1'))
