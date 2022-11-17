
# Iot Ventilation System
Iot Ventilation System is an Iot based solution for maintaing temperature and humidity in the preferred environment.
The system uses Azure Iot Hub for its cloud related operations.
For testing purpose, the project has been deployed in a Raspberry Pi 3.

## Authors

- [@Vishwanath](https://www.github.com/vishwanath-29)
- [@Roshan](https://www.github.com/Roshan-jose-a-j)
- [@Vishal](https://www.github.com/gkvishal7)



## Installation

To install this project clone the repository

```bash
  git clone https://github.com/vishwanath-29/IoT-Ventilation-System
  cd IoT-Ventilation-System
```
Copy the Easpberry pi files into the raspberry pi computer

Go into the Client end
```bash
  cd Client_End
```
Before Starting the Application set the environment variables for connection_string and consumer_group. 
```bash
set IotHubConnectionString=YourIoTHubConnectionString
set EventHubConsumerGroup=YourConsumerGroupName
```
To Start the Application 
```bash
  npm i;
  npm start;
```
If you do not have a raspberry pi and want to test it, run the azure_iot_send_emulate python script.
 Paste the connection string in the CONNECTION_STRING variable in the script
```bash
    python3 azure_iot_send_emulate.py
```


