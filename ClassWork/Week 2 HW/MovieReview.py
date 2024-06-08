import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
from keras.models import Sequential
from keras.layers import Embedding, LSTM, Dense, Dropout
from keras.utils import to_categorical

# Load dataset
url = "https://raw.githubusercontent.com/laxmimerit/IMDB-Movie-Reviews-Large-Dataset-50k/master/train_data.csv"
df = pd.read_csv(url)

# Preprocess labels
def categorize_sentiment(sentiment):
    if sentiment == 'positive':
        return 1
    elif sentiment == 'negative':
        return 0
    else:
        return 2

df['sentiment'] = df['sentiment'].apply(categorize_sentiment)

# Tokenization and Padding
max_words = 5000
max_len = 100

tokenizer = Tokenizer(num_words=max_words)
tokenizer.fit_on_texts(df['review'])
sequences = tokenizer.texts_to_sequences(df['review'])
padded_sequences = pad_sequences(sequences, maxlen=max_len)

# Split data
X_train, X_test, y_train, y_test = train_test_split(padded_sequences, df['sentiment'], test_size=0.2, random_state=42)

# Encode labels
encoder = LabelEncoder()
y_train = to_categorical(encoder.fit_transform(y_train), num_classes=3)
y_test = to_categorical(encoder.transform(y_test), num_classes=3)

# Building the model
model = Sequential()
model.add(Embedding(max_words, 128, input_length=max_len))
model.add(LSTM(64, dropout=0.2, recurrent_dropout=0.2))
model.add(Dense(3, activation='softmax'))

model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
model.summary()

# Training the model
history = model.fit(X_train, y_train, epochs=5, batch_size=32, validation_split=0.2)

# Evaluating the model
loss, accuracy = model.evaluate(X_test, y_test)
print(f'Test Accuracy: {accuracy*100:.2f}%')

# Making predictions
def predict_sentiment(review):
    sequence = tokenizer.texts_to_sequences([review])
    padded = pad_sequences(sequence, maxlen=max_len)
    pred = model.predict(padded)
    sentiment = np.argmax(pred, axis=1)[0]
    return encoder.inverse_transform([sentiment])[0]

# Example reviews
positive_review = "This film is a masterpiece of storytelling, featuring exceptional performances by the cast. The cinematography is stunning, and the direction is impeccable. It's a deeply emotional experience that will leave you thinking long after the credits roll. Highly recommend to anyone looking for a powerful and moving cinematic journey."
negative_review = "This movie was a huge disappointment. The plot was incoherent, and the characters were poorly developed. The special effects looked cheap, and the dialogue was cringeworthy. It felt like a waste of time and money. I wouldn't recommend this to anyone."
neutral_review = "The movie had its moments of brilliance, with some well-executed scenes and decent acting. However, it struggled with pacing issues, and some parts felt dragged out. It's an average film that might appeal to fans of the genre but doesn't stand out as particularly memorable or groundbreaking."

print("Positive Review Sentiment:", predict_sentiment(positive_review))
print("Negative Review Sentiment:", predict_sentiment(negative_review))
print("Neutral Review Sentiment:", predict_sentiment(neutral_review))
