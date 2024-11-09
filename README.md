# Midterm_IS218
# Calculator Application

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Architecture](#architecture)
  - [Design Patterns](#design-patterns)
  - [Logging Strategy](#logging-strategy)
- [Setup Instructions](#setup-instructions)
- [Usage](#usage)
  - [Available Commands](#available-commands)
  - [Examples](#examples)
- [Testing](#testing)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Introduction

Welcome to the **Calculator Application**! This is a robust, command-line based calculator designed to perform basic arithmetic operations, manage operation history, and support undo functionality. Built with Python, this application leverages design patterns to ensure maintainability and scalability.

## Features

- **Arithmetic Operations**: Perform addition, subtraction, multiplication, division, power, and modulus operations.
- **History Management**: Keep a record of all executed operations with the ability to view, undo, and clear history.
- **Undo Functionality**: Revert the last executed operation.
- **Persistent Storage**: Operation history is saved to a CSV file (`history.csv`) for persistence across sessions.
- **Comprehensive Logging**: Detailed logs are maintained for monitoring and debugging purposes.
- **Extensible Architecture**: Designed using design patterns to facilitate easy addition of new features.

## Architecture

The Calculator Application is structured into modular components, each responsible for specific functionalities. This separation of concerns enhances the application's maintainability, scalability, and testability.

### Design Patterns

#### Command Pattern

The application employs the **Command Pattern** to encapsulate all information needed to perform an action or trigger an event. This pattern is instrumental in implementing features like undo operations and history tracking.

- **Classes Involved**:
  - `OperationCommand`: Represents a single operation performed by the user.
  - `HistoryManager`: Maintains a list of `OperationCommand` instances, allowing operations to be recorded and undone.
  - `CommandProcessor`: Processes user inputs, executes operations using the `Calculator`, and interacts with `HistoryManager`.

**Impact**:
- **Extensibility**: Easily add new operations without altering existing codebase.
- **Maintainability**: Clear separation between command execution and command management.
- **Undo Capability**: Simplifies implementing undo operations by maintaining a history of executed commands.

### Logging Strategy

A comprehensive logging strategy is implemented to facilitate monitoring and debugging.

- **Implementation**:
  - Utilizes Python's built-in `logging` module.
  - Configured to log messages to both the console and a file (`app.log`).
  - Different log levels (`DEBUG`, `INFO`, `WARNING`, `ERROR`, `CRITICAL`) are used to capture varying degrees of information.

- **Logged Events**:
  - Initialization of core components (`Calculator`, `HistoryManager`, `CommandProcessor`).
  - Execution of operations and their results.
  - Addition and removal of operations in history.
  - Errors and exceptions, such as division by zero or invalid commands.

**Impact**:
- **Debugging**: Facilitates tracking the flow of operations and identifying issues.
- **Monitoring**: Provides insights into the usage patterns and potential areas of improvement.
- **Maintenance**: Easier to trace and fix bugs with detailed logs.

## Setup Instructions

### Prerequisites

- **Python 3.7+**: Ensure that Python is installed on your system. You can download it from [Python's official website](https://www.python.org/downloads/).

### Installation

### Video 

https://drive.google.com/file/d/1P1wlbbT9OVHU0leMmLvlKptlnVzur-TC/view?usp=drive_link
