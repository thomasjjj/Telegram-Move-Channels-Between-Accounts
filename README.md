# Telegram Channel Transfer Tool

This project consists of two Python scripts that enable you to transfer Telegram channels and groups that you follow from one account to another. The first script exports the list of channels and groups to a `.txt` file, while the second reads this file and adds these channels and groups to another Telegram account.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Setup](#setup)
  - [Clone the Repository](#clone-the-repository)
  - [Install Dependencies](#install-dependencies)
- [How to Get Telegram API Credentials](#how-to-get-telegram-api-credentials)
- [Usage](#usage)
  - [Export Channels](#export-channels)
  - [Import Channels](#import-channels)

## Prerequisites

1. **Python 3.x** - Download and install it from [here](https://www.python.org/downloads/).
2. **Telegram Account** - You should have an existing Telegram account.
3. **Git** (Optional) - Download and install it from [here](https://git-scm.com/) if you wish to clone the repository.

## Setup

### Clone the Repository

If you've never used Git before, you'll need to install it first. Download and install Git from [here](https://git-scm.com/download/win) if you're on Windows or follow instructions for other operating systems as outlined on the official site.

Once Git is installed, proceed with the following steps to clone this repository to your local machine:

1. Open your terminal (Command Prompt on Windows, Terminal on macOS or Linux).
2. Navigate to the folder where you would like to download this project to. Use the `cd` command to navigate to your desired folder. For example:

    ```bash
    cd path/to/your/folder
    ```

3. Once you're in the folder, copy and paste the following command into your terminal and press Enter:

    ```bash
    git clone <repository_link>
    ```

Replace `<repository_link>` with the URL of this GitHub repository, which you can find by clicking the green 'Code' button near the top right of the GitHub repository page.

### Install Dependencies

Before running any Python code, you'll need to install the required Python packages. Follow these steps to install the dependencies:

1. Make sure you have Python installed. If not, you can download and install it from [here](https://www.python.org/downloads/).
  
2. Open your terminal (Command Prompt on Windows, Terminal on macOS or Linux).
  
3. Navigate to the project folder where the `requirements.txt` file is located. If you've just cloned the repository, you should do:

    ```bash
    cd path/to/cloned/repository
    ```
  
4. Once you're in the project folder, run the following command to install the required Python packages:

    ```bash
    pip install -r requirements.txt
    ```

This will read the `requirements.txt` file and install all the packages listed there.



This will install all the necessary packages listed in `requirements.txt`.

## How to Get Telegram API Credentials

Before you proceed, you'll need the `api_id` and `api_hash` from Telegram. Follow these steps:

1. Go to [Telegram's Developer website](https://my.telegram.org/auth).
2. Log in with your Telegram account.
3. Click on "API development tools".
4. Fill out the form to create a new application.
5. You will be given an `api_id` and an `api_hash`. Keep these safe.

## Usage

### Export Channels

To export channels from your Telegram account, run the export script:

1. Navigate to the directory where the script is located.
2. Open your terminal and run:

\`\`\`bash
python <export_script_name>.py
\`\`\`

3. Follow the prompts to enter your `api_id`, `api_hash`, and phone number.

The list of channels and groups will be saved in a file named `channels.txt`.

### Import Channels

To import the channels to another Telegram account, run the import script:

1. Navigate to the directory where the script is located.
2. Open your terminal and run:

\`\`\`bash
python <import_script_name>.py
\`\`\`

3. Follow the prompts to enter your `api_id`, `api_hash`, and phone number.

The channels will be added to your Telegram account.
