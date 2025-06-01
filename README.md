# 💸 **Financial Controll** 🏦

An interactive program to manage personal finances, including expenses, income, balance control, statements, and record deletion. Ideal for those who want to organize their budget in a simple and efficient way.

---

## 🚀 **Project Overview**

The program implements essential functionalities for financial management:

* **Add Expenses and Income:** Categorized by type (essential, non-essential, fixed, or variable).
* **View Expenses and Income:** Visual summaries of financial records.
* **Delete Records:** Allows removal of expenses or income, automatically adjusting the balance.
* **View Statement:** Complete display of all transactions with updated balance.
* **Credit Management:** Option to add credit to the main balance.

---

## 🛠️ **Key Features**

### Functionalities:

* **Add Expense:** Differentiation between essential expenses (e.g., rent, healthcare) and non-essential expenses (e.g., entertainment).
* **Add Income:** Records categorized as either fixed income or variable income.
* **Summary of Expenses and Income:** Detailed display of all expenses and income.
* **Delete Expenses/Income:** Removes transactions and automatically adjusts the balance.
* **Complete Statement:** Shows all transactions performed and their impact on the balance.
* **Credit Management:** Adjusts the balance based on a credit limit set at the beginning.

---

## ⚙️ **Setup**

### Prerequisites

* Python 3.x must be installed on your system.

---

## ▶️ **How to Run**

1. Clone this repository to your local environment:

```bash
git clone https://github.com/jp9141joao/financial-controll.git
```

2. Install any necessary dependencies if required (there are no external dependencies for this code).

3. Run the code in the terminal with:

```bash
python your_file.py
```

---

## 🎮 **How It Works**

### Main Menu:

After starting, the user will see the following menu:

```
Menu:
1 - Add expenses
2 - Add income
3 - Show expenses
4 - Show income
5 - Show statement
6 - Exit
```

### Options:

1. **Add Expenses:**
   Includes essential or non-essential expenses with automatic balance adjustment.

2. **Add Income:**
   Includes income such as salary or investments, with the option to classify as fixed or variable.

3. **Show Expenses:**
   Displays a list of all categorized expenses.

4. **Show Income:**
   Displays a list of all categorized income.

5. **Show Statement:**
   Displays all transactions (expenses and income) with the updated balance.

6. **Exit:**
   Closes the program.

---

## 💬 **Technologies Used**

* **Python 3.x**: Core program logic.
* Data handling with simple lists.
* Screen clearing with `os.system('cls')` for a user-friendly console experience.

---

## 📊 **Example Usage**

After starting the program, you will see interactive options in the console:

```
Enter your account balance: $1000
Does your account have credit?
1- Yes
2- No
R: 1
Enter your account credit limit: $500
Balance + credit configured.
```

Main menu with options:

```
Menu:
1 - Add expenses
2 - Add income
3 - Show expenses
4 - Show income
5 - Show statement
6 - Exit
```

---

Now you can organize your finances easily with this manager! 💡✨
