# Utilising-MapReduce-Technology
Developing a Naïve Search Engine Utilising MapReduce  Technology
i19-1864_22i-1969_22i-1860_Usama_Bin_Sajid_Mujahid Abbas_DanishA1
Word_enum_mapper Implementation:
Using the word tokenize function, the script turns input text lines into words by utilizing the Natural Language Toolkit (NLTK) package.
It goes over every line of text input that is received from standard input once.
It tokenizes the text for every line, generating a key-value pair for every word (the word itself as the key, and 1 as the value).

Word_enum_reducer Implementation:
The script reads key-value pairs words as the key and the number of occurrences as the value using standard input.
It maintains a running total of the counts for each word encountered.
When the script encounters a new word, it emits the accumulated count for the previous word along with the word itself.
The reducer script outputs the final list of unique words along with their frequencies. 

Doc_count_mapper Interpretation:
The mapper reads input lines, expects at least four fields separated by commas, and extracts the article ID and section text.
 It tokenizes the section text into words using NLTK's word_tokenize function.
 It converts the words to lowercase and removes duplicates to obtain unique words.
For each unique word, it emits the word along with the corresponding article ID.

Doc_count_reducer Interpretation:
 The reducer aggregates the counts of documents for each word emitted by the mapper.
 It expects lines with a word and an article ID separated by a tab.
 It maintains a current word variable to keep track of the word being processed.
 It initializes a set to store unique article IDs for each word.
 For each input line, it aggregates the document counts for each word.
 When encountering a new word, it outputs the count of documents for the previous word.
 It outputs the final count for the last word encountered.

Indexer_mapper Implementation:
The mapper script, preprocesses input data and generates intermediate key-value pairs. Key points about the mapper implementation:
For every word in the text, it determines the term frequency (TF).

Indexer_reducer Implementation:
The reducer script,  aggregates intermediate results and computes the TF-IDF values. Key points about the reducer implementation:
It receives intermediate key-value pairs from the mapper.
It aggregates term frequencies for each word across documents.
For every word in every document, it computes the TF-IDF and the inverse document frequency .

Query_mapper Implementation:
Using the word tokenize function from NLTK, the mapper script tokenizes input text, making all words lowercase for consistency. The mapper returns a key-value pair for each word in the input text, where the word itself is the key and the value is set to 'query'.

Query_reducer Implementation:
Entries marked as "query" are filtered out by the reducer script, which aggregates word occurrences for every document. After that, it creates a dictionary structure using the pertinent terms for every document. The reducer outputs a key-value pair for each document, where the key is the document ID and the value is a list of terms that are discovered in the document separated by commas.

Article_data_mapper Interpretation:
It explains the role of the mapper in the data processing pipeline.
It explains the incoming data's format as well as the mapper's procedure for parsing and extracting relevant info.
Drawing attention to any filtering or preprocessing that the  mapper did.
Talk about the mapper's output format and how it gets the data ready for additional processing.

Article_data_reducer Interpretation:
Describe the reducer's function in the pipeline for data processing.
Explain the method by which the reducer gets and uses the data that the mapper emits.
Talk about any summarizing or aggregate work the reducer has done.
Describe the reducer's output format and how it completes the data processing process.
