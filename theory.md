## Case Studies

1. Customer Service 
    - HelloFresh Freddy
2. HealthCare Chatbots
    - Haptik Covid-19 Chatbot
    - HealthTap Dr. AI
    - Melody by BaiDu (China)
3. Conversion boosters & Sales bots
    - Landbot.io: Conglomerate, Dominos, etc.
4. Travel Chatbots
    - Emirates Airline
    - Dutch Airline KLM
5. Digital Assistants
    - Alexa
    - Google Assistant
    - Siri
    - Cortana
6. Survey bots
    - Polly: Slack, Microsoft Teams, etc.
7. Legal bots
    - DoNotPay: Joshua Browder

## Transformer Based Models

1. **BERT** - Bidirectional Encoder Representations from Transformers
2. **GPT** - Generative Pre-trained Transformers

## Speech to Text

1. **MFCCs** - Mel Frequency Cepstral Coefficients: Feature extraction
2. **HMM** - Hidden Markov Models: Acoustic modeling

## NLP Pipeline

1. **Sentence Segmentation**: Splitting text into sentences
2. **Tokenization**: Splitting sentences into words
3. **Stemming**: Reducing words to their root form
4. **Lemmatization**: Reducing words to their root form based on the dictionary
5. **POS Tagging**: Assigning part of speech to each word
6. **Named Entity Recognition**: Identifying named entities in text
7. **Chunking**: Grouping words into chunks

## Stages/Levels of NLP

1. **Morphological Analysis**: Word formation
2. **Syntactic Analysis**: Sentence formation
3. **Semantic Analysis**: Meaning of the sentence
4. **Pragmatic Analysis**: Meaning of the sentence in context
5. **Discourse Analysis**: Meaning of the sentence in context of the entire document

## Ambiguity in NLP

1. **Lexical Ambiguity**: Same word, different meaning
2. **Syntactic Ambiguity**: Same sentence, different meaning
3. **Semantic Ambiguity**: Same meaning, different sentence
4. **Anaphoric Ambiguity**: Same pronoun, different meaning
5. **Pragmatic Ambiguity**: Same sentence, different meaning in context

## Hidden Markov Models

1. **Stochastic Process**: A process whose next state is dependent on the previous state
2. **Stochastic Model**: A model that uses a stochastic process
3. **Markov Assumptions**
    - Limited Horizon: The next state is dependent only on the previous state (order 1)
    - Stationarity: The probability of transition from one state to another is constant
4. **Hidden Markov Model**: A stochastic model with hidden states
5. **Hidden Markov Assumptions**
    - Limited Horizon: The next state is dependent only on the previous state (order 1)
    - Stationarity: The probability of transition from one state to another is constant
    - Output Independence: The output is independent of the previous state

## Miscelleneous

1. **Morphology**: Study of word formation
2. **Morphene**: Smallest unit of meaning
3. **Morphological Parsing**: Breaking down words into morphemes
4. **Lexican**: Collection of words
5. **Morphotactics**: Rules for combining morphemes
6. **Orthographic Rules**: Rules for spelling
7. **Free and Bound Morphemes**: Morphemes that can stand alone and those that cannot
8. **Inflectional and Derivational Morphemes**: Morphemes that change the form of a word and those that change the meaning of a word
9. **Class Changing and Class Maintaining Morphemes**: Morphemes that change the part of speech and those that do not
10. **Hyponymy**: Relationship between a general word and a specific word
11. **Hypernymy**: Relationship between a specific word and a general word
12. **Meronymy**: Relationship between a whole and its parts
13. **Synonymy**: Relationship between words with the same meaning
14. **Antonymy**: Relationship between words with opposite meanings
15. **Polysemy**: Relationship between words with multiple meanings

## Vectorization

1. BoW: Bag of Words
    - CountVectorizer
    - TfidfVectorizer: Term Frequency - Inverse Document Frequency
2. Similarity
    - Cosine Similarity
    - One Hot Vectorization

## TF-IDF

```bash
TF(w) = (Number of times w appears in a document) / (Total number of words in the document)

IDF(w) = log_e(Total number of documents / Number of documents with word w in it)

TF-IDF = TF(w) * IDF(w)
```

## Sentiment Analysis

1. **VADER**: Valence Aware Dictionary and sEntiment Reasoner
2. **TextBlob**: Python library for processing textual data