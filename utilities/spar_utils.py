from typing import List, Union
import sys
import os
import imp
import requests

from tqdm import tqdm
from pathlib import Path
from textblob import TextBlob


class NER: 
    def __init__(self, 
                 api: str = "http://localhost:8501/predict_objects/", 
                 split_length: int = 300):
        """
        
        """
        self.api = api
        self.split_length = split_length   # in number of tokens
    
    def process_sentence(self, sentence: str = ''):
        """
        """
        # SPaR doesn't handle ALL uppercase sentences well, which you might get as output from OCR    
        sentence = sentence.lower() if sentence.isupper() else sentence
        prediction_dict =  requests.post(self.api,  json={"sentence": sentence}).json()
        if not prediction_dict:
            return []

        pred_labels = prediction_dict["prediction"]
        # only returing the objects (obj) for now
        return pred_labels['obj']
    
    def split_into_sentences(self, to_be_split: Union[str, List[str]]) -> List[str]:
        """
        """
        if type(to_be_split) == str:
            if ';' in to_be_split:
                # some of the WikiData definitions contain multiple definitions separated by ';'
                to_be_split = to_be_split.split(';')
            else:
                to_be_split = [to_be_split]
            
        sentences = []
        for text in to_be_split:
            for part in text.split('\n'):
                # split into sentences using PunktSentTokenizer (TextBlob implements NLTK's version under the hood) 
                sentences += [str(s) for s in TextBlob(part.strip()).sentences if len(str(s)) > 10]
        return sentences
    
    def process_sentences(self, sentences: List[str]):
        """
        """
        spar_objects = []
        for sentence in sentences:
            # Note; we are expecting a single list of objects here!
            spar_objects += self.process_sentence(sentence)
        return spar_objects
    
    def process_text(self, text: Union[str, List[str]]):
        """
        """
        sentences = self.split_into_sentences(text)
        return self.process_sentences(sentences)
        
        