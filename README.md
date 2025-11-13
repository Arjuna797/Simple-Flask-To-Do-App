# Simple-Flask-To-Do-App
A lightweight, educational **To-Do web app** built using **Flask**, demonstrating basic CRUD functionality (Create, Read, Update, Delete) entirely in memory — with a clean **HTML, CSS, JavaScript** front-end and **Docker support** for easy deployment.
| Category                | Technology       | Version | Purpose                                                          |
| ----------------------- | ---------------- | ------- | ---------------------------------------------------------------- |
| **Frontend**            | HTML5            | —       | Structure of the To-Do interface                                 |
|                         | CSS3             | —       | Styling and visual layout                                        |
|                         | JavaScript (ES6) | —       | Handles task actions (Add, Complete, Delete)                     |
| **Backend**             | Flask            | 3.0.3   | Lightweight Python framework serving templates and API endpoints |
| **Language**            | Python           | 3.11    | Core programming language for backend logic                      |
| **Environment / Tools** | pip              | Latest  | Dependency management                                            |
|                         | virtualenv       | Latest  | Isolated environment setup                                       |
| **Containerization**    | Docker           | Latest  | Containerization of Flask application                            |
|                         | Docker Compose   | Latest  | Orchestrates app containers                                      |
| **Version Control**     | Git & GitHub     | —       | Source code management and collaboration                         |
| **Port Used**           | Flask App        | 9090    | Access app at `http://localhost:9090`                            |
# Simple-Flask-To-Do-App
A lightweight, educational **To-Do web app** built using **Flask**, demonstrating basic CRUD functionality (Create, Read, Update, Delete) entirely in memory — with a clean **HTML, CSS, JavaScript** front-end and **Docker support** for easy deployment.

## Prerequisites
- **Python 3.11**: Required for running the Flask application.
- **pip**: For installing Python packages.
- **virtualenv**: For creating isolated Python environments.
- **Docker and Docker Compose**: For containerized deployment (optional, but recommended for easy setup).
- **Ubuntu Virtual Machine**: Hosted on VirtualBox for migration.
- **File Transfer Tool**: Such as FileZilla or SCP for transferring project files from Windows to Ubuntu VM.

## Migration from Windows to Ubuntu VM
To migrate the project from a Windows environment to an Ubuntu virtual machine on VirtualBox:
1. Ensure your Ubuntu VM is set up and running.
2. Transfer the project files from your Windows machine to the Ubuntu VM using a file transfer tool (e.g., FileZilla or SCP).
3. Place the project files in a desired directory on the Ubuntu VM, e.g., `/home/ubuntu/Simple-Flask-To-Do-App-main`.

## Dependency Installation on Ubuntu
Follow these steps to install all necessary dependencies on your Ubuntu VM:

### System-Level Packages
Install required system packages:
```bash
sudo apt update
sudo apt install python3 python3-pip python3-venv
```

### Virtual Environment Setup
Create and activate a virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate
```

### Python Dependencies
Install Python packages from `requirements.txt`:
```bash
pip install -r requirements.txt
```

The `requirements.txt` file contains:
- Flask==3.0.3

No additional changes were made to `requirements.txt` or the code; the project is ready for migration without modifications.

## Project Execution on Windows
To run the project on Windows:
1. Ensure Python 3.11, pip, and virtualenv are installed.
2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the application:
   ```bash
   python app.py
   ```
5. Access the app at `http://localhost:9090`.

Alternatively, using Docker:
```bash
docker compose up -d
```

## Project Execution on Ubuntu
To run the project on Ubuntu VM:
1. Ensure dependencies are installed as per the "Dependency Installation on Ubuntu" section.
2. Activate the virtual environment:
   ```bash
   source venv/bin/activate
   ```
3. Run the application:
   ```bash
   python3 app.py
   ```
4. Access the app at `http://localhost:9090` (or the VM's IP if accessing from host).

Alternatively, using Docker:
```bash
docker-compose up -d
```

| Category                | Technology       | Version | Purpose                                                          |
| ----------------------- | ---------------- | ------- | ---------------------------------------------------------------- |
| **Frontend**            | HTML5            | —       | Structure of the To-Do interface                                 |
|                         | CSS3             | —       | Styling and visual layout                                        |
|                         | JavaScript (ES6) | —       | Handles task actions (Add, Complete, Delete)                     |
| **Backend**             | Flask            | 3.0.3   | Lightweight Python framework serving templates and API endpoints |
| **Language**            | Python           | 3.11    | Core programming language for backend logic                      |
| **Environment / Tools** | pip              | Latest  | Dependency management                                            |
|                         | virtualenv       | Latest  | Isolated environment setup                                       |
| **Containerization**    | Docker           | Latest  | Containerization of Flask application                            |
|                         | Docker Compose   | Latest  | Orchestrates app containers                                      |
| **Version Control**     | Git & GitHub     | —       | Source code management and collaboration                         |
| **Port Used**           | Flask App        | 9090    | Access app at `http://localhost:9090`                            |

```bash
# On Ubuntu / Linux
docker-compose up -d

# On Windows
docker compose up -d
