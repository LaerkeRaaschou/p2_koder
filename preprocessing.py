import pandas as pd
import nltk
import lemmy
from nltk.corpus import stopwords

try:
    nltk.data.find('corpora/stopwords')
    print("Stopwords are already downloaded.")
except LookupError:
    print("Stopwords not found. Downloading now...")
    nltk.download('stopwords')

def lemmatizer(word):
    lemmatizer = lemmy.load('da')
    lemmas = lemmatizer.lemmatize("", word)

    if len(lemmas) == 1:
        return lemmas[0]
    elif word in lemmas:
        return word
    elif len(lemmas) == 3:
        return lemmas[0]
    else:
        return lemmas[-1]

def holdop_words():
    stopwords_spacy = ['henover', 'hvori', 'nemlig', 'lave', 'gjort', 'heller', 'uden', 
                 'hvordan', 'men', 'egen', 'sige', 'dens', 'hvorimod', 'endnu', 
                 'herpå', 'nogen', 'alt', 'dette', 'som', 'for', 'af', 'undtagen', 
                 'gøre', 'kun', 'derefter', 'man', 'selvom', 'sig', 'ene', 'jeres', 
                 'nu', 'jeg', 'hende', 'intet', 'vores', 'hvornår', 'mere', 'de', 
                 'sammen', 'hvad', 'først', 'dig', 'ens', 'mit', 'lige', 'nok', 'ville', 
                 'hvilkes', 'derfor', 'kunne', 'alle', 'begge', 'til', 'enhver', 'her', 
                 'gjorde', 'om', 'det', 'end', 'herefter', 'dem', 'jo', 'gør', 'ingen', 
                 'den', 'skal', 'flest', 'bag', 'efter', 'lav', 'må', 'altid', 'syntes', 
                 'vær', 'kom', 'hvorhen', 'aldrig', 'der', 'hvorefter', 'før', 'igennem', 
                 'overalt', 'alene', 'deri', 'eneste', 'hvilke', 'imens', 'sådan', 'ikke', 
                 'ligesom', 'mig', 'derpå', 'med', 'havde', 'da', 'imod', 'ved', 'enten', 
                 'og', 'god', 'indtil', 'vore', 'mens', 'gennem', 'næsten', 'lad', 'ny', 
                 'dermed', 'nær', 'hvorfor', 'dine', 'omkring', 'os', 'nogensinde', 'mest', 
                 'bliver', 'en', 'forrige', 'han', 'ud', 'dog', 'hvilken', 'hvem', 'via', 
                 'ind', 'min', 'foran', 'være', 'eller', 'er', 'fleste', 'blive', 'imellem', 
                 'udover', 'mindre', 'hen', 'selv', 'tidligere', 'senere', 'ham', 'have', 
                 'lille', 'hermed', 'hvis', 'hvorved', 'ellers', 'hver', 'hel', 'hendes', 
                 'kan', 'noget', 'under', 'burde', 'tit', 'har', 'flere', 'over', 'meget', 
                 'lavet', 'derfra', 'deres', 'næste', 'nogle', 'andre', 'længere', 'stadig', 
                 'siden', 'alligevel', 'ned', 'nyt', 'få', 'i', 'blandt', 'din', 'hvorfra', 
                 'op', 'gørende', 'mange', 'så', 'vi', 'været', 'igen', 'på', 'synes', 'blev', 
                 'vil', 'ses', 'mine', 'var', 'denne', 'måske', 'hans', 'også', 'samme', 'andet', 
                 'at', 'således', 'temmelig', 'et', 'heri', 'lidt', 'tilbage', 'derved', 'du', 
                 'hvor', 'skulle', 'øvrigt', 'fordi', 'hun', 'bør', 'langs', 'fra', 'anden', 
                 'mellem', 'allerede', 'disse', 'kommer', 'jer', 'mindst']

def preprocessing(description):
    ''' Tokenization, lemmatization, stopwords '''
    hold_words = stopwords.words('danish')

    words = str(description).split()
    words = [word.lower() for word in words if word.lower() not in hold_words]

    new_description = ""
    for word in words:
        new_description += ' '
        new_word = lemmatizer(word)
        new_description += new_word

    return new_description

def main():
    ''' main function '''
    data = pd.read_csv('/Users/laerkeraaschou/Desktop/semester2/projekt/p2_koder/data/Kundefejl_JA_NEJ.csv')
    categories = ['Instruction', 'Short_description', 'Technicians_description']

    for category in categories:
        for description in data[category]:
            new_description = preprocessing(description)
            print(new_description)

if __name__ == '__main__':
    main()