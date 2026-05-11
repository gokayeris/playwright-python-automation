# Playwright & Python - Full-Stack Automation Framework

This repository features a professional-grade automated testing architecture designed for scalability, maintainability, and high performance. It covers both User Interface (UI) and Web Service (API) validation.

## 🚀 Key Features
- **Page Object Model (POM):** Complete decoupling between application logic and test scripts for easier maintenance.
- **API Testing (REST):** Full coverage of HTTP methods (**GET, POST, PUT**) including schema validation and data persistence checks.
- **Evidence Management:** Automated, organized screenshots for rapid debugging and reporting.
- **Security:** Secure credential management using environment variables (`.env`).
- **Reporting:** Detailed, self-contained HTML reports for stakeholders.

## 📂 Project Structure
- `pages/`: Page Object classes encapsulating UI elements and actions.
- `tests/`: Test suites categorized by type (UI / API).
- `screenshots/`: Storage for visual evidence captured during test execution.
- `reporte_final.html`: A visual summary of the latest test execution.

## 🛠️ Installation & Usage

1. **Clone the repository.**
2. **Install dependencies:**
   ```bash
   pip install playwright pytest pytest-html python-dotenv
   playwright install