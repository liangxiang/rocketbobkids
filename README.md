# 🚀 RocketBobKids

A modern, responsive website for children's enrichment programs and summer camp activities.

## 📖 Overview

RocketBobKids is a comprehensive web platform that showcases various enrichment programs designed for children of all ages. From soccer and art classes to gymnastics, basketball, swimming, and summer camp activities, we provide tailored experiences that ignite curiosity and foster learning.

## ✨ Features

### 🎯 Core Functionality
- **Program Showcase**: Detailed pages for Soccer, Art Classes, Gymnastics, Basketball, and Swimming programs
- **Summer Camp**: Comprehensive information about our co-ed day camp for grades K-10
- **Responsive Design**: Optimized for desktop, tablet, and mobile devices
- **Mobile Navigation**: Hamburger menu for seamless mobile browsing
- **Contact Integration**: Easy access to phone and email contact options

### 🎨 Design & UX
- **Modern UI**: Clean, professional design using Tailwind CSS
- **Interactive Elements**: Hover effects, smooth animations, and transitions
- **Accessibility**: Keyboard navigation support and mobile-friendly interface
- **Brand Consistency**: Custom rocket favicon and cohesive visual identity

### 📱 Technical Features
- **Mobile-First**: Responsive navigation with collapsible hamburger menu
- **Performance**: Optimized loading times and smooth animations
- **SEO Ready**: Proper meta tags and structured content
- **Cross-Browser**: Compatible with all modern browsers

## 🛠️ Technology Stack

- **Backend**: Flask (Python web framework)
- **Frontend**: HTML5, CSS3, JavaScript (ES6+)
- **Styling**: Tailwind CSS v2.2.19
- **Icons**: Font Awesome 6.0.0
- **Development**: Python 3.x with Flask development server

## 📁 Project Structure

```
rocketbobkids/
├── app.py                 # Main Flask application
├── templates/             # HTML templates
│   ├── base.html         # Base template with navigation
│   ├── index.html        # Homepage
│   ├── programs.html     # Programs overview
│   ├── soccer.html       # Soccer program details
│   ├── art.html          # Art classes details
│   ├── gymnastics.html   # Gymnastics program details
│   ├── basketball.html   # Basketball program details
│   ├── swimming.html     # Swimming program details
│   ├── summer_camp.html  # Summer camp information
│   ├── about.html        # About us page
│   └── contact.html      # Contact information
├── static/               # Static assets
│   ├── css/
│   │   └── style.css     # Custom styles and animations
│   ├── js/
│   │   └── script.js     # JavaScript functionality
│   └── favicon.svg       # Website favicon
└── README.md             # This file
```

## 🚀 Quick Start

### Prerequisites
- Python 3.7 or higher
- Flask web framework

### Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd rocketbobkids
   ```

2. **Install dependencies**
   ```bash
   pip install flask
   ```

3. **Run the application**
   ```bash
   python app.py
   ```

4. **Open in browser**
   ```
   http://localhost:8080
   ```

## 🌐 Pages & Routes

| Route | Page | Description |
|-------|------|-------------|
| `/` | Home | Welcome page with mission and featured programs |
| `/programs` | Programs | Overview of all available programs |
| `/soccer` | Soccer | Soccer program details and schedule |
| `/art` | Art Classes | Art program information and age groups |
| `/gymnastics` | Gymnastics | Gymnastics classes and specialty programs |
| `/basketball` | Basketball | Basketball program for different age groups |
| `/swimming` | Swimming | Swimming lessons from infants to adults |
| `/summer-camp` | Summer Camp | Day camp information and activities |
| `/about` | About Us | Mission, values, and commitment |
| `/contact` | Contact | Contact information and program locations |

## 📱 Mobile Optimization

The website features a fully responsive design with special attention to mobile users:

- **Hamburger Navigation**: Clean mobile menu that doesn't overflow
- **Touch-Friendly**: Large buttons and touch targets
- **Fast Loading**: Optimized images and minimal JavaScript
- **Responsive Grid**: Content adapts to all screen sizes

## 🎨 Customization

### Colors & Branding
The website uses a consistent color scheme:
- **Primary**: Blue (#2563eb)
- **Secondary**: Purple (#7c3aed)
- **Accent**: Orange (#ea580c), Green (#10b981)
- **Text**: Gray scales for optimal readability

### Content Management
Program information is managed through Python dictionaries in `app.py`, making it easy to update:
- Program descriptions
- Age ranges and schedules
- Contact information
- Pricing details

## 📞 Contact Information

- **Email**: RocketBobKids02@gmail.com
- **Phone**: (650) 569-1741
- **Hours**: Monday-Friday 9:00 AM - 6:00 PM, Saturday 9:00 AM - 4:00 PM

## 🏢 Program Locations

- **Art Classes**: 908 Harmon Dr, Menlo Park, CA 94025
- **Soccer**: Multiple locations across Palo Alto area
- **Gymnastics**: Arrillaga Family Gymnastics Center
- **Basketball**: Fairmeadow Elementary School & Menlo Park Sports Center
- **Swimming**: Cubberley Community Center

## 📈 Development

### Recent Updates
- ✅ Responsive mobile navigation with hamburger menu
- ✅ Custom rocket favicon matching brand identity
- ✅ Complete brand transition from BobbyForFun to RocketBobKids
- ✅ Fixed button visibility issues on gradient backgrounds
- ✅ Individual program pages with detailed information

### Future Enhancements
- Online enrollment system
- Program calendar integration
- Photo galleries
- Parent testimonials
- Online payment processing

## 🤝 Contributing

To contribute to this project:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/new-feature`)
3. Make your changes
4. Test thoroughly on multiple devices
5. Commit your changes (`git commit -m 'Add new feature'`)
6. Push to the branch (`git push origin feature/new-feature`)
7. Create a Pull Request

## 📄 License

This project is proprietary and confidential. All rights reserved by RocketBobKids.

## 🆘 Support

For technical support or questions about the website:
- Email: RocketBobKids02@gmail.com
- Phone: (650) 569-1741

---

**Made with ❤️ for RocketBobKids - Where Fun Meets Learning!** 🚀
