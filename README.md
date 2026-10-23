
# 🎮 Tic Tac Toe — Flask Web Game

A colorful, interactive **two-player Tic Tac Toe game** built using Python and Flask, with a responsive frontend designed using HTML and CSS.

🔗 **Live Demo:** https://tic-tac-toe-game-aqpy.onrender.com

## 📌 About the Project

This project brings the classic Tic Tac Toe game to the web. Two players take turns placing **X** and **O** on a 3×3 board. The application automatically detects the winner or a draw and allows players to start a new game.

## ✨ Features

- 🎯 Two-player gameplay (X vs O)
- 🏆 Automatic winner detection
- 🤝 Draw detection
- 🔄 Play Again / reset functionality
- 🎨 Colorful gradient design
- 📱 Responsive user interface
- ⚡ Flask-powered backend
- ☁️ Deployed online using Render

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Game logic and backend |
| Flask | Web framework |
| HTML5 | Webpage structure |
| CSS3 | Styling and responsive design |
| Git & GitHub | Version control and source code |
| Render | Web application deployment |
| Gunicorn | Production WSGI server |

## 📂 Project Structure

```text
tic-tac-toe-flask/
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
├── templates/
│   └── index.html
└── static/
    └── style.css
```

## 🚀 Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/manasidesai23/tic-tac-toe-flask.git
```

### 2. Open the project folder

```bash
cd tic-tac-toe-flask
```

### 3. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 4. Start the application

```bash
python app.py
```

### 5. Open in your browser

Visit:

```text
http://127.0.0.1:5000
```

## 🎮 How to Play

1. Player X starts the game.
2. Players take turns selecting an empty cell.
3. The first player to align three symbols horizontally, vertically, or diagonally wins.
4. If all nine cells are filled without a winner, the game ends in a draw.
5. Click **Play Again** to start a new match.

## ☁️ Deployment

The application is deployed using **Render**.

- Build command: `pip install -r requirements.txt`
- Start command: `gunicorn app:app`

## 🔮 Future Improvements

- Add single-player mode against an AI opponent.
- Track scores across multiple rounds.
- Add sound effects and animations.
- Store match history and statistics.
- Introduce different themes and difficulty levels.

## 👨‍💻 Author

**Atharv Anagal**

Developed as a Python Flask web development project.

---

⭐ If you enjoy this project, consider giving the repository a star!
