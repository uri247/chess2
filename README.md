# Chess 2

Chess 2 is a multi-player real time strategy game based on the classic game of Chess.

## Installing

### Installing on macOS and Windows

Download the app from the [releases page](https://github.com/yairchu/chess2/releases)

### Other platforms

* Install Python (version 3.3 or above)
* In your terminal:
* `pip install pygame`
* `pip install pystun3`
* To run the game type `python main.py` from the game's folder

## Playing

Chess 2 is played vs friends over the network.

* Both players need to open the game
* At the top of each player an address such as "BASK DAWN ALAN" will appear
* Such an address can be sent over to the other player via any chat platform
* The other player should type the address to connect

## Internals

### Networking setup

* During the game its communication is direct peer to peer over UDP (for minimum latency a la RTS games like Starcraft)
* To establish a UDP connection the peers first need to find their external ip address and port, which they do using a STUN service
* To connect without each typing the other's address, they connect to the [matching server](https://github.com/yairchu/game-match-server) over HTTP which assigns each player a three word identifier
* When the identifier is entered the game asks the server for the address it represents
* The host also polls the server until a connection is established, and the server tells it the ip address and port of the other player
* Then both players send UDP packets to each other and in such scenario Routers/NAT allow the communication to happen

## Building

### Building a macOS app

    python setup.py py2app
    # Remove unneeded resources to save some space
    rm dist/Chess\ 2.app/Contents/Frameworks/lib*.dylib
    rm -rf dist/Chess\ 2.app/Contents/Resources/lib/{tcl,tk}*
    rm -r dist/Chess\ 2.app/Contents/Resources/lib/python3.8/pygame/{docs,examples,tests}

(this worked for me on macOS 10.14.6 with Python 3.8.2 and pygame 2.0.0.dev6)

### Building a Windows exe

    pip install pyinstaller
    pyinstaller -F main.y
    copy chess.png dist

