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
    
    def split_into_sentences(self, to_be_split: Union[str, List[str]]) -> List[str]:
        """
        Split a larger text into sentences using TextBlob (NLTK's PunktSentTokenizer).
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
    
    def process_text(self, text: Union[str, List[str]]):
        """
        Call the SPaR.txt API, expecting {"texts": original_input, "sentences": List[str], "predictions": List[Dict[str, str]]}
        """
        response = requests.post(self.api,  json={"texts": text}).json()
        # texts = response['texts']
        sentences = response['sentences']
        predictions = response['predictions']
        
        return sentences, predictions
        
        