# Deployment Guide

Since your application uses **Python (Flask)** for the backend and **HTML/JS** for the frontend (served by Flask), you need a host that supports Python.

Here are the two best **FREE** options for beginners:

---

## Option 1: Render (Recommended for Portfolios)
**Render** is modern, connects directly to GitHub, and gives you a free `.onrender.com` URL.

### 1. Prepare your Code
Create a file named `Procfile` (no extension) in your `backend` folder with this single line:
```
web: gunicorn app:app
```
*Note: You may need to add `gunicorn` to your `requirements.txt`.*

### 2. Push to GitHub
1.  Initialize a Git repo in your project folder.
2.  Push your code to a public GitHub repository.

### 3. Deploy on Render
1.  Go to [dashboard.render.com](https://dashboard.render.com/) and Sign Up (use GitHub).
2.  Click **New +** -> **Web Service**.
3.  Connect your GitHub repository.
4.  **Settings**:
    - **Name**: `blackjack-web` (or unique name)
    - **Root Directory**: `backend` (Important! Your app.py is here)
    - **Runtime**: Python 3
    - **Build Command**: `pip install -r requirements.txt`
    - **Start Command**: `gunicorn app:app`
5.  Click **Create Web Service**.
6.  Wait ~2 minutes. Your app will be live!

---

## Option 2: PythonAnywhere (Easiest for Students)
**PythonAnywhere** allows you to upload files directly without Git if you prefer.

### Steps
1.  Sign up at [pythonanywhere.com](https://www.pythonanywhere.com/).
2.  Go to **Files** tab -> Upload your `blackjack-web` folder.
3.  Go to **Web** tab -> **Add a new web app**.
4.  Select **Flask** -> **Python 3.10** (or similar).
5.  **Configuration**:
    - **Source code**: Enter path to your `backend` folder (e.g., `/home/username/blackjack-web/backend`).
    - **Working directory**: Enter path to your `backend` folder.
    - **WSGI configuration file**: Edit this file to import your app:
      ```python
      import sys
      path = '/home/yourusername/blackjack-web/backend'
      if path not in sys.path:
          sys.path.append(path)
      from app import app as application
      ```
6.  Go to **Consoles** -> **Bash** and run:
    ```bash
    pip install flask flask-cors
    ```
7.  Go back to **Web** tab and click **Reload**.
8.  Your app is live at `yourusername.pythonanywhere.com`.
