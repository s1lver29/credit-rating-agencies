import string

import nltk
from natasha import Doc, MorphVocab, NewsEmbedding, NewsMorphTagger, NewsNERTagger, Segmenter
from nltk.corpus import stopwords

nltk.download("punkt")
nltk.download("stopwords")
segmenter = Segmenter()
morph_vocab = MorphVocab()
emb = NewsEmbedding()
morph_tagger = NewsMorphTagger(emb)
ner_tagger = NewsNERTagger(emb)

stop_words = set(stopwords.words("russian"))
punct = string.punctuation

stop_words.update(
    [
        "млн",
        "млрд",
        "руб",
        "год",
        "тыс",
        "январь",
        "февраль",
        "март",
        "апрель",
        "май",
        "июнь",
        "июль",
        "август",
        "сентябрь",
        "октябрь",
        "ноябрь",
        "декабрь",
    ]
)


def pr_web_scrap_cleaner(pr):
    """
    Очищает пресс-релиз от артефактов веб-скраппинга
    """
    if "Эксперт РА" in pr:
        pr = pr[: pr.find("Контакты для СМИ:")]
    elif "АКРА" in pr:
        pr = pr[: pr.lower().rfind("факторы")]
    elif "НКР" in pr:
        pr = pr[pr.lower().find("обоснование рейтингового действия") :]
        pr = pr[: pr.lower().rfind("регуляторное раскрытие")]
    return pr


cyrillic_letters = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"


def has_latin_letters_or_numbers(word: str):
    """
    Проверяем наличие латинских символов
    """
    return any(char not in cyrillic_letters for char in word)


def pr_preprocessing(pr_text, stop_words, punct, segmenter, morph_tagger, ner_tagger, morph_vocab):
    """
    Очищает текст от пунктуации, мусорных символов, латинских слов, организация и некоторых стоп-слов,
    лемматизует и приводит к нижнему регистру
    """
    sentences = nltk.sent_tokenize(pr_text)
    sentences_cleaned = []
    for sent in sentences:
        doc = Doc(sent)
        doc.segment(segmenter)
        doc.tag_morph(morph_tagger)
        doc.tag_ner(ner_tagger)
        for token in doc.tokens:
            token.lemmatize(morph_vocab)
        org_and_loc = {token.text for span in doc.spans for token in span.tokens}
        words = [
            token.lemma
            for token in doc.tokens
            if (token.text not in org_and_loc)
            and (token.text not in stop_words)
            and (not has_latin_letters_or_numbers(token.text))
            and (token.text not in punct)
            and len(token.text) > 2
        ]
        sentences_cleaned.append(" ".join(words))
    return ". ".join(sentences_cleaned)


def main_preprocessing(text: str):
    pr_orig = pr_web_scrap_cleaner(text)
    pr_cleaned = pr_preprocessing(
        pr_orig, stop_words, punct, segmenter, morph_tagger, ner_tagger, morph_vocab
    )

    return pr_cleaned, pr_orig
