# 📄 Data Extraction and Analysis
## 📌 Project Overview
This project involves extracting data from a given set of URLs, analyzing the textual content using NLP (Natural Language Processing) techniques, and generating multiple linguistic and readability metrics. The final output is a structured CSV file containing scores and statistics for each URL.

## 🧠 Objectives
- Extract web page content using URLs provided in an Excel file.

- Perform text processing and generate individual text files per URL.

- Calculate various sentiment and readability metrics.

- Store results in a final structured CSV file for easy interpretation and reporting.

## 🛠️ Technologies Used
- Python

- pandas, openpyxl (for Excel handling)

- os, re (for file and regex handling)

- nltk (for NLP-based scoring)

- custom modules (for specific metrics)

## 🗂️ Workflow Summary
1. TextFiles.py
- Reads input.xlsx containing url_id and url.

- Extracts content from each URL and saves it into separate text files.

- Filenames are based on the corresponding url_id.

2. Text Analysis
- Each .txt file is processed to extract the following metrics:

- POSITIVE SCORE

- NEGATIVE SCORE

- POLARITY SCORE

- SUBJECTIVITY SCORE

- AVG SENTENCE LENGTH

- PERCENTAGE OF COMPLEX WORDS

- FOG INDEX

- AVG NUMBER OF WORDS PER SENTENCE

- COMPLEX WORD COUNT

- WORD COUNT

- SYLLABLE PER WORD

- PERSONAL PRONOUNS

- AVG WORD LENGTH

3. Final CSV Generation
- Results for each text file are stored in a master CSV file with the structure:

4. Organizing Text Files
- A Python script is used to move all generated .txt files into a single organized folder named TextFiles.

## ▶️ How to Run
1. Clone the repository:
git clone https://github.com/your-username/data-extraction-analysis.git
cd data-extraction-analysis

2. Install dependencies:
pip install -r requirements.txt

3. Run the TextFiles.py script:
python TextFiles.py

4. Run the metric calculation script:
python text_analysis.py

5. Check output.csv for final results.

## 🔮 Future Enhancements
- Add automated URL content extraction using requests and BeautifulSoup.

- Integrate GUI to input URLs and display metrics.

- Extend analysis using advanced sentiment analysis tools like VADER or TextBlob.

📬 Contact
For questions or collaboration, feel free to connect via [maheshgoud3110@gmail.com].
