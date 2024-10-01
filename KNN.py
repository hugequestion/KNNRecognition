from numpy import *
import operator
from os import listdir
from PIL import Image




#输入你需要识别的图片名
target = '8_test7'

#KNN分类算法
#inX：待测试的数据 （1，D）
#dataSet： 训练集  （n，D）
#labels：标签  （n，1）
#k：超参数
def classify0(inX, dataSet, labels, k):
    dataSetSize = dataSet.shape[0]                               #定义数据集的大小
    diffMat = tile(inX, (dataSetSize, 1)) - dataSet         #将维度统一

    #计算L2距离
    sqDiffMat = diffMat**2
    sqDistances = sqDiffMat.sum(axis=1)
    distances = sqDistances**0.5

    sortedDistIndicies = distances.argsort()                     #排序
    classCount={}                                                #定义字典用于接收k

    #找到k个最接近的标签并返回最多的那一个
    for i in range(k):
        voteIlabel = labels[sortedDistIndicies[i]]                 #从小到大统计距离最近的k个标签
        classCount[voteIlabel] = classCount.get(voteIlabel, 0) + 1 #统计每个标签出现的次数
    sortedClassCount = sorted(classCount.items(), key=operator.itemgetter(1), reverse=True)#将字典转化为元组降序（从大到小)排序
    return sortedClassCount[0][0]                                  #返回次数最多的标签，如果是[0][1]则是这个标签出现的个数




img = Image.open('I:/Python/pythonProject/selfDigits/'+target+'.jpg')
# 模式L”为灰色图像，它的每个像素用8个bit表示，0表示黑，255表示白，其他数字表示不同的灰度。
Img = img.convert('L')
Img.save('I:/Python/pythonProject/selfGrayDigits/'+'gray'+target+'.jpg')
# 自定义灰度界限，大于这个值为黑色，小于这个值为白色
maxvalve = 180
table = []
for i in range(256):
    if i < maxvalve:
        table.append(0)
    else:
        table.append(1)
# 图片二值化
photo = Img.point(table, '1')
photo.save("I:/Python/pythonProject/selfBinaryzationDigits/"+target+'.jpg')

img = Image.open("I:/Python/pythonProject/selfBinaryzationDigits/"+target+'.jpg')
new_img = img.resize((32, 32))
w, h = new_img.size
with open('I:/Python/pythonProject/output/'+target+".txt", "w") as f:
   for c in range(h):
        for j in range(w):
             f.write(str(int((255-(new_img.getpixel((j, c))))/255)))
             if j == w-1:
                  f.write("\n")
f.close()

#将图像转化为测试向量
def img2vector(filename):
    returnVect = zeros((1,1024))
    fr = open(filename)
    for i in range(32):
        lineStr = fr.readline()
        for j in range(32):
            returnVect[0, 32*i+j] = int(lineStr[j])
    return returnVect



#手写数字识别系统的测试代码
def handwritingClassTest():
    hwLabels = []
    trainingFileList = listdir('I:/Python/pythonProject/trainingDigits')           #load the training set
    m = len(trainingFileList)
    trainingMat = zeros((m, 1024))
    for i in range(m):
        fileNameStr = trainingFileList[i]
        fileStr = fileNameStr.split('.')[0]                #take off .txt
        classNumStr = int(fileStr.split('_')[0])
        hwLabels.append(classNumStr)
        trainingMat[i, :] = img2vector('I:/Python/pythonProject/trainingDigits/%s' % fileNameStr)
    testFileList = listdir('output')                    #iterate through the test set   listdir()函数输出文件夹下所有文件
    errorCount = 0.0
    mTest = len(testFileList)
    for i in range(mTest):
        fileNameStr = testFileList[i]                       #表示第几个文件
        fileStr = fileNameStr.split('.')[0]                 #take off .txt;   split()函数表示字符串以什么为分隔符;  fileStr表示没有后缀的文件名
        classNumStr = int(fileStr.split('_')[0])            #classNumStr表示文件_前的这个数字，也就是正确的结果
        vectorUnderTest = img2vector('I:/Python/pythonProject/output/%s' % fileNameStr)
        classifierResult = classify0(vectorUnderTest, trainingMat, hwLabels, 3)
        print("the classifier came back with: %d, the real answer is: %d" % (classifierResult, classNumStr))
        if (classifierResult != classNumStr):
            errorCount += 1.0
    print("\n the total number of errors is: %d" % errorCount)
    print("\n the total error rate is: %f" % (errorCount/float(mTest)))

handwritingClassTest()
