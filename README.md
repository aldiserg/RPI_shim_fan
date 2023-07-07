# Managing cooled fan via shin on RPI
![Connection](https://github.com/aldiserg/RPI_shim_fan/blob/main/connections.png?raw=true)

# Requirements
Hardware:
  1. RPI
  2. 5V Fan
  3. Transistor (for example IRF3205)
  4. Resistor 100 OM
  5. Resistor 10k OM

Software:
  1. Python3


# Setup
clone repository
```
git clone https://github.com/aldiserg/RPI_shim_fan.git
cd RPI_shim_fan
```

Change path to shim.py into shimFAN.service

Change connected pin into shim.py (variable name is dataPIN)

Create the service
```
sudo cp shimFAN.service /etc/systemd/system/shimFAN.service
sudo systemctl enable shimFAN --now
```

