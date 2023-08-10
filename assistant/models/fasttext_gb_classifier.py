
import fasttext


fasttext_path = '/content/drive/MyDrive/PROJECTS_COMPETITIONS/life_analyser/fasttext-en/model.bin'
ft_model = fasttext.load_model(fasttext_path)

from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.metrics import f1_score, accuracy_score


def get_embedding(text):
    tokens = text.lower().split()
    embeddings = [model.get_word_vector(token) for token in tokens]
    return np.mean(embeddings, axis=0)


X = df.activity_name.apply(get_embedding).tolist()
y = df.encoded_activity_type.tolist()


gb_model = GradientBoostingClassifier()
gb_model.fit(X_train, y_train)

y_pred = gb_model.predict(X_val)

f1_score_val = f1_score(y_val, y_pred, average='micro')
accuracy_val = accuracy_score(y_val, y_pred)

print("F1 Score on Validation Set:", f1_score_val)
print("Accuracy on Validation Set:", accuracy_val)
