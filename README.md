
# Social Media Analytics Tool with DataStax Astra DB + Langflow

## Hi there! 👋
I built this tool to help analyze social media content performance using DataStax Astra DB and Langflow. It's a project for the Level Supermind Hackathon that looks at how different types of posts (photos, videos, reels, text) perform and gives you useful insights about what works best.

## What This Tool Does 🚀
- Analyzes how well your posts are doing in real-time
- Compares different types of content
- Automatically calculates engagement metrics
- Uses GPT to give you content suggestions
- Helps find similar content
- Shows which hashtags work best
- Predicts how new content might perform

## How It Works 🛠️
### The Main Parts:
1. **DataStax Astra DB**
   - Stores and organizes all your post data
   - Makes it easy to find similar content
   - Handles lots of data smoothly

2. **Langflow**
   - Connects everything together
   - Processes data automatically
   - Works with GPT to give you insights

3. **Analytics**
   - Calculates engagement numbers
   - Spots trends in your content
   - Compares different post types
   - Shows which hashtags are working

## Getting Started 🔧

### Prerequisites
- DataStax Astra DB account
- OpenAI API key
- Python 3.8+
- Langflow

### Installation

1. **Clone the repository**
```bash
git clone [your-repo-url]
cd level-supermind-socialmedia
```

2. **Set up environment variables**
```bash
cp .env.example .env
# Edit .env with your credentials:
# ASTRA_DB_APPLICATION_TOKEN=your_token
# ASTRA_DB_API_ENDPOINT=your_endpoint
# OPENAI_API_KEY=your_key
```

3. **Install Langflow**
```bash
pip install langflow
```

4. **Run Langflow**
```bash
langflow run
```

### Want to Try It? 🔄

This project is easy to replicate using the provided sample data:

1. **Get the Data**
   - Check the `mockdata` folder for the sample dataset
   - Contains 200 social media posts with likes, comments, shares, and hashtags
   - Real-world engagement patterns included

2. **Set Up the Flow**
   - Import the Langflow JSON from the `src` folder
   - Found in: `src/langflow_social_analytics.json`
   - This sets up the entire workflow automatically

3. **Configure DataStax**
   - Use your Astra DB credentials
   - Collection name: "socialmedia"
   - Import mock data using the provided script

## Features in Detail 🔍

### 1. Data Analysis
- Real-time engagement tracking
- Historical trend analysis
- Performance benchmarking
- Content type comparison

### 2. Content Recommendations
- AI-powered suggestions
- Best times to post
- Hashtag recommendations
- Content type optimization

### 3. Predictive Features
- Engagement forecasting
- Content success prediction
- Trend analysis
- Strategy recommendations

## Project Structure 📁
```
level-supermind-socialmedia/
├── src/
│   ├── langflow_social_analytics.json

├── mockdata/
│   └── Mock Social Posts Dec 2024.csv
└── README.md
```

## Sample Data Structure 📊
The mock dataset includes:
- post_id (Integer)
- post_type (String)
- likes (Integer)
- comments (Integer)
- shares (Integer)
- date_posted (String)
- hashtags (String)



## Common Issues & Solutions 🔧

1. **DataStax Connection**
   - Make sure your credentials are correct
   - Check collection name matches
   - Verify API endpoint

2. **Langflow Import**
   - Use the latest Langflow version
   - Import JSON through the UI
   - Check all connections are made



## Acknowledgments 🙏
- Level Supermind Hackathon
- DataStax Team
- Langflow Community

