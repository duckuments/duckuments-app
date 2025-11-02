# Duckuments

![Duckuments Logo](./duckuments/duckumets-img.jpg)

An AI-powered documentation generator that transforms your source code into comprehensive, modular Markdown documentation with just a few clicks.

## 🚀 Features

- **AI-Powered Documentation**: Leverages advanced AI models (GPT-4o or Ollama) to generate high-quality documentation
- **Multi-Language Support**: Currently supports Python projects with extensible architecture for more languages
- **Real-time Preview**: Live preview of generated documentation with syntax highlighting
- **Secure File Handling**: Safe extraction and processing of uploaded code archives
- **User Management**: JWT-based authentication with custom user profiles and coin-based usage tracking
- **Modern UI**: Built with Next.js, React, and shadcn/ui for a sleek, responsive interface
- **RESTful API**: Comprehensive Django REST Framework API for all operations

## 🏗️ Architecture

### Backend (Django)
- **Framework**: Django 4.x with Django REST Framework
- **Authentication**: JWT tokens with custom user model
- **Database**: SQLite (easily configurable for PostgreSQL/MySQL)
- **File Processing**: Secure zip extraction and AI integration
- **API**: RESTful endpoints for all operations

### Frontend (Next.js)
- **Framework**: Next.js 15 with App Router
- **UI Library**: shadcn/ui components with Radix UI primitives
- **Styling**: Tailwind CSS with custom design system
- **Code Editor**: CodeMirror for markdown rendering and editing
- **State Management**: React hooks with context providers

## 📋 Prerequisites

- Python 3.8+
- Node.js 18+
- OpenAI API key (for GPT-4o) or Ollama (for local LLM)

## 🛠️ Installation & Setup

### Backend Setup

1. **Clone and navigate to backend directory:**
   ```bash
   cd duckuments/duckumentsCore
   ```

2. **Create virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r ../requirements.txt
   ```

4. **Configure environment:**
   - Set your OpenAI API key in `duckumentsCore/settings.py` or environment variables
   - Configure email settings for user notifications
   - Update CORS settings for frontend URL

5. **Run migrations:**
   ```bash
   python manage.py migrate
   ```

6. **Start development server:**
   ```bash
   python manage.py runserver
   ```

### Frontend Setup

1. **Navigate to frontend directory:**
   ```bash
   cd duckuments-site/duckuments
   ```

2. **Install dependencies:**
   ```bash
   npm install
   ```

3. **Configure environment:**
   - Create `.env.local` with backend API URL
   - Configure authentication providers if needed

4. **Start development server:**
   ```bash
   npm run dev
   ```

## 📖 Usage

1. **Sign Up/Login**: Create an account or log in to access the dashboard
2. **Create Project**: Upload a zip file containing your source code
3. **Configure**: Add project description and select programming language
4. **Generate**: AI processes your code and generates documentation
5. **Preview & Download**: View live preview and download generated Markdown files

## 🔌 API Documentation

### Authentication Endpoints
- `POST /auth/signup/` - User registration
- `POST /auth/login/` - User login

### Account Management
- `GET /account/profile/` - Get user profile
- `POST /account/avatar/` - Upload avatar
- `POST /account/password/` - Change password

### Project Management
- `GET /project/all/` - List user projects
- `POST /project/new/` - Create new project
- `GET /project/doc/<slug>/` - Get documentation preview
- `GET /project/download/<slug>/` - Download documentation

## 🤖 AI Integration

Duckuments supports multiple AI backends:

### OpenAI GPT-4o
- High-quality documentation generation
- Fast inference times
- Secure API-based processing
- Requires OpenAI API key

### Ollama (Local LLM)
- Privacy-focused local processing
- No API costs
- Supports various open-source models
- Enhanced security for sensitive codebases

## 🏛️ Project Structure

```
duckuments-app/
├── duckuments/                    # Backend (Django)
│   ├── duckumentsCore/
│   │   ├── account/              # User management app
│   │   ├── projects/             # Project & documentation app
│   │   ├── settings.py           # Django settings
│   │   └── urls.py               # Main URL configuration
│   ├── media/                    # User uploads & generated files
│   ├── requirements.txt          # Python dependencies
│   └── manage.py                 # Django management script
├── duckuments-site/              # Frontend (Next.js)
│   └── duckuments/
│       ├── app/                  # Next.js app directory
│       ├── components/           # Reusable UI components
│       ├── package.json          # Node dependencies
│       └── next.config.mjs       # Next.js configuration
└── README.md                     # This file
```

## 🔒 Security Features

- JWT-based authentication
- File type and size validation
- Secure file extraction
- Automatic cleanup of temporary files
- CORS protection
- Input sanitization

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- OpenAI for GPT-4o API
- Ollama for local LLM support
- shadcn/ui for beautiful components
- Django and Next.js communities

---

Built with ❤️ for developers who value comprehensive documentation


