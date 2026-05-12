# Playwright & Python - Full-Stack Automation Framework 🚀

![Playwright Tests](https://github.com/gokayeris/playwright-python-automation/actions/workflows/playwright.yml/badge.svg)

This repository features a professional-grade automated testing architecture designed for scalability, maintainability, and high performance. It covers both User Interface (UI) and Web Service (API) validation.

## 🚀 Key Features
- **Page Object Model (POM):** Complete decoupling between application logic and test scripts for easier maintenance.
- **API Testing (REST):** Full coverage of HTTP methods (**GET, POST, PUT, DELETE**) including schema validation and data persistence checks.
- **Evidence Management:** Automated, organized screenshots for rapid debugging and reporting.
- **CI/CD Pipeline:** Fully integrated with GitHub Actions (Node.js 24 / Python 3.11) for automated execution on every push.
- **Security:** Secure credential management using environment variables (`.env`) and GitHub Secrets.
- **Reporting:** Detailed, self-contained HTML reports generated automatically after each run.

## 📂 Project Structure
- `.github/workflows/`: Continuous Integration (CI/CD) pipeline configuration.
- `pages/`: Page Object classes encapsulating UI elements and actions.
- `tests/`: Test suites categorized by type (UI / API).
- `screenshots/`: Visual evidence captured during test execution.
- `requirements.txt`: List of project dependencies.

## 🛠️ Installation & Local Usage

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/gokayeris/playwright-python-automation.git](https://github.com/gokayeris/playwright-python-automation.git)
   cd playwright-python-automation
   ```
2. **Install dependencies:**
   ```bash
   pip install playwright pytest pytest-html python-dotenv
   playwright install
   ```
3. **Configure Environment Variables:**
   Create a .env file in the root directory with your credentials:
   ```Plaintext
   SAUCE_USER=your_user
   SAUCE_PASSWORD=your_password
   ```
4. **Run Tests:**
   Create a .env file in the root directory with your credentials:
   ```Bash
   # Run all tests with HTML report
   pytest --html=report.html --self-contained-html
   ```

## 📈 Continuous Integration (CI/CD)
The framework is powered by GitHub Actions. Upon every push to the main branch, the pipeline:

1. Provisions a clean Ubuntu environment.

2. Installs Python 3.11 and necessary browser binaries.

3. Executes the full test suite.

4. Generates and uploads the final HTML report as a downloadable Build Artifact.

Developed by Gokay Eris - QA Automation Engineer.

### 💡 Final Tips for your Repository:
* **Secrets:** I see you've already started adding `SAUCE_USER` in your GitHub settings. Make sure `SAUCE_PASSWORD` is also there so the "9 passed" result we saw in your reports remains consistent.
* **Node.js Warning:** By using the `FORCE_JAVASCRIPT_ACTIONS_TO_NODE24: true` environment variable we discussed, that yellow warning about Node.js 20 will disappear from your **Actions** summary.
* **Artifacts:** After the next run, you'll be able to find the `playwright-report` directly in the **Summary** page of your GitHub Action, just like it appears in your local browser.