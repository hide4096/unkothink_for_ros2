# SPDX-FileCopyrightText: 2023 Aso Hidetoshi asouhide2002@gmail.com
# SPDX-License-Identifier: BSD-3-Clause

import rclpy
from rclpy.node import Node
from std_msgs.msg import String

def RptCr(length,chara):
    space = ''
    for i in range(length):
        space += chara
    return space

def showunko(whatthink,step=3):

  showthink = whatthink.splitlines()
  maxlen = max([len(i) for i in showthink])
  frame = ' ' + RptCr(maxlen + 2,'-') + ''

  print(frame)
  cnt = 0
  for i in showthink:
      space = ''
      for j in range(maxlen - len(i)):
          space += ' '

      l = r = '|'
      if len(showthink) > 1:
          if cnt == 0:
              l = '/'
              r = '\\'
          elif cnt == len(showthink)-1:
              l = '\\'
              r = '/'

      print(l + ' ' + i + space + ' ' + r)
      cnt += 1
  print(frame)

  print('  @')
  print('    @')

  for i in range(step):
      if i == 0:
          print(RptCr(step+1,' ') + '人')
      print(RptCr(step-i,' ') + '(' + RptCr((i+1)*2,'_') + ')')

class ListenUnko(Node):
  def __init__(self):
    super().__init__("oshiri")
    self.sub = self.create_subscription(String, "unkothink", self.dopoop, 10)
  
  def dopoop(self,msg):
    showunko(msg.data)

def main():
  rclpy.init()
  node = ListenUnko()
  rclpy.spin(node)

if __name__ == "__main__":
  main()
