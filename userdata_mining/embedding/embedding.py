import re
from flair.data import Sentence
from flair.embeddings import TransformerDocumentEmbeddings


class Embedding:
    """
    Performs embedding on sentences.
    """

    def __init__(self, model='gpt2-medium'):
        """
        Initializes the embedding model.

        :param {str} model - The model architecture. Must be one of
        https://huggingface.co/transformers/pretrained_models.html
        """
        self.model = TransformerDocumentEmbeddings(model, batch_size=8)

    def embed(self, sentence: str) -> list:
        """
        Embeds a given sentence. If it fails, returns None.

        :param {str} sentence - A cased or uncased sentence.
        """
        if isinstance(sentence, bytes):
            sentence = sentence.decode('ascii')

        if isinstance(sentence, list):
            sentence = ' '.join(sentence)

        if sentence == '':
            return None

        try:
            sent = Sentence(sentence)
            self.model.embed(sent)
            return sent.embedding.detach().cpu().numpy()
        except TypeError:
            return None
