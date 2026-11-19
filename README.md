# paris-travel-chatbot-openaiapi
An AI-powered virtual travel guide for Paris using the OpenAI Python SDK. Features sequential conversation history, structured JSON outputs, and prompt engineering.

# OpenAI Paris Travel Guide

A Python-based AI travel assistant designed for Peterman Reality Tours. This project utilizes the OpenAI API to answer common tourist questions about Paris, France.

## Features
- **Sequential Context:** Maintains conversation history to provide context-aware answers.
- **Deterministic Output:** Uses a `temperature` of 0.0 to ensure factual, consistent responses.
- **Token Management:** Limits responses to 100 tokens for concise, easy-to-read travel tips.
- **Structured Data:** Stores the conversation in a list of dictionaries as a JSON object.

## Contextual Memory Demonstration

To prove that this chatbot maintains state and remembers previous conversations, I tested it with follow-up questions that use pronouns and implicit references. 

For example:
- **User:** *"How long would it take to drive that distance?"* (The AI knows this refers to the Louvre to the Eiffel Tower).
- **User:** *"Who painted the most famous piece you just mentioned?"* (The AI knows this refers to the Mona Lisa).
