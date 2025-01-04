'''
this script publishes an image to the topic /camera/img
'''
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image

class ImagePublisher(Node):
    def __init__(self):
        super().__init__('image_publisher')
        self.publisher_ = self.create_publisher(Image, '/camera/img', 10)

    def publish_image(self, img):
        msg = Image()
        msg = img
        self.publisher_.publish(msg)

def main():
    rclpy.init()
    node = ImagePublisher()
    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

