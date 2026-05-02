![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![OpenCV](https://img.shields.io/badge/OpenCV-4.x-5C3EE8?style=for-the-badge&logo=opencv&logoColor=white)
![MediaPipe](https://img.shields.io/badge/MediaPipe-Hand_Tracking-0097A7?style=for-the-badge&logo=google&logoColor=white)
![PyAutoGUI](https://img.shields.io/badge/PyAutoGUI-Mouse_Control-FF6B6B?style=for-the-badge&logo=python&logoColor=white)
![SpeechRecognition](https://img.shields.io/badge/SpeechRecognition-Voice_Input-4CAF50?style=for-the-badge&logo=google&logoColor=white)
![pyttsx3](https://img.shields.io/badge/pyttsx3-Text_to_Speech-FF9800?style=for-the-badge&logo=python&logoColor=white)
![Threading](https://img.shields.io/badge/Multithreading-Parallel_Execution-9C27B0?style=for-the-badge&logo=python&logoColor=white)
![OpenWeatherMap](https://img.shields.io/badge/OpenWeatherMap-Weather_API-EB6E4B?style=for-the-badge&logo=openweathermap&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Active-brightgreen?style=for-the-badge)
<h1>AI Gesture & Voice Assistant</h1>

<p>
A real-time multimodal system enabling touchless system control using computer vision and voice AI.
</p>

<hr>

<h2>🎯 Problem Statement</h2>

<p>
Traditional human-computer interaction relies heavily on physical input devices like a mouse and keyboard.
This project provides a <strong>touchless interaction system</strong>, enabling users to control their system using gestures and voice — useful for accessibility, productivity, and futuristic UI systems.
</p>

<hr>

<h2>✨ Key Features</h2>

<ul>
<li>🖐️ Real-time <strong>hand gesture-based mouse control</strong></li>
<li>🎙️ Voice assistant for executing commands</li>
<li>🌐 Open websites (YouTube, Google, Instagram) via voice</li>
<li>💻 Launch desktop applications (Notepad, Calculator)</li>
<li>🌦️ Fetch real-time weather data using API</li>
<li>🔄 Multithreading: runs gesture + voice simultaneously</li>
<li>⚡ Smooth cursor movement and gesture-based clicking, scrolling, and zooming</li>
</ul>

<hr>

<h2>🛠️ Tech Stack</h2>

<table border="1">
<tr>
<th>Tool</th>
<th>Purpose</th>
</tr>
<tr>
<td>Python</td>
<td>Core programming language</td>
</tr>
<tr>
<td>OpenCV</td>
<td>Image processing & webcam handling</td>
</tr>
<tr>
<td>MediaPipe</td>
<td>Hand tracking & landmark detection</td>
</tr>
<tr>
<td>PyAutoGUI</td>
<td>Mouse automation</td>
</tr>
<tr>
<td>SpeechRecognition</td>
<td>Voice input processing</td>
</tr>
<tr>
<td>pyttsx3</td>
<td>Text-to-speech output</td>
</tr>
<tr>
<td>Requests</td>
<td>API integration (weather)</td>
</tr>
</table>

<hr>

<h2>🧠 System Architecture</h2>

<p><strong>Gesture Pipeline</strong></p>
<p>Camera → MediaPipe → Gesture → Mouse</p>

<p><strong>Voice Pipeline</strong></p>
<p>Microphone → SpeechRecognition → Command → Action</p>

<hr>

<h2>📊 Key Insights / Results</h2>

<ul>
<li>Built a <strong>real-time multimodal system</strong> combining computer vision and voice AI</li>
<li>Achieved smooth cursor control using gesture interpolation and filtering</li>
<li>Implemented <strong>event-driven multithreading</strong> for parallel execution</li>
<li>Reduced dependency on physical input devices → improved accessibility use case</li>
<li>Demonstrates practical integration of <strong>AI and system automation</strong></li>
</ul>

<hr>


<h2>⚙️ How to Run</h2>

<h3>1. Clone the repository</h3>

<pre>
git clone https://github.com/your-username/gesture-voice-ai-assistant.git
cd gesture-voice-ai-assistant
</pre>

<h3>2. Install dependencies</h3>

<pre>
pip install -r requirements.txt
</pre>

<h3>3. Add API Key</h3>

<p>Create a <code>.env</code> file in root:</p>

<pre>
WEATHER_API_KEY=your_api_key_here
</pre>

<h3>4. Run the project</h3>

<pre>
python main.py
</pre>

<hr>


## 📂 Project Structure

<pre>
gesture-voice-ai-assistant/
│
├── 📁 <a href="./config/">config/</a>
│   ├── 📄 <a href="./config/__init__.py">__init__.py</a>
│   ├── 📄 <a href="./config/config.example.env">config.example.env</a>
│   └── 📄 <a href="./config/settings.py">settings.py</a>
│
├── 📁 <a href="./features/">features/</a>
│   ├── 📄 <a href="./features/__init__.py">__init__.py</a>
│   ├── 📄 <a href="./features/apps.py">apps.py</a>
│   ├── 📄 <a href="./features/browser.py">browser.py</a>
│   └── 📄 <a href="./features/weather.py">weather.py</a>
│
├── 📁 <a href="./gesture/">gesture/</a>
│   ├── 📄 <a href="./gesture/__init__.py">__init__.py</a>
│   └── 📄 <a href="./gesture/gesture_control.py">gesture_control.py</a>
│
├── 📁 <a href="./voice/">voice/</a>
│   ├── 📄 <a href="./voice/__init__.py">__init__.py</a>
│   ├── 📄 <a href="./voice/assistant.py">assistant.py</a>
│   ├── 📄 <a href="./voice/speech.py">speech.py</a>
│   └── 📄 <a href="./voice/tts.py">tts.py</a>
│
├── 📄 <a href="./.gitignore">.gitignore</a>
├── 📄 <a href="./README.md">README.md</a>
├── 📄 <a href="./main.py">main.py</a>
└── 📄 <a href="./requirements.txt">requirements.txt</a>
</pre>

<hr>



<h2>👨‍💻 Author</h2>
<p>Hey, I'm Sunidhi Singh — focused on building practical AI and automation systems for real-world use.</p>
<p>📧 Connect with me on 
<a href="https://www.linkedin.com/in/sunidhi-singh-4aa45233b" target="_blank">
LinkedIn
</a>

</p>

<hr>
