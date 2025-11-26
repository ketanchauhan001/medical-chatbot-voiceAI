📘 Project Overview – Medical Chatbot VoiceAI

Medical Chatbot VoiceAI is an AI-powered healthcare assistant designed to help users interact using voice and text. The project combines natural language understanding, speech processing, and information retrieval to answer medical-related questions in a convenient and interactive way.

The system allows users to speak their health queries, processes the input through speech-to-text, generates accurate responses using AI models, and returns the answer through both text output and text-to-speech audio. It also stores conversational data in a vector database, enabling context-aware replies in future interactions.

This project aims to simplify access to basic medical information, provide quick answers for common symptoms, and serve as the foundation for more advanced healthcare AI applications such as telemedicine assistants, patient triage systems, and personal healthcare companions.



🎯 Objectives

Provide users with instant medical information using AI.

Build a voice-enabled chatbot for hands-free interaction.

Maintain conversation history to improve response quality over time.

Support medical document generation (PDFs) for reference.

Offer a simple and intuitive web interface for seamless interaction.



🧠 Key Capabilities
1. Voice Interaction

Speech-to-Text (STT) for user input

Text-to-Speech (TTS) for spoken responses

Real-time microphone recording and playback

2. AI-Powered Medical Q&A

Responds to queries about diseases, symptoms, medicines, etc.

Uses retrieval-augmented generation (RAG) for improved accuracy

Supports follow-up questions with contextual memory

3. Vector Database

Stores past chat data for future reference

Improves personalization

Enables semantic search

4. PDF Generation

Export chat history or medical notes

Automatically saves PDFs in the pdfs/ folder

5. Clean Web UI

HTML-based chat interface

Supports text chat + voice chat

Audio playback for responses



🏗 Architecture Summary

The system consists of:

Frontend (HTML templates) → Chat UI, microphone, stop button, audio playback

Backend (Python) → STT, TTS, AI response generation, PDF creation

Vector Store → Memory and context management

Static Files → Audio resources, generated outputs

Modules Folder → Helper logic for AI, audio, and utilities



👨‍⚕️ Use Cases

Ask about symptoms, diseases, or medical conditions

Get explanations for medicines or treatments

Voice-based medical assistant

Generate medical notes or summaries

Educational tool for students
