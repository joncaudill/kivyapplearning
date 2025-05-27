# Language Learner

A simple Kivy-based language learning game where you match Spanish words to images. 
Built with Python and Kivy.

## Purpose

This was written to get a feel for the basics of building an application using 
Kivy.

## Features

- Randomized image-word matching questions
- Score and high score tracking
- Progress bar with timer
- End game popup with results
- Play again functionality

## Getting Started

### Prerequisites

- Python 3.7+
- [Kivy](https://kivy.org/#download) (install via pip)

### Installation

1. Clone the repository:

    ```sh
    git clone https://github.com/joncaudill/language-learner.git
    cd language-learner
    ```

2. (Optional) Create and activate a virtual environment:

    ```sh
    python -m venv kivy_venv
    # On Windows:
    kivy_venv\Scripts\activate
    # On Unix or MacOS:
    source kivy_venv/bin/activate
    ```

3. Install dependencies:

    ```sh
    pip install kivy
    ```

### Running the Game

```sh
python main.py
```

## Project Structure

```
.
├── main.py
├── languagelearner.kv
├── images/
│   ├── bote.png
│   ├── diamante.png
│   ├── espada.png
│   ├── hacha.png
│   ├── ladrillos.png
│   ├── manzana.png
│   ├── pala.png
│   ├── pasto.png
│   ├── roca.png
│   ├── tierra.png
│   ├── trophy.png
│   └── white.png
└── ...
```

## How to Play

1. The game displays a Spanish word and four images.
2. Click the image that matches the word.
3. Your score increases for each correct answer.
4. The game ends when the timer runs out. Try to beat your high score!

## License

This project was just written for educational purposes