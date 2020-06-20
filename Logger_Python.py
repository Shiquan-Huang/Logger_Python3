import logging
import os
import datetime
 
class loggerClass:
     #日志级别的字典
     level_relations = {"debug": logging.DEBUG, "info": logging.INFO, "warning": logging.WARNING,
                       "error": logging.ERROR, "critical": logging.CRITICAL,}
     #日志输出格式
     fmt_str="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
     logFile='log'   #定义日志存储的文件夹
 
     def __init__(self,level='info',fmt=fmt_str):
        if not os.path.exists(self.logFile):   #判断日志存储文件夹是否存在，不存在，则新建
              os.makedirs(self.logFile)
        formatter=logging.Formatter(fmt)  
        #生成以当天日期为名称的日志文件
        filename=self.logFile+'/'+datetime.datetime.today().strftime('%Y-%m-%d')+'.log'   
 
        #初始化日志类参数
        self.logger=logging.getLogger(__name__)
        self.logger.setLevel(self.level_relations.get(level))
 
        #定义日志输出到前面定义的filename中
        self.filelogger=logging.FileHandler(filename)
        #self.filelogger.setLevel(self.level_relations.get(level))
        #定义日志输出的格式
        self.filelogger.setFormatter(formatter)         
      
        
     def info(self,message,level="info"):
         '''
        #日志输出到控制台
        console=logging.StreamHandler()
        self.logger.addHandler(console)
        '''
         self.logger.addHandler(self.filelogger)
         if level == "debug" or level == "DEBUG":
             self.logger.debug(message)
         elif level == "info" or level == "INFO":
             self.logger.info(message)
         elif level == "warning" or level == "WARNING":
             self.logger.warning(message)
         elif level == "error" or level == "ERROR":
             self.logger.error(message)
         elif level == "critical" or level == "CRITICAL":
             self.logger.critical(message)
         else:
             raise ("日志级别错误")
         self.logger.removeHandler(self.filelogger)
 
 
 
logger=loggerClass('debug')   #设置日志对象接受的输出级别
logger.info('测试的日志输出INFO','INFO')
logger.info('测试的日志输出ERROR','ERROR')
logger.info('测试的日志输出WARNING','WARNING')
logger.info('测试的日志输出DEBUG','DEBUG')
 
logger1=loggerClass('warning')   #设置日志对象接受的输出级别
logger1.info('测试的日志输出INFO','INFO')
logger1.info('测试的日志输出ERROR','ERROR')
logger1.info('测试的日志输出WARNING','WARNING')
logger1.info('测试的日志输出DEBUG','DEBUG')