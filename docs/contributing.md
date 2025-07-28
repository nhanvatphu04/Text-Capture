# Contributing to TextCapture

Thank you for your interest in contributing to TextCapture! This guide will help you get started with contributing to the project.

## 🤝 How to Contribute

### Types of Contributions
We welcome various types of contributions:

- **🐛 Bug Reports**: Report issues you encounter
- **✨ Feature Requests**: Suggest new features
- **📝 Documentation**: Improve or add documentation
- **🔧 Code Contributions**: Submit code improvements
- **🧪 Testing**: Help test the application
- **🌍 Translations**: Add support for new languages

## 🚀 Getting Started

### Prerequisites
- **Git** installed on your system
- **Python 3.8+** for development
- **GitHub account** for submitting contributions

### Development Setup
1. **Fork the repository** on GitHub
2. **Clone your fork**:
   ```bash
   git clone https://github.com/nhanvatphu04/Text-Capture.git
   cd Text-Capture
   ```
3. **Set up development environment**:
   ```bash
   python -m venv venv
   venv\Scripts\activate  # Windows
   source venv/bin/activate  # macOS/Linux
   pip install -r requirements.txt
   ```
4. **Create a feature branch**:
   ```bash
   git checkout -b feature/your-feature-name
   ```

## 🔧 Development Tools

### Recommended Tools
- **VS Code** with Python and C++ extensions
- **Git** for version control
- **Black** for code formatting
- **Flake8** for linting
- **MyPy** for type checking

### Setup Development Tools
```bash
# Install development dependencies
pip install black flake8 mypy pytest

# Format code
black src/

# Check code style
flake8 src/

# Type checking
mypy src/
```

## 🏷️ Release Process

### Version Numbers
We use [Semantic Versioning](https://semver.org/):
- **MAJOR.MINOR.PATCH**
- **MAJOR**: Breaking changes
- **MINOR**: New features, backward compatible
- **PATCH**: Bug fixes, backward compatible

### Release Checklist
- [ ] All tests pass
- [ ] Documentation updated
- [ ] Version number updated
- [ ] Changelog updated
- [ ] Release notes prepared
- [ ] C++ module rebuilt if needed

## 🤝 Community Guidelines

### Code of Conduct
- **Be respectful** and inclusive
- **Help others** learn and contribute
- **Provide constructive feedback**
- **Follow project guidelines**

### Communication
- **Use clear, professional language**
- **Be patient** with new contributors
- **Ask questions** when unsure
- **Share knowledge** and experiences

## 📞 Getting Help

### Resources
- **[GitHub Issues](https://github.com/nhanvatphu04/Text-Capture/issues)**: For bugs and feature requests
- **[Discussions](https://github.com/nhanvatphu04/Text-Capture/discussions)**: For questions and ideas
- **[Documentation](README.md)**: For setup and usage guides

### Contact
- **Create an issue** for bugs or feature requests
- **Start a discussion** for questions or ideas
- **Join the community** to connect with other contributors

## 🙏 Recognition

### Contributors
All contributors will be recognized in:
- **README.md** contributors section
- **Release notes** for their contributions
- **GitHub contributors** page

### Types of Recognition
- **Code contributions**: Listed in contributors
- **Documentation**: Acknowledged in docs
- **Testing**: Recognized in release notes
- **Community support**: Thanked in discussions

---

**Thank you for contributing to TextCapture!** Your contributions help make this project better for everyone.

*For questions about contributing, please open an issue or start a discussion on GitHub.* 