import docx 


def not_used():
    
    wordDoc = docx.Document('POS.docx')

    unuse_word = ['Verb','Noun','Adjective','Adverb']

    for i in range(1,89):
        unuse_word.append(str(i))

    words = []
    for table in wordDoc.tables:
        for row in table.rows:
            for cell in row.cells:
                if cell.text != "":
                    if not any(x in cell.text for x in unuse_word):
                        words.append(cell.text)

    return words                     


if __name__ == "__main__":
    not_used()