<h1>✈️ Flight Deal Tracker</h1>

<p>A program that monitors flight prices and sends notifications when deals are found below your target price.</p>

<h2>📋 Project Overview</h2>

<p>This project uses a Google spreadsheet to track cities you want to visit along with your maximum price for each destination. The program automatically checks flight prices and notifies you via text and email when it finds a deal cheaper than your target price.</p>

<p>For example, if you set London at $400 as your max, you'll get notified the moment a flight drops below that price.</p>

<h2>🏗️ Project Structure</h2>

<p>Built using OOP principles across multiple modules:</p>

<ul>
<li><strong>main.py</strong> - Orchestrates all the classes and handles the main program flow</li>
<li><strong>data_manager.py</strong> - Manages communication with Google Sheets via Sheety API</li>
<li><strong>flight_search.py</strong> - Handles all flight API interactions</li>
<li><strong>notification_manager.py</strong> - Sends text and email notifications when deals are found</li>
</ul>

<h2>🔧 API Choices & Challenges</h2>

<h3>Why Two Different Flight APIs?</h3>

<p>I ended up using two separate flight APIs because no single API provided everything I needed:</p>

<ul>
<li><strong>Amadeus API</strong> - Used for retrieving IATA city codes. Their authentication and city search endpoints work great, and it was straightforward to get the codes I needed to populate the spreadsheet.</li>
<li><strong>Kiwi API (via RapidAPI)</strong> - Used for actual flight price searches. The original course recommended using Amadeus for this too, but their flight search endpoint is no longer available. After testing multiple alternatives, Kiwi had the most reliable and comprehensive flight data.</li>
</ul>

<h3>Other APIs Considered</h3>

<p>I spent days researching flight APIs. Most either had incomplete documentation, were too expensive, or didn't provide the search functionality I needed. This taught me that dealing with deprecated APIs and finding alternatives is just part of being a developer.</p>

<h3>Notification Services</h3>

<ul>
<li><strong>Vonage</strong> - Handles SMS notifications. The course originally suggested Twilio, but they now require verification for US numbers. Vonage worked as a solid alternative, though I can't use emojis in the messages.</li>
<li><strong>SMTP</strong> - Sends email notifications as a backup to texts.</li>
</ul>

<h3>Data Management</h3>

<ul>
<li><strong>Sheety API</strong> - Connects to Google Sheets. Fair warning: they only give you 200 free requests, and I burned through those quickly while testing. Ended up paying for a month because the project was too cool to abandon.</li>
</ul>

<h2>💡 Key Learnings</h2>

<p>This was the hardest project I've tackled so far, but also the most rewarding. I learned more from the struggles than I could have imagined:</p>

<ul>
<li>How to work with multiple APIs and handle their quirks</li>
<li>The reality of dealing with deprecated endpoints and finding alternatives</li>
<li>OOP principles—specifically that you call classes from main.py rather than nesting class calls within other classes. This was a huge revelation for me.</li>
<li>The importance of managing API rate limits (learned this one the expensive way)</li>
</ul>

<h2>🚀 Future Improvements</h2>

<p>I could see expanding this to track prices for other products beyond flights. The core concept of monitoring prices and alerting when they drop is super useful and could apply to anything with a price-tracking API.</p>

<hr>

<p>This project was completed as part of Day 39-40 of the 100 Days of Python course by App Brewery.</p>

