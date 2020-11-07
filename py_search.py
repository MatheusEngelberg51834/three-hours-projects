def read_file(path):

    '''
    read pdf file with pdfplumber and return a book defaultdict with page index as key
    and page text as value
    '''
    
    if path.endswith('pdf'):
        import pdfplumber
        from collections import defaultdict
        book = defaultdict(list)
        with pdfplumber.open(path) as pdf:
            for page_index, page in enumerate(pdf.pages):
                try:
                    book[page_index] = page.extract_text(x_tolerance=3, y_tolerance=3).replace('\n', ' ')
                except AttributeError:
                    pass
        return book
    else:
        raise TypeError

def tokenize(array):

    '''
    return a set of tokens from a array, use in iterations
    '''

    import nltk
    from nltk.corpus import stopwords

    unsorted_tokens = set()

    for term in array:
        for tokenized_prashe in nltk.word_tokenize(term):
            unsorted_tokens.add(tokenized_prashe)

    try:
        tokens = list(token for token in unsorted_tokens if token not in stopwords.words('english'))
        return tokens
    except:
        print('erro na funcao tokenize')

def ngram(array, start, end):

    '''
    iterate throught terms and split it in range start to end
    '''

    from collections import defaultdict
    try:
        term_ngrammed_term = defaultdict(set)
        if end > start: 
            for phrase in set(array):
                for term in phrase.split():
                    ngrammed_term = set(term[:i] for i in range(start, end + 1) if term[:i])
                    term_ngrammed_term[term] = ngrammed_term
        return term_ngrammed_term
    except TypeError as e:
        return print('please verify the data type of the inputs --> ', e)

def parse_search_query():

    '''
    return parsed input
    '''

    search_query = list(map(str, input().split()))
    return ngram(tokenize(search_query), (len(min(search_query, key=len)) + 1), len(max(search_query, key=len)))
