import os
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split

# 读取问题文本
with open('question_1.txt', 'r', encoding='utf-8') as file:
    question_text = file.read()

# 读取答案文本
with open('answer_1.txt', 'r', encoding='utf-8') as file:
    answer_text = file.read()

# 创建一个包含文本内容和对应标签的数据集
texts = [question_text, answer_text]
labels = ['提问', '回答']

# 数据预处理和特征提取
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(texts)

# 创建标签对应的数组
y = labels

# 数据分割为训练集和测试集
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 创建朴素贝叶斯分类器
classifier = MultinomialNB()

# 训练分类器
classifier.fit(X_train, y_train)

# 模型训练完成，现在可以应用该模型进行分类
with open('unknown_1.txt', 'r', encoding='utf-8') as file:
    unknown_text = file.read()
predicted_label = classifier.predict([unknown_text])

print("未知文本的分类结果:", predicted_label[0])