import os, shutil, datetime, fileinput

def nicepath(dir):
    "①文件夹存在②有jpg③有list④list不为空，都满足则返回1"
    # 检查文件夹是否存在
    if not os.path.exists(dir):
        with open('error.log', 'a', encoding='utf-8') as f:
            f.write(f'Error: folder "{dir}" does not exist.\n')
        return 0
    # 检查是否有 jpg 文件
    imgFiles = [f for f in os.listdir(dir) if f.endswith('.jpg')]
    if not imgFiles:
        with open('error.log', 'a', encoding='utf-8') as f:
            f.write(f'Error: no jpg files found in folder "{dir}".\n')
        return 0
    # 检查是否有 list.txt 文件且不为空
    listFile = os.path.join(dir, 'list.txt')
    if not os.path.exists(listFile):
        with open('error.log', 'a', encoding='utf-8') as f:
            f.write(f'Error: list.txt not found in folder "{dir}".\n')
        return 0
    elif os.path.getsize(listFile) == 0:
        with open('error.log', 'a', encoding='utf-8') as f:
            f.write(f'Error: list.txt in folder "{dir}" is empty.\n')
        return 0
    # 满足所有条件，返回 1
    return 1

workPath = os.path.abspath(os.path.dirname(__file__))
os.chdir(workPath)

# Step 1: 确定原图路径：

SPECIAL_DIR = '/special/'
SCREENSHOTS_DIR = '/screenshots/'
#这里可以修改special文件夹和默认的普通截图文件夹

if nicepath('special')==1:    # 优先选special
    imgDir = SPECIAL_DIR
else:   # 其次选对应的纪念日（文件夹名格式为MMDD）
    t = datetime.datetime.now()
    dateDir = t.strftime('%m%d')
    if nicepath(dateDir)==1:
        imgDir = '/' + dateDir + '/'
    else:
        imgDir = SCREENSHOTS_DIR    # 不符合特殊条件就选默认文件夹

imgPath = workPath + imgDir
os.chdir(imgPath)   # 切换工作文件夹到原图路径

# Step 2: 移动图片

myList = os.path.join(imgPath, 'list.txt')
fileName = next(open(myList)).strip()
while not os.path.exists(fileName):
    os.system(f'sed -i "1d" {myList}')
    fileName = next(open(myList)).strip()  # 得到fileName字符串

# 移动jpg文件，记录原图文件夹、文件名和时间
logContents = f"{imgDir[1:]}{fileName}\t{str(datetime.datetime.now())[:-4]}\n"
shutil.move(os.path.join(imgPath, fileName), os.path.join(workPath, 'img.jpg'))
with open(os.path.join(workPath, 'imgpicked.log'), 'a', encoding='utf-8') as log:
    log.write(logContents)

# Step 3: 输出图片文件名（去掉.jpg后缀和多余换行符）
print(fileName[:-4], end='') 