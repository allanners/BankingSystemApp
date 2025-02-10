# Banking System App

## Description
This is a simplified **Banking System Application** built using **Python**, following the **Clean Architecture** principles.  
The application consists of three layers:
- **Domain Layer**: Defines core entities such as `Account` and `Customer`.
- **Use Case Layer**: Handles business logic, including creating accounts, making transactions, and generating account statements.
- **Infrastructure Layer**: Manages data persistence through a simple repository pattern.

## Features
- **Create a new account** with customer details.
- **Deposit and withdraw funds** from an account.
- **Generate account statements** to check transaction details.
- **Follow Clean Architecture** to ensure modularity and separation of concerns.

## Getting Started

### **Prerequisites**
Ensure you have **Python 3.7+** installed on your system.

### **Installation**
1. **Clone the repository:**
   ```bash
   git clone https://github.com/YOUR_GITHUB_USERNAME/banking-system.git
   ```
2. **Navigate to the project folder**
   ```bash
   cd BankingSystemApp
   ```
3. **Run the script:**
   ```bash
   python main.py
   ```

### Usage
- The program initializes an account repository.
- It creates a sample customer and an account.
- Deposits and withdrawals can be made using the MakeTransaction use case.
- Account statements can be generated for tracking balances.

## Project Structure
   ```
   BankingSystemApp/
    ├── main.py           # Main entry point of the application
    └── README.md         # Project documentation
   ```

## License
This project is licensed under the MIT License.