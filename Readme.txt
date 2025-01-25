# WhatsApp Auto-Reply Chatbot

This Python script automates replying to WhatsApp messages using OpenAI's GPT-3.5 model. It utilizes PyAutoGUI for automation, Pyperclip for clipboard management, and OpenAI's API for generating responses.

## Prerequisites

- Python 3.x
- Libraries: `pyautogui`, `pyperclip`, `openai`
- OpenAI API Key

Install dependencies using:

```bash
pip install pyautogui pyperclip openai
```

## Setup

1. Replace `client = OpenAI()` with your OpenAI API key initialization.
2. Adjust screen coordinates for your display (use `pyautogui.position()` to get screen positions).
3. Modify the `is_last_message_from_sender()` function to check the desired sender.

## How It Works

1. **Launches WhatsApp Web**: Clicks on the Chrome icon and opens WhatsApp.
2. **Selects and Copies Text**: Copies the latest message from the chat.
3. **Generates Response**: Sends the chat history to OpenAI and generates a reply.
4. **Pastes and Sends Reply**: Pastes the response back to WhatsApp and sends it.
5. **Continuous Monitoring**: Repeats the process every 5 seconds.

## Customization

- **Sender ID**: Modify `is_last_message_from_sender()` to check for different senders.
- **Coordinates**: Adjust the mouse coordinates for selecting text, pasting, and sending messages.
- **Response Style**: Customize the system message to change the chatbot's tone and behavior.

## Usage

1. Open WhatsApp Web and log in.
2. Run the script:
   ```bash
   python whatsapp_auto_reply.py
   ```
3. The script will monitor messages and automatically respond.
