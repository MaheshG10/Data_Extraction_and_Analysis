#importing excel file
import pandas as pd
df=pd.read_excel('Input.xlsx')
#print(df)
# print(df)
# #Creating .txt files
import requests
from bs4 import BeautifulSoup
for i, row in df.iterrows():

#Get the URL_ID and URL from the current row

    url_id = row['URL_ID']
    url = row['URL']
    
    # Make a GET request to the URL and parse the HTML content using BeautifulSoup
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    
    # Find the article title and text using their HTML tags
    try:
      title = soup.find('h1').get_text().strip()
    except AttributeError:
      title = 'Untitled Article'
    article_text = '\n'.join([p.get_text().strip() for p in soup.find_all('p')])
    
    # Save the article text in a text file with URL_ID as the file name
    with open(f'{url_id}.txt', 'w', encoding='utf-8') as f:
        f.write(title + '\n\n')
        f.write(article_text)
        print(f"Creating {url_id}.txt file is done ✅")



#Creating CSV file
import re,requests,csv
from bs4 import BeautifulSoup
import pandas as pd
headers=["URL_ID",'URL'
    ,'POSITIVE SCORE',
      'NEGATIVE SCORE',
      'POLARITY SCORE',
      'SUBJECTIVITY SCORE',
      'AVG SENTENCE LENGTH',
      'PERCENTAGE OF COMPLEX WORDS',
      'FOG INDEX',
      'AVG NUMBER OF WORDS PER SENTENCE',
      'COMPLEX WORD COUNT',
      'WORD COUNT',
      'SYLLABLE PER WORD',
      'PERSONAL PRONOUNS','AVG WORD LENGTH']

filename = "Output_Data_structure.csv"
input_df = pd.read_excel('Input.xlsx')
with open(filename, 'w', newline='') as csvfile:
  csvwriter = csv.writer(csvfile)
  csvwriter.writerow(headers)
  for index, row in input_df.iterrows():
    try:
      url_id = row['URL_ID']
      url = row['URL']

      # Send a GET request to the URL and get the HTML content
      response = requests.get(url)
      
      # Use BeautifulSoup to parse the HTML content
      soup = BeautifulSoup(response.content, 'html.parser')
      
      # Find the article text and remove any unnecessary characters
      article_tag = soup.find('article')
      if article_tag:
          article_text = article_tag.get_text().strip()
      else:
          article_text = ''
      # for p in soup.find_all('p'):
      #     article_text += p.text

      # Define lists of positive and negative words
      with open('positive-words.txt', 'r') as file:
          ptext = file.read()
      positive_words=ptext.split()
      with open('negative-words.txt', 'r') as file:
          ntext = file.read()
      negative_words =ntext.split()

      # Split the article text into individual words
      text = article_text
      words=text.split()
      # Calculate the number of positive and negative words in the text
      positive_count = sum([1 for word in words if word in positive_words])
      negative_count = sum([1 for word in words if word in negative_words])
      #words=article_tag.get_text().strip().split()
      # Calculate the polarity score
      if positive_count + negative_count != 0:
          polarity_score = (positive_count - negative_count) / (positive_count + negative_count)
      else:
          polarity_score = 0

      # Calculate the total number of words in the text
      word_count = len(words)

      # Calculate the number of complex words in the text
      syllable_count = 0
      complex_word_count = 0
      for word in words:
          syllable_count += len(re.findall('(?!e$)[aeiouy]+', word))
          if len(re.findall('(?!e$)[aeiouy]+', word)) >= 3:
              complex_word_count += 1

      # Calculate the percentage of complex words in the text
      complex_word_percentage = complex_word_count / word_count * 100

      # Calculate the Fog index
      avg_sentence_length = word_count / len(soup.find_all('p'))
      # Calculate the subjectivity score
      subjective_words = ['i', 'you', 'he', 'she', 'it', 'we', 'they', 'me', 'him', 'her', 'us', 'them', 'my', 'your', 'his', 'her', 'its', 'our', 'their', 'mine', 'yours', 'hers', 'theirs']
      subjective_count = sum([1 for word in words if word in subjective_words])
      objective_count = word_count - subjective_count
      subjectivity_score = subjective_count / (subjective_count + objective_count)

      # Calculate the average word length
      total_word_length = sum([len(word) for word in words])
      avg_word_length = total_word_length / word_count

      # Calculate the number of personal pronouns in the text
      personal_pronouns = sum([1 for word in words if word in ['i', 'you', 'he', 'she', 'it', 'we', 'they', 'me', 'him', 'her', 'us', 'them', 'my', 'your', 'his', 'her', 'its', 'our', 'their', 'mine', 'yours', 'hers', 'theirs']])
      fog_index=0.4*(avg_sentence_length+complex_word_percentage)
      # print("Fog index: ",fog_index)
      #Average Number of Words Per Sentence = the total number of words / the total number of sentences
      avg_words_per_sentence = avg_sentence_length / word_count
      # print("Avg words per sentence:",avg_words_per_sentence)
      #Complex WC
      cwc=complex_word_count
      # print("Complex Word count:",complex_word_count)
      # #WC
      # print("Word Count:",word_count)
      import re
      def syllable_count(word):
          word = word.lower()
          count = 0
          vowels = "aeiouy"
          if word[0] in vowels:
              count += 1
          for index in range(1, len(word)):
              if word[index] in vowels and word[index - 1] not in vowels:
                  count += 1
          if word.endswith("e"):
              count -= 1
          if count == 0:
              count += 1
          return count
      # print("Syllable Count:",(syllable_count(text)))
      #personal pronouns
      def count_personal_pronouns(text):
          # Define the regular expression to match personal pronouns
          pronoun_regex = r'\b(I|we|my|ours|us)\b'

          # Exclude instances of "US" in the text
          excluded_text = re.sub(r'\bUS\b', '', text)

          # Find all matches of personal pronouns in the text
          matches = re.findall(pronoun_regex, excluded_text)

          # Return the count of personal pronouns
          return len(matches)
      # print("Personal pronoun:",count_personal_pronouns(text))
      # print("Avg Word Length:",len(text)/word_count)

      fin_arr = [url_id,url,positive_count,
        negative_count,
        polarity_score,
        subjectivity_score,
        avg_sentence_length,
        complex_word_percentage,
        fog_index,
        avg_words_per_sentence,
        complex_word_count,
        word_count,
        syllable_count(text),
        count_personal_pronouns(text),len(text)/word_count]
      # print(fin_arr)
      print(f"Working on {url_id} is done ✅")
      csvwriter.writerow(fin_arr)
    except:pass