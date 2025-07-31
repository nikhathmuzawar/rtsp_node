import rclpy
from rclpy.node import Node
from std_msgs.msg import String  

class RTSPDummyPublisher(Node):
    def __init__(self):
        super().__init__('rtsp_dummy_publisher')
        self.publisher_ = self.create_publisher(String, '/video/rtsp', 10)
        self.timer = self.create_timer(1.0, self.publish_fake_msg)

    def publish_fake_msg(self):
        msg = String()
        msg.data = "Streaming RTSP video via WebRTC"
        self.publisher_.publish(msg)
        self.get_logger().info('Publishing fake RTSP metadata')

def main(args=None):
    rclpy.init(args=args)
    node = RTSPDummyPublisher()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
