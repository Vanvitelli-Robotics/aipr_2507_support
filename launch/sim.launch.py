from launch import LaunchDescription
from launch_ros.actions import Node, PushRosNamespace
from launch.actions import IncludeLaunchDescription, GroupAction
from launch_ros.substitutions import FindPackageShare
from launch.substitutions import PathJoinSubstitution


def generate_launch_description():

    ld = LaunchDescription()

    this_package = FindPackageShare('aipr_2507_support')
    rviz_config_path = PathJoinSubstitution(
        [this_package, 'launch', 'sim.rviz'])
    
    ld.add_action(GroupAction(
        actions=[
            PushRosNamespace("panda"),
            IncludeLaunchDescription(
                PathJoinSubstitution(
                    [FindPackageShare('uclv_aipr_panda_sim'), 'launch', 'demo.launch.py']),
                launch_arguments={
                'rviz' : 'false'
                }.items()
        )]
        )
    )

    ld.add_action(GroupAction(
        actions=[
            PushRosNamespace("meca"),
            IncludeLaunchDescription(
                PathJoinSubstitution(
                    [FindPackageShare('uclv_aipr_meca500_sim'), 'launch', 'sim.launch.py']),
                launch_arguments={
                'rviz' : 'false'
                }.items()
        )]
        )
    )

    ld.add_action(Node(package = "tf2_ros", 
                       name= 'tf_meca500',
                       namespace="meca",
                       executable = "static_transform_publisher",
                       output = "screen",
                       arguments = "--x 1 --y 0 --z 0 --qx 0 --qy 0 --qz 1 --qw 0 --frame-id world --child-frame-id meca_base_link".split(' ')))


     ######## Run rviz ##############################################
    ld.add_action(Node(
        package='rviz2',
        executable='rviz2',
        output='screen',
        arguments=['-d', rviz_config_path],
    ))
    ###############################################################

    return ld