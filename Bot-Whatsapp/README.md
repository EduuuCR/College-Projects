
## Installation and Setup


1. **Download Node.js and on the terminal use:**:
```bash
node -v
npm -v
```
2. **Create a folder for the project:**
```bash
mkdir bot-whatsapp-stickers
cd bot-whatsapp-stickers
npm init -y
```
3. **Install the required libraries:**
```bash
npm install whatsapp-web.js qrcode-terminal
```

4. **Run on the terminal:**
```bash
node index.js
```

**OBS: Messaging practice test**

Risk Interval Observations
```bash
2000ms (2 seg)	-   Safe	  -   Ideal for lightweight bots
1000ms (1 seg)	-  Moderate	-   Works well, but be careful with the volume
500ms	     -        High	  -   Can lead to quick ban
< 300ms    -    	Very High	-   WhatsApp may disconnect or ban you
```
