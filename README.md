# CobaltTravelingRobotChallenge

## Setup (Ubuntu)
1. Install Docker
2. Clone this repository
3. Modify DISPLAY Environment variable in Dockerfile to match your machine's IP and desired display number
4. In the base folder, enter the following to build and run:
```bash
docker build -t cobalt-latest . && 
docker run -v $pwd:/home/will/CobaltChallenge/ --name cobalt-challenge cobalt-latest python3 Cobalt_traveling_robot_challenge.py
```
