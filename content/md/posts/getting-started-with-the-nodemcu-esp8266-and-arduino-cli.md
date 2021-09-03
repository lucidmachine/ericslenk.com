{:title "Getting Started with the NodeMcu, ESP8266, and arduino-cli", :date "2021-02-15", :tags ["nodemcu" "esp8266" "cli" "arduino" "wifi"], :description "Install and configure software to use the NodeMcu ESP8266 dev board with arduino-cli."}

The [NodeMcu](https://www.nodemcu.com/index_en.html) is an open-source development kit for the
[ESP8266 WiFi chip series](http://esp8266.net/) which is compatible with Arduino software.

# Install Drivers
In order to communicate with the microcontroller you'll need serial drivers. If you're running a
Linux kernel 3 or up then they're already installed, just make sure your computer doesn't need a
reboot since your last kernel update OR SOMETHING. Otherwise download and install [Silicon Labs'
CP210x
USB to UART Bridge VCP Drivers](https://www.silabs.com/developers/usb-to-uart-bridge-vcp-drivers).

# Install arduino-cli
[arduino-cli](https://github.com/arduino/arduino-cli) is a command line utility to manage boards and
libraries and compile and flash code like the full-fledged Arduino IDE, but with your own favorite
tools. Install it via your package manager where available, otherwise see [the arduino-cli
installation page](https://arduino.github.io/arduino-cli/latest/installation/).

```bash
$ sudo pamac install arduino-cli
```

# Add the ESP8266 Repository to arduino-cli
`arduino-cli` doesn't maintain ESP8266 board packages in its default repository, but we can easily
add a repository which does. Use the `config init` subcommand to generate a configuration file.

```bash
$ arduino-cli config init
Config file written: /home/lucidmachine/.arduino15/arduino-cli.yaml
```

Once the configuration file has been created, edit it to add an entry in the `additional_urls` list
under `board_manager`.

```yaml
# /home/lucidmachine/.arduino15/arduino-cli.yaml
board_manager:
  additional_urls:
    - http://arduino.esp8266.com/stable/package_esp8266com_index.json
```

Now update the index of cores. You should see that the ESP8266 index has been downloaded.

```bash
$ arduino-cli core update-index
Updating index: package_index.json downloaded
Updating index: package_index.json.sig downloaded
Updating index: package_esp8266com_index.json downloaded
```

# Install ESP8266 Cores
Now that you can find them, install the ESP8266 cores.

```bash
$ arduino-cli core install esp8266:esp8266
Downloading packages...
esp8266:xtensa-lx106-elf-gcc@2.5.0-4-b40a506 already downloaded
esp8266:mkspiffs@2.5.0-4-b40a506 already downloaded
esp8266:mklittlefs@2.5.0-4-fe5bb56 already downloaded
esp8266:python3@3.7.2-post1 already downloaded
esp8266:esp8266@2.7.4 already downloaded
Installing esp8266:xtensa-lx106-elf-gcc@2.5.0-4-b40a506...
esp8266:xtensa-lx106-elf-gcc@2.5.0-4-b40a506 installed
Installing esp8266:mkspiffs@2.5.0-4-b40a506...
esp8266:mkspiffs@2.5.0-4-b40a506 installed
Installing esp8266:mklittlefs@2.5.0-4-fe5bb56...
esp8266:mklittlefs@2.5.0-4-fe5bb56 installed
Installing esp8266:python3@3.7.2-post1...
esp8266:python3@3.7.2-post1 installed
Installing esp8266:esp8266@2.7.4...
Configuring platform...
esp8266:esp8266@2.7.4 installed
```

# Create a Test Project
Now create a new sketch with the `sketch` subcommand.

```bash
$ arduino-cli sketch new blink
Sketch created in: /home/lucidmachine/src/blink
```

And edit the generated file to contain some basic blink code, courtesy of [the arduino-cli Getting
Started guide](https://arduino.github.io/arduino-cli/latest/getting-started/#create-a-new-sketch).

```c
// /home/lucidmachine/src/blink/blink.ino

void setup() {
    pinMode(LED_BUILTIN, OUTPUT);
}

void loop() {
    digitalWrite(LED_BUILTIN, HIGH);
    delay(1000);
    digitalWrite(LED_BUILTIN, LOW);
    delay(1000);
}
```

# Compile and Upload the Test Sketch
To upload code to the board you'll need to first identify the board's Fully Qualified Board Name
(FQBN) and the port to which it is attached. Plug your board in to your computer and run the `board
list` subcommand.

```bash
$ arduino-cli board list
Port         Type              Board Name FQBN Core
/dev/ttyS0   Serial Port       Unknown
/dev/ttyUSB0 Serial Port (USB) Unknown
```

My board is attached to `/dev/ttyUSB0`.

If your board happens to be identified as "Unknown", then you'll need to pick the appropriate FQBN
from the list of all boards. In my case I happen to know I've bought the NodeMcu with the ESP-12E
Module, so I filter my search for 'nodemcu'.

```bash
$ arduino-cli board listall | grep -i 'nodemcu'
NodeMCU 0.9 (ESP-12 Module)     esp8266:esp8266:nodemcu
NodeMCU 1.0 (ESP-12E Module)    esp8266:esp8266:nodemcu2
```

`esp8266:esp8266:nodemcu2` is my board's FQBN.

Now you can compile the sketch given your board's FQBN using the `compile` subcommand.

```bash
$ arduino-cli compile --fqbn esp8266:esp8266:nodemcuv2 blink
Executable segment sizes:
IROM   : 228624          - code in flash         (default or ICACHE_FLASH_ATTR)
IRAM   : 26752   / 32768 - code in IRAM          (ICACHE_RAM_ATTR, ISRs...)
DATA   : 1248  )         - initialized variables (global, static) in RAM/HEAP
RODATA : 688   ) / 81920 - constants             (global, static) in RAM/HEAP
BSS    : 24880 )         - zeroed variables      (global, static) in RAM/HEAP
Sketch uses 257312 bytes (24%) of program storage space. Maximum is 1044464 bytes.
Global variables use 26816 bytes (32%) of dynamic memory, leaving 55104 bytes for local variables.
Maximum is 81920 bytes.
```

If it compiled, then you can upload the sketch with the `upload` subcommand given the board's FQBN
and port.

```bash
$ arduino-cli upload --port /dev/ttyUSB0 --fqbn esp8266:esp8266:nodemcuv2 blink
esptool.py v2.8
Serial port /dev/ttyUSB0
Connecting....
Chip is ESP8266EX
Features: WiFi
Crystal is 26MHz
MAC: f4:cf:a2:f7:5f:1e
Uploading stub...
Running stub...
Stub running...
Configuring flash size...
Auto-detected Flash size: 4MB
Compressed 261472 bytes to 193129...
Wrote 261472 bytes (193129 compressed) at 0x00000000 in 17.0 seconds (effective 122.9 kbit/s)...
Hash of data verified.

Leaving...
Hard resetting via RTS pin...
```

DONE.