import os, shutil, datetime, fileinput

def jpg(dir):
    "判断文件夹是否存在并含有jpg文件"
    if os.path.exists(dir):
        imgFile = os.listdir(dir)
        for i in range(len(imgFile)):
            imgFile[i] = os.path.splitext(imgFile[i])[1]
        if '.jpg' in imgFile:
            return 1

workPath = os.path.abspath(os.path.dirname(__file__))
os.chdir(workPath)

# Step 1: 确定原图路径：

if jpg('special')==1:    # 优先选special
    imgDir = '/special/'
else:   # 其次选对应的纪念日（文件夹名格式为MMDD）
    t = datetime.datetime.now()
    dateDir = t.__format__('%m%d')
    if jpg(dateDir)==1:
        imgDir = '/' + dateDir + '/'
    else:
        imgDir = '/screenshots/'    # 不符合特殊条件就选默认文件夹

imgPath = workPath + imgDir   # 原图路径，里面有jpg文件和对应的list.txt
os.chdir(imgPath)

# Step 2: 移动图片

# 读取list第一行
f = open('list.txt', 'r', encoding='utf-8')
fileName = f.readline().rstrip()
f.close()
# 移动相应图片并记录
logContents = imgDir[1:] + fileName + "\t"  + str(datetime.datetime.now())+ "\n"
shutil.move(imgPath + fileName, workPath + '/img.jpg')
log = open(workPath + '/imgpicked.log', 'a+', encoding='utf-8')
log.write(logContents)
log.close()
# 删除读取过的行
for line in fileinput.input('list.txt', inplace=1):
    if not fileinput.isfirstline():
        print(line.replace('\n',''))

# Step 3: 输出图片描述文alt
imgAlt = fileName[:-4] # 即文件名去掉最后的'.jpg'
print(imgAlt)