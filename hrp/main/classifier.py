import torch
from transformers import BertTokenizer, BertForSequenceClassification


class HRClassifier:
    def __init__(self, model_path, tokenizer_path):
        self.tokenizer = BertTokenizer.from_pretrained(tokenizer_path)
        self.model = BertForSequenceClassification.from_pretrained('bert-base-uncased')
        self.model.load_state_dict(torch.load(model_path, map_location=torch.device('cpu')))
        self.model.eval()

    def predict(self, text):
        inputs = self.tokenizer(text, return_tensors='pt', padding=True, truncation=True, max_length=128)
        with torch.no_grad():
            outputs = self.model(**inputs)
        logits = outputs.logits
        predicted_class_id = torch.argmax(logits, dim=1).item()
        return predicted_class_id


# Instantiate the classifier with paths to your saved model and tokenizer
classifier = HRClassifier(model_path='C:\Users\DELL\Documents\task_internship\hr_newsline_classifier', tokenizer_path='C:\Users\DELL\Documents\task_internship\tokenizer')
