# OnBrand MVP v0.4
*Proactive Brand Consistency Platform*

## 🎯 Problem Statement

Most AI content tools provide generic analysis that sounds the same for every brand. **OnBrand** solves this by creating sophisticated, actionable brand personality profiles that capture the nuances of how different traits work together to create a unique brand voice.

## ✨ What OnBrand Does

OnBrand analyzes your brand across three core dimensions:
- **Casual ↔ Formal**: Communication style and tone
- **Playful ↔ Serious**: Approach to engagement and personality  
- **Simple ↔ Technical**: Complexity and depth of communication

Instead of generic analysis, OnBrand provides:
- **Trait Complementarity**: How your brand voice dimensions work together
- **Productive Tensions**: Where contrasts create an interesting human voice
- **Dominance Moments**: When different traits should lead your communication
- **Brand Voice Archetype**: Clear positioning and communication strategy

## 🚀 Current Features (v0.4)

- Interactive brand personality assessment (3-slider system)
- AI-powered personality synthesis using Claude Sonnet 4
- Professional brand voice analysis with actionable insights
- Content analysis with OnBrand scoring (0-100)
- **Multi-platform optimization**: Twitter, LinkedIn, Email, and Blog support
- **Smart validation**: Character limits for social platforms, word count recommendations for long-form content
- **Professional error handling** with user-friendly messaging
- Timestamped analysis history and file saving
- Complete user workflow with exit options at all decision points
- Secure API key management with environment variables

## 📋 Requirements

- Python 3.7+
- Anthropic API key
- Required packages: `anthropic`, `python-dotenv`

## 🛠️ Installation

1. Clone the repository:
```bash
git clone https://github.com/Innovictor/onbrand-mvp.git
cd onbrand-mvp
```

2. Install dependencies:
```bash
pip3 install anthropic python-dotenv
```

3. Create `.env` file with your Anthropic API key:
```
ANTHROPIC_API_KEY=your-api-key-here
```

4. Run OnBrand:
```bash
python3 onbrand_mvp.py
```

## 💡 Example Output

```
Brand Voice Archetype: The Articulate Expert

This brand embodies an intelligent, trustworthy professional who speaks 
with measured confidence. Technical depth is elegantly framed through a 
formal lens, creating authority without coldness.

Dominant Trait Moments:
- Technical precision emerges during detailed explanations
- Formal professionalism shines in high-stakes contexts  
- Subtle playfulness appears in explanatory moments
```

## 🗺️ Roadmap

**v0.2 (✅ Completed):**
- User confirmation workflow (accept/adjust brand personality)
- Parameter adjustment loop with seamless UX
- Graceful exit options and enhanced user experience
- Upgraded AI model for improved accuracy

**v0.3 (✅ Completed):**
- Content analysis against brand personality
- OnBrand scoring (0-100) with improvement suggestions
- Platform-specific analysis (Twitter 280 chars, LinkedIn 1300 chars)
- Character limit validation and platform context
- Timestamped analysis history with file saving
- User exit options at all decision points
- Loading states and UX improvements

**v0.4 (✅ Completed):**
- **Email and Blog platform support** with word-count validation
- **Professional error handling** and user experience improvements
- **Enhanced content validation** with platform-specific recommendations
- Multi-tier validation system with user override options
- OnBrand-consistent messaging throughout application

**v0.5 (Coming Next):**
- Data visualization and analytics dashboard
- Additional platform support (Instagram, Facebook)
- Batch content analysis capabilities
- Enhanced file management and history tracking

**v1.0 (Vision):**
- Multi-platform analysis and optimization
- Brand personality persistence (save/load profiles)
- Brand voice memory and learning
- Team collaboration features

## 🎨 Technical Approach

OnBrand differentiates through:
- **Domain Expertise Integration**: I have 12+ years of marketing communications experience and found generic AI solutions lacking providing brand-specific insights across industries
- **Sophisticated Analysis Framework**: Goes beyond simple sentiment to analyze trait interactions and communication strategy
- **Professional Output**: Consultant-grade brand voice descriptions ready for strategy documents

## 📈 Commercial Applications

- **Marketing Teams**: Consistent brand voice across campaigns and channels
- **Content Creators**: Ensure content matches brand personality guidelines  
- **Brand Consultants**: Data-driven brand voice development and documentation
- **Agencies**: Scalable brand analysis for multiple clients

## 🔧 Built With

- **Python**: Core application logic and user interface
- **Anthropic Claude 3.5 Haiku**: AI-powered brand personality analysis. I will experiment with different Claude models over time.
- **python-dotenv**: Secure environment variable management
- **Professional Development Practices**: Git version control, environment security, incremental development

## 📝 Development Notes

I built this project using a **pseudocode-first methodology**:
1. Complete user journey mapped in plain English
2. Logic refined and validated before coding
3. Incremental development with testing at each milestone
4. Professional security practices (environment variables, .gitignore)

**Technical Limitations**: Terminal input is currently limited to approximately 1000 characters due to system constraints. This will be resolved with web interface implementation in future versions.

## 🤝 Contributing

OnBrand MVP is currently in active development. Future versions will include expanded functionality and team collaboration features.

## 📄 License

This project is part of a learning portfolio demonstrating professional programming practicies in Python, AI integration, and product development.

---

### Built by: Victor Alagbe 

#### Why?

I am a content marketing professional with 12 years of experience in emerging technologies, most recently in Web3. With the explosion of AI solutions for marketing professionals, I have observed that most tools provide generic results that don't offer much value to marketers worthy of the name or recommendations that could be logged under the "AI slop" category. This is an attempt to leverage my domain expertise from a Bachelor's degree in Linguistics and an MSc in Marketing Communications, plus more than a decade's worth of hands-on experience to create AI-powered tools that actually get the job done for marketers.