# Haier Model Label System

## 1. Ye system kya karta hai
QR scan -> model list -> model par click -> mapped Haier share link khulta hai.
21 unique models, 4 sticker groups. Original 24 rows ke duplicate model names ek baar rakhe gaye hain. Blank links ko same part-code group ka link diya gaya hai. Model names aur sticker names supplied list ke hisaab se hain.

Live page: https://haier-heater-label-models.pundir-kartiksingh.chatgpt.site

Photo files Haier server par hain; is folder mein photos ki offline copies nahi hain. Photo khulna original link ki availability aur permissions par depend karta hai.

## 2. Folder mein kya hai
- website/index.html: complete website; HTML, CSS aur links ek file mein.
- data/models.csv: editable model-to-link mapping. Part codes text hain; leading zero preserve karein.
- scripts/build_page.py: CSV se website dobara banata hai.
- scripts/page-template.html: website design template.
- scripts/generate_qr.py: kisi URL ka PNG aur vector PDF QR banata hai.
- requirements-qr.txt: sirf QR generation ki Python dependencies.
- qr/haier-model-list-qr.png aur .pdf: current live page ke ready QR files.
- documents/haier-model-labels.docx: existing clickable Word copy.

Old single-photo QR files intentionally include nahi kiye: current QR model list kholta hai.

## 3. Scratch se tools aur setup
### Sabse simple: koi installation nahi
1. ZIP ko Extract All karein.
2. Haier-Model-Label-System folder kholein.
3. website/index.html ko double-click karein; Chrome/Edge/browser mein list khul jayegi.
4. Model par click karein. Haier photo link ke liye internet chahiye.

### Local server ya editing ke liye
- Python 3: official installer https://www.python.org/downloads/windows/ se install karein. Installer mein available ho to Add Python to PATH select karein.
- Browser: Edge ya Chrome.
- Editing: Notepad kaafi hai; koi code editor bhi use kar sakte hain.
- Node.js, npm, Git, database, API key aur admin PowerShell local run ke liye required nahi hain.

Normal PowerShell kholein. Extracted folder ko File Explorer mein kholkar address bar mein powershell type karke Enter karein. Isse terminal sahi folder mein khulega.

Check:
```powershell
py --version
```
Agar py command nahi milti aur python installed hai, neeche ke commands mein py ki jagah python use karein.

## 4. Computer par locally run karein
Project folder mein:
```powershell
py -m http.server 8765 --bind 127.0.0.1 --directory website
```
Browser mein http://127.0.0.1:8765 kholein. Terminal khula rakhein. Server rokne ke liye Ctrl+C.

## 5. Phone par same Wi-Fi se test
Computer aur phone same trusted Wi-Fi par hone chahiye.
```powershell
py -m http.server 8765 --bind 0.0.0.0 --directory website
```
Dusri PowerShell window mein:
```powershell
ipconfig
```
Active Wi-Fi adapter ka IPv4 Address dekhein. Example 192.168.1.25 ho to phone browser mein http://192.168.1.25:8765 kholein. Apne actual IPv4 se replace karein. Agar Windows Firewall prompt aaye to trusted private network ke liye Python access allow karein.
Phone par localhost/127.0.0.1 computer ko refer nahi karta. Server band hone ya IP badalne par local URL/QR kaam nahi karega. Corporate Wi-Fi device isolation ho to IT help chahiye ho sakti hai.

## 6. Model name ya link update karein
1. data/models.csv ka backup lein, phir Notepad/editor mein edit karein.
2. Columns model,part_code,sticker,url same rakhein.
3. New model ke liye ek row add karein. Har row mein complete URL likhein.
4. Part-code ke leading zeros preserve karein. Excel use karein to Part Code column ko Text import karein.
5. Project folder mein run karein:
```powershell
py scripts/build_page.py
```
6. Browser refresh karein. Model count aur links check karein.

Builder website/index.html overwrite karta hai. Design edits scripts/page-template.html mein karein, warna rebuild par direct HTML edits replace ho jayenge. CSV edit se Word file aur hosted page automatically update nahi hote.

## 7. Naya QR aur vector PDF banayein
Ye step optional hai; current live QR pehle se qr folder mein diya hai.
Project folder mein:
```powershell
py -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements-qr.txt
.\.venv\Scripts\python.exe scripts/generate_qr.py "https://haier-heater-label-models.pundir-kartiksingh.chatgpt.site"
```
Virtual environment activate karna zaroori nahi. Output qr/generated-qr.png aur qr/generated-qr.pdf hoga. Script re-run par generated files overwrite hoti hain; supplied current QR files unchanged rehti hain.

Local phone test ke liye URL argument mein apna http://COMPUTER-IP:8765 dein. Public use/printing ke liye permanent hosted URL use karein. file:/// path ko QR mein use na karein.

## 8. Online publish aur updates
Current live page Codex Sites par hosted hai. Local files badalne se live site nahi badalti. Isi Codex task mein updated files ke saath existing Haier Heater Labels site update/publish karne ko kahen. Existing URL same rahe to printed QR replace karna zaroori nahi. Naya host ya URL ho to naya QR generate karna hoga.

Independent hosting ke liye kisi static website host par website folder ka content upload karein; index.html public root mein hona chahiye. Phir host se mila actual public HTTPS URL QR generator ko dein. Git sirf host ke workflow ki requirement ho sakti hai; website chalane ki dependency nahi hai.

Is handover mein account credentials, tokens, .git history ya private publishing credentials nahi hain. Hosting account access alag se chahiye; ZIP se account ownership transfer nahi hoti.

## 9. Common problems
- File not found: terminal project root mein kholein, website folder ke andar nahi.
- Port already in use: 8765 ki jagah 8766 use karein aur browser URL bhi badlein.
- Page open hai lekin photo nahi: original Haier link internet ke saath directly test karein; expired/password/permission issues Haier side par fix honge.
- Phone connect nahi: same Wi-Fi, correct IPv4, running server aur firewall permission check karein.
- Word links: desktop Word mein Ctrl+Click required ho sakta hai.
- Purana QR: qr/haier-model-list-qr files current public list ke hain.

## 10. Final check before printing
Page kholein, har group ka ek model test karein, phone se QR scan karein, phir PDF print karein. QR ka white border crop na karein. PDF vector format mein hai, zoom/print par sharp rahega.
