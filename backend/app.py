from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for frontend requests

@app.route('/')
def home():
    return jsonify({"message": "Welcome to the Backend API!"})

@app.route('/api/skills')
def get_skills():
    skills = {
        "frontend": ["HTML", "CSS", "JavaScript", "React"],
        "backend": ["Python", "Node.js", "Express", "Flask"],
        "databases": ["MongoDB", "PostgreSQL", "MySQL"]
    }
    return jsonify(skills)

@app.route('/api/projects')
def get_projects():
    projects = [
        {
            "id": 1,
            "title": "Task Management App",
            "description": "A web app for managing daily tasks",
            "technologies": ["React", "Node.js", "MongoDB"]
        },
        {
            "id": 2,
            "title": "E-commerce Platform",
            "description": "Full-stack e-commerce site with payment integration",
            "technologies": ["React", "Express", "PostgreSQL", "Stripe"]
        },
        {
            "id": 3,
            "title": "Algorithm Visualizer",
            "description": "Interactive tool to visualize sorting and searching algorithms",
            "technologies": ["JavaScript", "Canvas API"]
        }
    ]
    return jsonify(projects)

@app.route('/api/contact', methods=['POST'])
def contact():
    return jsonify({"message": "Thank you for your message! We'll get back to you soon."})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
