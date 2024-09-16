from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import IncludeLaunchDescription
from launch_ros.substitutions import FindPackageShare
from launch.substitutions import PathJoinSubstitution


def generate_launch_description():

    ld = LaunchDescription()

    this_package = FindPackageShare('aipr_2409_support')
    rviz_config_path = PathJoinSubstitution(
        [this_package, 'launch', 'sim.rviz'])
    ld.add_action(IncludeLaunchDescription(
        PathJoinSubstitution(
            [FindPackageShare('uclv_aipr_panda_sim'), 'launch', 'demo.launch.py']),
        launch_arguments={
            'rviz_config': rviz_config_path}.items()
    ))

    ld.add_action(Node(package = "tf2_ros", 
                       executable = "static_transform_publisher",
                       output = "screen",
                       arguments = "--x 1 --y 0 --z 0 --qx 0 --qy 0 --qz 0 --qw 1 --frame-id world --child-frame-id calibration".split(' ')))



    return ld