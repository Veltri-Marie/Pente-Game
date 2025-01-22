
# Pente - A Real-Time Multiplayer Board Game

Pente is a strategic two-player board game where the goal is to align five stones in a row. This project features real-time multiplayer gameplay,
 where players can challenge each other over a network connection. The game consists of a **C** server and a **Python** client built with **Pygame** for the graphical interface.

## Tech Stack

- **Server**: C, SQLite  
- **Client**: Python, Pygame  
- **Virtualization**: VirtualBox (Linux VM - recommended: Debian)  
- **Database**: SQLite for storing player data and game states  
- **Real-Time Communication**: Sockets and binary protocol for client-server communication  

## Features

- **Real-Time Multiplayer**: Play against friends or other players over the network.
- **Intuitive User Interface**: A user-friendly interface built with Pygame, featuring a dynamic game board with clickable intersections.
- **Game Lobby**: View and join ongoing games or create new ones.
- **Security**: Enhanced security measures for user authentication and game integrity.
- **SQLite Database**: Stores player data and game history.


### Multiplayer Gameplay

- Players can join existing games or create new ones.
- The game progresses in real-time, with players placing their pieces on the board and trying to form a line of five stones to win.
- The server handles all the game logic and synchronization between clients.

## Commands

- **Client**:
  - Players can click on the board to place their pieces.
  - The UI updates in real-time to show the moves of the opponent.
  - The game ends when one player wins or when the board is full.


## Structure of the Code

- **`server.c`**: Contains the server logic. It handles player connections, manages game state, and updates the database.
- **`client.py`**: Handles the user interface using Pygame, as well as the communication with the server.


