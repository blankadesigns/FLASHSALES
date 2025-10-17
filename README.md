# Marketplace - Cloud-ready (Postgres + S3 + Vite React)

This is a cloud-ready version of the mini Marketplace app.

Structure:
- server/  (Express backend - Postgres + S3)
- client/  (React + Vite frontend)

Quick start (local testing requires Postgres + S3 or you can use Render & Vercel):

1. Server
   - Edit server/.env.example -> create a .env with real values OR set env vars in Render.
   - Install dependencies:
     cd server
     npm install
   - Run migrations on your Postgres (server/migrations/001_create_tables.sql)
   - Start:
     NODE_ENV=development node server.js

2. Client
   cd client
   npm install
   VITE_API_ROOT=http://localhost:4000 npm run dev

Deploy:
- Host server on Render (Docker or Node) and client on Vercel.
- See the repository or conversation for detailed deploy steps.

