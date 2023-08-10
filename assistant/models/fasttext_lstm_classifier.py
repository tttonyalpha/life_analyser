import torch
import torch.nn as nn
import torch.optim as optim
import torch.utils.data as data
import numpy as np
import pandas as pd


class LSTMClassifier(nn.Module):
    def __init__(self, input_size, hidden_size, num_classes):
        super(LSTMClassifier, self).__init__()
        self.hidden_size = hidden_size
        self.lstm = nn.LSTM(input_size, hidden_size, batch_first=True)
        self.hidden = nn.Linear(hidden_size, hidden_size)
        self.fc = nn.Linear(hidden_size, num_classes)

    def forward(self, x):
        h0 = torch.zeros(1, x.size(0), self.hidden_size).to(device)
        c0 = torch.zeros(1, x.size(0), self.hidden_size).to(device)
        out, _ = self.lstm(x, (h0, c0))
        out = self.hidden(out[:, -1, :])
        out = torch.nn.ReLU()(out)
        out = self.hidden(out)
        out = self.fc(out)
        return out


class ActivityDataset(data.Dataset):
    def __init__(self, dataframe, ft_model, max_length=20):
        self.data = dataframe
        self.ft_model = ft_model
        self.max_length = max_length

    def __getitem__(self, index):
        activity = self.data.iloc[index]['activity_name']
        encoded_activity_type = self.data.iloc[index]['encoded_activity_type']

        tokens = activity.split()
        embeddings = []
        for token in tokens:
            embedding = self.ft_model.get_word_vector(token)
            embeddings.append(embedding)
        embeddings = np.array(embeddings)

        if embeddings.shape[0] < self.max_length:
            pad_length = self.max_length - embeddings.shape[0]
            embeddings = np.pad(
                embeddings, [(0, pad_length), (0, 0)], mode='constant')
        elif embeddings.shape[0] > self.max_length:
            embeddings = embeddings[:self.max_length, :]

        return torch.FloatTensor(embeddings), encoded_activity_type

    def __len__(self):
        return len(self.data)


device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

fasttext_path = '/content/drive/MyDrive/PROJECTS_COMPETITIONS/life_analyser/fasttext-en/model.bin'
ft_model = fasttext.load_model(fasttext_path)

input_size = ft_model.get_dimension()
hidden_size = 128
num_classes = 11
batch_size = 32
num_epochs = 70
learning_rate = 0.001
test_size = 0.2

train_data, val_data = train_test_split(
    df, test_size=test_size, random_state=random_state)


train_dataset = ActivityDataset(train_data, ft_model)
val_dataset = ActivityDataset(val_data, ft_model)
train_loader = data.DataLoader(
    train_dataset, batch_size=batch_size, shuffle=True)
val_loader = data.DataLoader(val_dataset, batch_size=batch_size, shuffle=False)

model = LSTMClassifier(input_size, hidden_size, num_classes).to(device)

criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters(), lr=learning_rate)


for epoch in range(num_epochs):
    model.train()
    total_loss = 0
    correct = 0
    total = 0
    for embeddings, labels in train_loader:
        embeddings = embeddings.to(device)
        labels = labels.to(device)

        optimizer.zero_grad()

        outputs = model(embeddings)

        loss = criterion(outputs, labels)
        loss.backward()
        optimizer.step()

        total_loss += loss.item()

        _, predicted = torch.max(outputs.data, 1)
        total += labels.size(0)
        correct += (predicted == labels).sum().item()

    train_loss = total_loss / len(train_loader)
    train_accuracy = 100 * correct / total

    model.eval()
    val_loss = 0
    val_correct = 0
    val_total = 0
    with torch.no_grad():
        for embeddings, labels in val_loader:
            embeddings = embeddings.to(device)
            labels = labels.to(device)

            outputs = model(embeddings)
            loss = criterion(outputs, labels)

            val_loss += loss.item()

            _, predicted = torch.max(outputs.data, 1)
            val_total += labels.size(0)
            val_correct += (predicted == labels).sum().item()

    val_loss = val_loss / len(val_loader)
    val_accuracy = 100 * val_correct / val_total

    print('Epoch [{}/{}], Train Loss: {:.4f}, Train Accuracy: {:.2f}%, Val Loss: {:.4f}, Val Accuracy: {:.2f}%'
          .format(epoch + 1, num_epochs, train_loss, train_accuracy, val_loss, val_accuracy))


predictions = []
with torch.no_grad():
    for embeddings, labels in val_loader:
        embeddings = embeddings.to(device)
        labels = labels.to(device)

        outputs = model(embeddings)
        _, predicted = torch.max(outputs.data, 1)

        predictions.extend(predicted.tolist())

true_labels = val_dataset.data['encoded_activity_type'].tolist()
f1_score = f1_score(true_labels, predictions, average='weighted')
accuracy = accuracy_score(true_labels, predictions)

print("F1 Score: {:.4f}".format(f1_score))
print("Accuracy: {:.2f}%".format(accuracy * 100))
