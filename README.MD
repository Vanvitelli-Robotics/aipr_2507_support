# ROS2 simulator for the test 07/2025

[![N|Solid](https://www.unicampania.it/doc/img/logo_vanvitelli.jpg)](https://www.ingegneria.unicampania.it/roboticslab)

## Install

- Install this package and the simulators, finally install the dependencies.
In the src folder of the ROS workspace
```bash
git clone https://github.com/Vanvitelli-Robotics/uclv_aipr_panda_sim.git # PANDA Simulator
git clone https://github.com/Vanvitelli-Robotics/uclv_aipr_meca500_sim.git # MECA Simulator
git clone https://github.com/Vanvitelli-Robotics/aipr_2507_support.git
sudo apt update && rosdep install -r --from-paths . --ignore-src --rosdistro $ROS_DISTRO -y
```

## Start the simulation

RUn the simulator:
```bash
ros2 launch aipr_2507_support sim.launch.py
```

## License

GNU General Public License v3.0