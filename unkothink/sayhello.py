# SPDX-FileCopyrightText: 2023 Aso Hidetoshi asouhide2002@gmail.com
# SPDX-License-Identifier: BSD-3-Clause

import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class Talker():
  def __init__(self,node):
    self.pub = node.create_publisher(String,"unkothink",10)
    node.create_timer(1,self.cb)


  def cb(self):
    msg = String()
    msg.data = 'Hello!'
    self.pub.publish(msg)

def main():
  rclpy.init()
  node = Node("sayhello")
  talker = Talker(node)
  rclpy.spin(node)

if __name__ == '__main__':
  main()
  


