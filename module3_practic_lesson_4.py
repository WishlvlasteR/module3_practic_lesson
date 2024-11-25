def single_root_words(root_word,*other_words):
    # Пустой список для подходящих слов
    same_words = []
    # Перебираем все слова из *other_words
    for i in other_words:
    # Проверяем root_word и *other_word на похожие слова
        if root_word.lower() in i.lower() or i.lower() in root_word.lower():
            same_words.append(i)
    # Возвращаем итоговый список
    return same_words
print(single_root_words('Hello','hello','llo','asd','home','HELLO',''))
print(single_root_words('Elephant','Sas','Phanta','phantomas','ever','ant','elephan'))