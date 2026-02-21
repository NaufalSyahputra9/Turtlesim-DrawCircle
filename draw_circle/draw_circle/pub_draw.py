import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist


class TurtleCircle(Node):

    def __init__(self):
        super().__init__('turtle_circle')
        self.publisher_ = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)

        timer_period = 0.5  
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.i = 0
        self.declare_parameter('radius', 2.0)


    def timer_callback(self):
        vel = Twist()
        self._radius = float(self.get_parameter('radius').value)
        vel.linear.x = self._radius
        vel.angular.z = 1.0
            
        self.get_logger().info('Publishing #%d, Radius = "%f"' % (self.i, self._radius))
        self.publisher_.publish(vel)
        self.i += 1


def main(args=None):
    rclpy.init(args=args)

    minimal_publisher = TurtleCircle()

    rclpy.spin(minimal_publisher)

    minimal_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()

#ros2 param set /turtle_circle radius 5.0