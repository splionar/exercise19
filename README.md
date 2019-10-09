# Instructions to reproduce results

### 1. Clone this repository and go to its directory
```bash
git clone https://github.com/splionar/exercise19.git
cd exercise19
```
### 2. Build docker image
```bash
dts devel build -f --arch amd64 
```

### 3. Run docker image with the following options
```bash
docker run -it --rm --net host -v [PATH_TO_BAG_FOLDER]:/code/catkin_ws/src/exercise19/bag duckietown/exercise19:v1-amd64 /bin/bash
```

### 4. After going inside the docker shell, run the python script using the command below
```bash
python packages/analyze_bag.py bag/[BAG_FILE_NAME]
```
