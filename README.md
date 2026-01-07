# Moveit Servo

See the [Realtime Arm Servoing Tutorial](https://moveit.picknik.ai/main/doc/realtime_servo/realtime_servo_tutorial.html) for installation instructions, quick-start guide, an overview about `moveit_servo`, and to learn how to set it up on your robot.

### Build pkg
```bash
colcon build --symlink-install --packages-select moveit_servo && . install/setup.bash
```

### Run demos
```bash
ros2 launch moveit_servo servo_example.launch.py
ros2 launch moveit_servo pose_tracking_example.launch.py
```

### Publish twist command
```bash
cd <path_to_ws>/src/moveit_servo/launch && python3 pub_twist.py
```