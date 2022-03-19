import pandas as pd
import stanza

stanza.download('de') #download german language model

nlp = stanza.Pipeline(lang='de', processors='tokenize,lemma,mwt,ner')
filename = "Covid_Korpus_SZ_bereinigt.txt"
with open(filename, 'r') as f:
    doc = nlp(f.read())
print(*[f'entity: {ent.text}\ttype: {ent.type}' for ent in doc.ents], sep='\n')


def word_info_df(doc):
    frequencies = {}
    rows = []
    for sentence in doc.sentences:
        for entity in sentence.entities:
            lemmatizedEntity = ''
            for word in entity.words:
                lemmatizedEntity += word.lemma + ''
            if lemmatizedEntity in frequencies.keys():
                frequencies[lemmatizedEntity] = frequencies[lemmatizedEntity] + 1
            else:
                frequencies[lemmatizedEntity] = 1
    for lemma_2 in frequencies.keys():
        row = {
            "lemma": lemma_2, "loc_frequency": frequencies[lemma_2]
        }
        rows.append(row)
    return pd.DataFrame(rows)


print(word_info_df(doc))
df = pd.DataFrame(word_info_df(doc))
print(df)
df.to_csv(r'C:\Users\Martin\PycharmProjects\Methodenvorlesung\sz_corpus.csv')
