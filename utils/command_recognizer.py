from transformers import BertTokenizer, BertForSequenceClassification

class CommandRecognizer:
    def __init__(self):
        self.tokenizer = BertTokenizer.from_pretrained('Model/classifier/bert_classifier_tokenizer')
        self.model = BertForSequenceClassification.from_pretrained('Model/classifier/bert_classifier')
        self.label_mapping = {
            'create_directory': 0,
            'create_file': 1,
            'delete': 2,
            'kill': 3,
            'show_stats': 4,
            'ml_project': 5,
            'general_project': 6}
        
    def tokenize(self, text: str):
        return self.tokenizer(text, return_tensors='pt')
    
    def predict(self, text: str):
        inputs = self.tokenize(text)
        outputs = self.model(**inputs)
        predictions = outputs.logits.argmax(dim=-1)
        label = list(self.label_mapping.keys())[predictions.item()]
        return predictions.item(), label