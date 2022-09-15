import os, shutil, datetime, fileinput

def nicepath(dir):
    "①文件夹存在②有jpg③有list④list不为空，都满足则返回1"
    if os.path.exists(dir) & os.path.exists(dir + '/list.txt'):
        imgFile = os.listdir(dir)
        for i in range(len(imgFile)):
            imgFile[i] = os.path.splitext(imgFile[i])[1]
        if '.jpg' in imgFile:
            size = os.path.getsize(dir + '/list.txt')
            if size != 0:
               return 1

workPath = os.path.abspath(os.path.dirname(__file__))
os.chdir(workPath)

# Step 1: 确定原图路径：

if nicepath('special')==1:    # 优先选special
    imgDir = '/special/'
else:   # 其次选对应的纪念日（文件夹名格式为MMDD）
    t = datetime.datetime.now()
    dateDir = t.__format__('%m%d')
    if nicepath(dateDir)==1:
        imgDir = '/' + dateDir + '/'
    else:
        imgDir = '/screenshots/'    # 不符合特殊条件就选默认文件夹

imgPath = workPath + imgDir
os.chdir(imgPath)   # 切换工作文件夹到原图路径

# Step 2: 移动图片

# 读取list第一行然后删除
fileName = 'fileName'
while os.path.exists(fileName) is False: # 如果第一行文件不存在，则删除后再读下一行
   with open('list.txt', 'r', encoding='utf-8') as f:
      fileName = f.readline().rstrip()
   for line in fileinput.input('list.txt', inplace=1):
      if not fileinput.isfirstline():
         print(line.replace('\n',''))
# 移动相应图片并记录
logContents = imgDir[1:] + fileName + "\t"  + str(datetime.datetime.now())+ "\n"
shutil.move(imgPath + fileName, workPath + '/img.jpg')
with open(workPath + '/imgpicked.log', 'a+', encoding='utf-8') as log:
    log.write(logContents)

# Step 3: 输出图片描述文alt
imgAlt = fileName[:-4] # 即文件名去掉最后的'.jpg'
print(imgAlt)