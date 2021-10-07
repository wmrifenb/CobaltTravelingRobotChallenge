# CobaltTravelingRobotChallenge
[Will Rifenburgh](mailto:wmrifenburgh@gmail.com)

## Setup (Ubuntu)
1. Install Docker
2. Clone this repository
3. In terminal, in the base folder, enter the following to build and run:
```bash
docker build -t cobalt-latest . && 
docker run -ti --rm -e DISPLAY=$DISPLAY -v "$(pwd)":/home/will/CobaltChallenge/ -v /tmp/.X11-unix:/tmp/.X11-unix -h $HOSTNAME -v $HOME/.Xauthority:/home/will/.Xauthority --name cobalt-challenge cobalt-latest python3 Cobalt_traveling_robot_challenge.py
```
