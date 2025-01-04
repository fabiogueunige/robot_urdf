'''
This script is used to publish velocity commands to the robot.
The velocity commands are published to the topic 'cmd_vel' in the form of Twist messages.
'''
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

class CmdPublisher(Node):
    def __init__(self):
        super().__init__('vel_publisher')
        self.publisher_ = self.create_publisher(Twist, 'cmd_vel', 1)

    def send_cmd(self, linear, angular):
        msg = Twist()
        msg.linear.x = linear
        msg.angular.z = angular
        self.publisher_.publish(msg)

def main():
    rclpy.init()
    node = CmdPublisher()
    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()