import time
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import TwistStamped

rclpy.init()
node = Node('twist_pub')
pub = node.create_publisher(TwistStamped, '/servo_node/delta_twist_cmds', 10)

msg = TwistStamped()
msg.header.frame_id = 'panda_hand'
msg.twist.linear.x = 0.0
msg.twist.linear.y = 0.0
msg.twist.linear.z = 0.0
msg.twist.angular.x = 0.0
msg.twist.angular.y = 0.1
msg.twist.angular.z = 0.0


dt = 1.0 / 50.0
try:
    while rclpy.ok():
        msg.header.stamp = node.get_clock().now().to_msg()
        pub.publish(msg)
        rclpy.spin_once(node, timeout_sec=0.0)
        time.sleep(dt)
finally:
    node.destroy_node()
    rclpy.shutdown()
    
# import rclpy
# from rclpy.node import Node
# from rclpy.parameter import Parameter
# from geometry_msgs.msg import TwistStamped

# rclpy.init()
# node = Node("twist_pub")
# node.set_parameters([Parameter("use_sim_time", Parameter.Type.BOOL, True)])

# pub = node.create_publisher(TwistStamped, "/servo_node/delta_twist_cmds", 10)

# msg = TwistStamped()
# # msg.header.frame_id = "panda_link0"
# msg.header.frame_id = "panda_hand"
# msg.twist.linear.x = 0.0
# msg.twist.linear.y = 0.0
# msg.twist.linear.z = -1.0
# msg.twist.angular.x = 0.0
# msg.twist.angular.y = 0.0
# msg.twist.angular.z = 0.0

# def tick():
#     msg.header.stamp = node.get_clock().now().to_msg()
#     pub.publish(msg)

# rate = 50.0  # [Hz]
# node.create_timer(1.0 / rate, tick)  # 50 Hz
# rclpy.spin(node)
