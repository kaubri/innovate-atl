# What is CityPulse ATL?
CityPulse ATL is a pioneering initiative designed to bridge the gap between the people of Atlanta and their public officials. 
Our mission is simple yet profound: to empower individuals to report the needs of their city without the traditional barriers of
knowledge, accessibility, and bureaucracy.

# Demo
https://youtu.be/vyJQNnBq230

# Pitch deck
https://docs.google.com/presentation/d/1ZsGu14eIb4o9jRbsEvSH9I7RQb1G6kMIX5qDEgODpBg/edit?usp=sharing

# Tech Stack
- Language: Python 3
- Framework: Flask
- API: OpenAI API (model: gpt-3.5-turbo)
- Observability: New Relic

# Run CityPulse ATL
The CityPulse application exists within a docker container to ensure a consistent environment when running and because NewRelic required a Linux environment when using Flask.

config.py is not in source-control because it serves as a configuration file that contains the OpenAI API key.

To run locally, you will need to create this file and set OPENAI_API_KEY to your OpenAI API Key

```
# Configuration file
# Ensure that this file is included in .gitignore

# Development API token
OPENAI_API_KEY = 'YOUR_KEY_HERE'
```

Then, you can run the application locally, making sure to specify your New Relic license key:
```
docker build --build-arg NEW_RELIC_LICENSE_KEY='YOUR_LICENSE_KEY' -t citypulse-app .

docker run -p 5000:5000 citypulse-app
```

# Usage
## Example prompts to try
Infrastructure Installation:
```
I live at 342 Relic Lane and I really wish we had a bike lane for my morning workout
```

Infrastructure Maintenance:
```
Estoy en la avenida Render y mi llanta explotó debido al bache en el carril izquierdo. (Google Translated from: i'm on render ave and my tire blew because of the pothole in the left lane)
```

```
yo what's up with all these potholes on Auburn ave?
```

Public Safety:
```
A tree has fallen on 75 north near exit 260!
```

# Supported Hackathon User Cases

## Categories 
- Infrastructure Installation
- Infrastructure Repair
- Public Safety Concerns

## Examples of service requests for each category
1. **Infrastructure Installation:**
   - Request for new sidewalks or crosswalks
   - Requests for new streetlights
   - Request for public facilities (e.g., benches, waste bins)

1. **Infrastructure Maintenance or Repairs:**
   - Broken streetlights
   - Potholes and road damage
   - Damaged or missing road signs
   - Blocked or damaged sidewalks
   - Flooding or drainage problems
   - Street Cleaning

1. **Public Safety Concerns:**
   - Graffiti and vandalism
   - Illegal dumping or littering
   - Suspicious activities or loitering
   - Unsafe playground equipment
   - Overgrown vegetation obstructing visibility

# Future Work and Opportunities:
- Route requests to database and to a specific department
- Add support for phone calls by using OpenAI's translate and transcribe endpoints
- Extend categories to fit needs of City of Atlanta.
- Expand to metro Atlanta (Marietta, Dunwoody, etc)
- A site where users can see popular and/or recent requests.
  - Ensure AI can identify new requests that are similar to others and let officials know in analytics
