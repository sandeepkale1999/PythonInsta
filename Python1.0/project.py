from sklearn.feature_extraction.text import CountVectorizer
text = ['She is good','I am good', 'He is not good']
cv = CountVectorizer()
cv.fit(text)
print(cv.vocabulary_)
vector = cv.transform(text)
print(vector)
print(vector.toarray())