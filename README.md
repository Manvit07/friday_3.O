# Friday 3.0 - Personal AI Assistant

## Table of Contents
1. [Overview](#overview)
2. [Features](#features)
3. [Libraries Used](#libraries-used)
4. [How It Works](#how-it-works)
   - [Voice Commands](#1-voice-commands)
   - [Task Automation](#2-task-automation)
   - [Speech Output](#3-speech-output)
5. [Key Functionalities](#key-functionalities)
   - [Greeting and Interaction](#greeting-and-interaction)
   - [YouTube Music Search](#youtube-music-search)
   - [Google Search](#google-search)
   - [System Control](#system-control)
   - [Webcam Access](#webcam-access)
   - [Screenshots](#screenshots)
   - [IP Address](#ip-address)
6. [Installation](#installation)
7. [Usage](#usage)
8. [Future Enhancements](#future-enhancements)
9. [Contributing](#contributing)
10. [License](#license)

## Overview

**Friday 3.0** is a voice-controlled AI personal assistant that allows you to automate various tasks on your computer. From opening applications to playing music on YouTube, performing Google searches, controlling system settings, and more, Friday is designed to make your computer experience more convenient and efficient.

## Features

- **Voice Interaction**: Control your system using natural voice commands.
- **Date and Time Queries**: Ask Friday for the current time, date, and day of the week.
- **YouTube Search and Play**: Search and play music directly from YouTube.
- **Google Search**: Perform web searches and read the top results.
- **Application Control**: Open/close applications like Notepad, Paint, and browser tabs.
- **System Control**: Manage system functions like shutdown, restart, and locking the system.
- **Webcam Access**: Activate the camera and display the feed.
- **Screenshots**: Take screenshots of your screen.
- **IP Address**: Get your system's public IP address.
- **Volume Control**: Adjust the system's volume through voice commands.
- **Note Taking**: Open Notepad for quick note-taking.
- **Weather Information**: Get current weather details by searching on Google.

## Libraries Used

To implement these features, the following Python libraries are used:

- `pyttsx3` - For text-to-speech conversion.
- `speech_recognition` - For converting voice commands into text.
- `datetime` - For handling time, date, and day functions.
- `webbrowser` - For opening web pages in the default browser.
- `requests` - For making HTTP requests to the web.
- `BeautifulSoup` - For scraping Google search results.
- `pywhatkit` - For playing YouTube videos via commands.
- `os` - To interact with system functions.
- `cv2` (OpenCV) - For webcam handling.
- `pyautogui` - For automating system tasks like screenshots, volume control, and more.
- `time` - For managing timing and delays.

## How It Works

### 1. Voice Commands
Friday uses the `speech_recognition` library to listen to voice inputs via the microphone. After recognizing the speech, it converts the command to text and executes the relevant task.

### 2. Task Automation
Friday can automate tasks like opening applications, performing web searches, and controlling system settings, using Python libraries like `os`, `webbrowser`, `pyautogui`, and others.

### 3. Speech Output
Friday responds with spoken feedback using `pyttsx3` for text-to-speech conversion, informing the user of the status of their request.


