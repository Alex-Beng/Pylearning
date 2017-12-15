import jieba.analyse
import PIL
import matplotlib.pyplot as plot
import wordcloud
import numpy

with open('三体1.txt',encoding='ansi') as file:#刚好是用的utf-8..
   mangshi_content=file.read()
   
#进行分词
result=jieba.analyse.textrank(mangshi_content,topK=20,withWeight=True)#太多会卡..日
print(result)#看一下有没有得到result,result 是一个list?
#for i in result:
   #print("%s  %f\n"%(i[0],i[1]))
   
word_fre=dict()#生成空字典
for i in result:
   word_fre[i[0]]=i[1]
   #print(type(i)),i是一个tuple,都在list里面

#del word_fre['没有']#删掉 没有
#word_fre['三体']=1.0

img=PIL.Image.open('chmap.png')
graph=numpy.array(img)#矢量化img

wc=wordcloud.WordCloud(font_path='C:\Windows\Fonts\simsun.ttc',
                       max_words=40,mask=graph,background_color='black')

wc.generate_from_frequencies(word_fre)
image_color=wordcloud.ImageColorGenerator(graph)

plot.imshow(wc)
plot.imshow(wc.recolor(color_func=image_color))
plot.axis("off")
#for i in range(54):
plot.show()


'''
with open('三体1.txt',encoding='ansi') as file:#刚好是用的utf-8..
   mangshi_content=file.read()
   
#进行分词
result=jieba.analyse.textrank(mangshi_content,topK=100,withWeight=True)#太多会卡..日
#print(result)#看一下有没有得到result,result 是一个list?
word_fre=dict()#生成空字典
for i in result:
   word_fre[i[0]]=i[1]
   #print(type(i)),i是一个tuple,都在list里面

del word_fre['没有']#删掉 没有
#word_fre['三体']=1.0

img=PIL.Image.open('coloredcloud.jpg')
graph=numpy.array(img)

wc=wordcloud.WordCloud(font_path='C:\Windows\Fonts\simfang.ttf',
                       max_words=100,mask=graph,background_color='white')

wc.generate_from_frequencies(word_fre)
image_color=wordcloud.ImageColorGenerator(graph)

plot.imshow(wc)
#plot.imshow(wc.recolor(color_func=image_color))
plot.axis("off")
plot.show()
'''
