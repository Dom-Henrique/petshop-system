# 🐶 | PETSHOP - SYSTEM

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)
![HTML](https://img.shields.io/badge/HTML-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-D71F00?style=for-the-badge&logo=sqlalchemy&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white)

A web-based pet shop application built with **Flask**, **SQLAlchemy**, and **Flask-Login**.

What started as a basic terminal project in Python grew into a full e-commerce-style web app, with user authentication and a database behind it.

> 🚧 **Status:** prototype in active development. The UI design is still being built.

---

## 📖 About

I'm **Dom Henrique**, a back-end developer from Brazil. I recently started my Software Development journey, and this project began as a simple pet shop system that ran in the terminal when i was in CS degree in PUC-PB. I decided to take it further and turn it into something more sophisticated: a real web application using Python's best-known web tools.

## ✨ Features

- **Login:** the home page, with email and password authentication.
- **User registration:** collects first and last name, email, password, username, and user type.
- **Session management** with Flask-Login.
- **Database persistence** with SQLAlchemy.

> **Note:** the registration and user-type functionality will be reworked in future versions. It is kept as is for now to provide a complete user experience.

## 🛠️ Tech Stack

| Layer          | Technology                                              |
| -------------- | ------------------------------------------------------- |
| Language       | Python                                                  |
| Web framework  | [Flask](https://flask.palletsprojects.com/)             |
| ORM / database | [SQLAlchemy](https://www.sqlalchemy.org/)               |
| Authentication | [Flask-Login](https://flask-login.readthedocs.io/)      |

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or newer
- Git

### Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/Dom-Henrique/PetShop-System.git
   cd main
   ```

2. **Create and activate a virtual environment** (recommended)

   ```bash
   python -m venv venv

   # Linux / macOS
   source venv/bin/activate

   # Windows
   venv\Scripts\activate
   ```

3. **Install the dependencies**

   ```bash
   pip install flask
   pip install flask-login
   pip install flask-sqlalchemy
   pip install sqlalchemy
   ```

4. **Run the application**

   ```bash
   python __init__.py
   ```

5. **Open it in your browser** at `http://127.0.0.1:5152`

## 🗺️ Roadmap

- [X] Accessibility features for visually impaired users
- [ ] Facial recognition
- [X] Animations
- [ ] Final UI design *(in progress)*
- [ ] Rework of the registration / user-type flow

<!-- ## 🤝 Contributing

Suggestions and contributions are welcome! To contribute:

1. Fork the project
2. Create a branch for your feature (`git checkout -b feature/my-feature`)
3. Commit your changes (`git commit -m "Add my feature"`)
4. Push to the branch (`git push origin feature/my-feature`)
5. Open a Pull Request -->

## 💬 Feedback

Thank you for using this project for your studies! Feel free to open an [issue](https://github.com/Dom-Henrique/PetShop-System/issues) or reach out with your thoughts. Opinions are always welcome.

---

Made with 🐾 by **Dom Henrique**, Brazil