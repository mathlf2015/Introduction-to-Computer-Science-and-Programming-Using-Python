1.生成随机数
          import random    #这个是注释，引入模块
          rnd = random.randint(1,500)#生成1-500之间的随机数
 
2.读文件
 
         f = open("c:\\1.txt","r")
         lines = f.readlines()#读取全部内容
         for line in lines
                 print line
3.写文件
        f = open("c:\\1.txt","r+")#可读可写模式
        f.write("123")#写入字符串
 
4.正则表达式，读取tomcat的日志并打印日期
 
     import re
     regx = "\d\d\d\d-\d\d-\d+"
     f = open("c:\stdout.log","r")
     i = 0
     for str in f.readlines():
        if re.search(regx,str):
             Response.write(str+"<br>")
              if i>10:break#由于是测试，只分析十行
              i=i+1
     f.close();
 
5.连接数据库
 
import pgdb
 
conn = pgdb.connect
 
(host='localhost',databse='qingfeng',user='qingfeng',password='123')
 
        cur = conn.cursor() 
 
        cur.execute("select * from dream") 
 
        print cur.rowcount
 
6.SAX处理xml:
 
      import string
      from xml.sax import saxlib, saxexts
 
      class QuotationHandler(saxlib.HandlerBase):
          """Crude sax extractor for quotations.dtd document"""
 
          def __init__(self):
                  self.in_quote = 0
                  self.thisquote = ''
 
          def startDocument(self):
              print '--- Begin Document ---'
 
          def startElement(self, name, attrs):
              if name == 'quotation':
                  print 'QUOTATION:'
                  self.in_quote = 1
              else:
                  self.thisquote = self.thisquote + '{'
 
          def endElement(self, name):
              if name == 'quotation':
                  print string.join(string.split(self.thisquote[:230]))+'...',
                  print '('+str(len(self.thisquote))+' bytes)\n'
                  self.thisquote = ''
                  self.in_quote = 0
              else:
                  self.thisquote = self.thisquote + '}'
 
          def characters(self, ch, start, length):
              if self.in_quote:
                  self.thisquote = self.thisquote + ch[start:start+length]
 
      if __name__ == '__main__':
          parser  = saxexts.XMLParserFactory.make_parser()
          handler = QuotationHandler()
          parser.setDocumentHandler(handler)
          parser.parseFile(open("sample.xml"))
          parser.close()
 
 
7.python的GUI模块标准的是Tkinter,也有QT和MFC的模块，有兴趣的大家自己搜索下
 
        import Tkinter
 
        root=Tkinter.Tk()
 
        my=Label(root,"Welcome to python's world")
 
        my.pack()
 
        root.mainloop()
