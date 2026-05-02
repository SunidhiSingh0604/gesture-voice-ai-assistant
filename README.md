
<h1>AI Gesture & Voice Assistant</h1>

<p>
Control your computer using <strong>hand gestures and voice commands</strong> — a real-time system combining computer vision and voice AI.
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

<h2>📊 Key Insights / Results</h2>

<ul>
<li>Built a <strong>real-time multimodal system</strong> combining computer vision and voice AI</li>
<li>Achieved smooth cursor control using gesture interpolation and filtering</li>
<li>Implemented <strong>event-driven multithreading</strong> for parallel execution</li>
<li>Reduced dependency on physical input devices → improved accessibility use case</li>
<li>Demonstrates practical integration of <strong>AI and system automation</strong></li>
</ul>

<hr>

<h2>🖼️ Screenshots / Dashboard Preview</h2>

<p>Add these (VERY IMPORTANT):</p>

<ul>
<li>Gesture controlling mouse</li>
<li>Voice command execution</li>
<li>Weather output</li>
</ul>

<pre>
assets/
   demo/demo.gif
   screenshots/demo_preview.png
</pre>

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

<h2>📂 Project Structure</h2>

<pre>
gesture-voice-ai-assistant/
│
├── main.py
├── config/
├── features/
├── gesture/
├── voice/
├── assets/
├── requirements.txt
└── README.md
</pre>

<hr>

<h2>👩‍💻 Author</h2>

<p><strong>Sunidhi Singh</strong><br>
B.Tech CSE | Aspiring Data Analyst / Software Developer</p>

<p>
LinkedIn: https://linkedin.com/in/your-profile<br>
GitHub: https://github.com/your-username
</p>

<hr>
