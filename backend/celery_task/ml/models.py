import torch
from transformers import BertForSequenceClassification, BertTokenizer

model = BertForSequenceClassification.from_pretrained(
    "./celery_task/ml/models/rubert-tiny2", num_labels=7, max_length=2048
)
tokenizer = BertTokenizer.from_pretrained("./celery_task/ml/models/rubert-tiny2", max_length=2048)

def predict_rating_model_bert(text: str):
    text_tokenizer = tokenizer(text, padding=True, truncation=True, return_tensors="pt", max_length=2048)
    with torch.no_grad():
        output = model(**{k: v.to(model.device) for k, v in text_tokenizer.items()})

        logits = output.logits.detach().cpu()
        predictions = torch.argmax(logits, dim=-1).numpy()[0]

    return model.config.id2label[predictions]
