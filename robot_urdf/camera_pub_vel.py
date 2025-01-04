'''
- this script is used to publish the velocity command to the joint controller
- the velocity command is published to the topic '/joint_01_controller/commands'
- the velocity command is published as a Float64MultiArray message
- the velocity command is published as a single element array
'''
import rclpy
from rclpy.node import Node
from std_msgs.msg import Float64MultiArray

class CmdJointPublisher(Node):
    def __init__(self):
        super().__init__('joint_vel_publisher')
        self.publisher_ = self.create_publisher(Float64MultiArray, '/joint_01_controller/commands', 1)

    def send_cmd(self, velocity):
        msg = Float64MultiArray()
        msg.layout.dim = []
        msg.layout.data_offset = 0
        msg.data = [velocity]
        self.publisher_.publish(msg)

def main():
    rclpy.init()
    node = CmdJointPublisher()
    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()