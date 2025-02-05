# google-ads-chatbot
This project is a web-based AI chatbot that automates Google Ads campaign creation using ChatGPT. The chatbot interacts with business owners, gathers relevant details, and generates campaign recommendations.

Features

Conversational chatbot for business owners

Collects business details for ad campaign creation

Uses ChatGPT for intelligent responses

Simple web-based UI (React.js)

FastAPI backend for chatbot interactions

Tech Stack

Frontend: React.js (with TailwindCSS for styling)

Backend: FastAPI (Python)

AI Model: ChatGPT (OpenAI API)

Hosting: Can be deployed on Vercel (Frontend) & Render/Heroku (Backend)

Installation & Setup

Prerequisites

Node.js & npm (for frontend)

Python & pip (for backend)

OpenAI API key

Frontend Setup

cd frontend
npm install
npm run dev

Backend Setup

cd backend
pip install -r requirements.txt
uvicorn main:app --reload

API Endpoints

POST /api/chat - Sends user messages to ChatGPT and returns responses.

Usage

Start the backend server.

Run the frontend development server.

Interact with the chatbot to generate Google Ads campaigns.

Contributing

Feel free to fork the repository and submit pull requests with improvements!

License

MIT License

