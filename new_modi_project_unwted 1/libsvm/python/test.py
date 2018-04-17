from svmutil import *
svm_model.predict = lambda self, x: svm_predict([0], [x], self)[0][0]

prob = svm_problem([1,-1,2], [[1,0,1], [-1,0,-1],[2,15,2]])

param = svm_parameter()
param.kernel_type = LINEAR
param.C = 10

m=svm_train(prob, param)

c =m.predict([1,19,1])
print c
