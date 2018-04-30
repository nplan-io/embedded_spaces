from nltk.corpus import webtext
import embeddedspaces.doc2vec
from models.common import make_sentence

raw = webtext.raw('firefox.txt')
sentences = raw.split('\r\n')
d2v = embeddedspaces.doc2vec.Doc2Vec(dm=0, hs=1)
docs = [make_sentence(x) for x in sentences]
d2v.build_vocab(docs)
d2v.train(docs)
