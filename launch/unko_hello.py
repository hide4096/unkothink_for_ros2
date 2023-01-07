# SPDX-FileCopyrightText: 2023 Aso Hidetoshi asouhide2002@gmail.com
# SPDX-License-Identifier: BSD-3-Clause

import launch
import launch.actions
import launch.substitutions
import launch_ros.actions

def generate_launch_description():

    sayhello = launch_ros.actions.Node(
            package='unkothink',
            executable='sayhello',
            )
    listen_unko = launch_ros.actions.Node(
            package='unkothink',
            executable='listen_unko',
            output='screen'
            )

    return launch.LaunchDescription([sayhello,listen_unko])
