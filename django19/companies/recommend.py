from sklearn.decomposition import LatentDirichletAllocation
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from collections import Counter
from sklearn.metrics.pairwise import cosine_similarity
from scipy import spatial




def getTermFrequency(documents, no_features):
    tf_vectorizer = CountVectorizer(max_df=0.95, min_df=2, max_features=no_features, stop_words='english')
    tf = tf_vectorizer.fit_transform(documents)
    tf_feature_names = tf_vectorizer.get_feature_names()
    return [tf, tf_feature_names]


def display_topics(model, feature_names, no_top_words):
    for topic_idx, topic in enumerate(model.components_):
        print("Topic %d:" % (topic_idx))
        print(" ".join([feature_names[i]
                        for i in topic.argsort()[:-no_top_words - 1:-1]]))


no_topics = 10
no_features = 100

def getDocuments():
    with open('description.txt','r') as file:
        lines = file.readlines()
    return lines



def getTermFrequencyFromFeatures(resume_text, no_features, tf_feature_names):
    words = resume_text.split(" ")
    count = Counter(words)
    idx = 0
    tf = np.zeros(len(tf_feature_names))
    for feature in tf_feature_names:
        print(feature)
        print("\n")
        print(count[feature])
        tf[idx] = count[feature]
        idx  = idx+1
    return tf


documents = getDocuments()
docs = documents[0:8]

[tf, tf_feature_names] = getTermFrequency(documents=docs, no_features=no_features)
lda = LatentDirichletAllocation(n_topics=no_topics, max_iter=5, learning_method='online', learning_offset=50.,
                                random_state=0).fit(tf)

doc_desc_mat = [lda.transform(doc_tf) for doc_tf in tf]

doc_desc_mat = np.reshape(doc_desc_mat, (8, 10))
topic_word_mat = lda.components_

print(len(topic_word_mat))

topicWordMat = np.reshape(topic_word_mat, (10,27))



doc = documents[7]

doc_tf = getTermFrequencyFromFeatures(doc, no_features, tf_feature_names)
doc_tf = np.reshape(doc_tf, (27,1))
reuslt_vec = np.matmul(topicWordMat,doc_tf)


compare_vec = doc_desc_mat[0]


result_vector = reuslt_vec.flatten().tolist()
compare_vector = compare_vec.flatten().tolist()


print((result_vector))
print((compare_vector))
consine = cosine_similarity(result_vector, compare_vector)



dataSetI = [3, 45, 7, 2]
dataSetII = [2, 54, 13, 15]
result = 1 - spatial.distance.cosine(np.asarray(result_vector,(10,1)), np.reshape(compare_vector,(10,1)))


print("cosine similarity %s" %str(result))




