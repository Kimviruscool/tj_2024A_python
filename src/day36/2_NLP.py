#2_NLP.py

#텐서플로 토크나이저
from tensorflow.keras.preprocessing.text import Tokenizer
sentences = [
    '영실이는 나를 정말 정말 좋아해',
    '영실이는 영화를 좋아해'
]
#객체 생성
tokenizer = Tokenizer()
tokenizer.fit_on_texts(sentences) #.fit_on_texts(문장목록)
print("단어 인덱스 :",tokenizer.word_index) #문장에서 문자들을 인덱스와 매칭 한다. # 단어 사전
#단어 인덱스 : {'영실이는': 1, '정말': 2, '좋아해': 3, '나를': 4, '영화를': 5}

#인코딩된 결과
word_encoding = tokenizer.texts_to_sequences(sentences)
print(word_encoding)
#[[1, 4, 2, 2, 3], [1, 5, 3]]

#사전에 없는 단어가 있을 때 인코딩 결과
new_sentences = ['영실이는 경록이와 나를 좋아해']
new_word_encoding = tokenizer.texts_to_sequences(new_sentences)
print(new_word_encoding)
#[[1, 4, 3]]

#사전에 없는(Out of Vocabulary) 단어 처리
#새로운 단어 처리방법 # 앞전 사전에 등록되지 않는 단어들은 <OOV> 표현한다.
tokenizer = Tokenizer(oov_token="<OOV>")
tokenizer.fit_on_texts(sentences)
word_index = tokenizer.word_index

new_word_encoding = tokenizer.texts_to_sequences(new_sentences)

print(word_index)
print(new_word_encoding)
#{'<OOV>': 1, '영실이는': 2, '정말': 3, '좋아해': 4, '나를': 5, '영화를': 6}
# [[2, 1, 5, 4]]

#단어 사전 개수 설정
#새로운 단어 처리방법 # 최대 개수 외 단어들은 <OOV> 표현한다.
tokenizer = Tokenizer(num_words=3,oov_token="<OOV>")
tokenizer.fit_on_texts(sentences)
word_index = tokenizer.word_index

new_word_encoding = tokenizer.texts_to_sequences(new_sentences)

print(word_index)
print(new_word_encoding)
# {'<OOV>': 1, '영실이는': 2, '정말': 3, '좋아해': 4, '나를': 5, '영화를': 6}
# [[2, 1, 1, 1]]

#문장 길이 맞추기
from tensorflow.keras.preprocessing.sequence import pad_sequences
padded = pad_sequences(word_encoding)
print(padded)

#패딩 뒤에 0 붙이기
padded = pad_sequences(word_encoding,padding='post')
print(padded)
# [[1 4 2 2 3]
#  [1 5 3 0 0]]

#문장의 최대 길이 고정
padded = pad_sequences(word_encoding,padding='post',maxlen=4)
print(padded)
# [[4 2 2 3]
#  [1 5 3 0]]

#최대 길이보다 문장이 길 때 뒷부분 자르기
padded = pad_sequences(word_encoding, padding='post',truncating='post',maxlen=4)
print(padded)
# [[1 4 2 2]
#  [1 5 3 0]]

