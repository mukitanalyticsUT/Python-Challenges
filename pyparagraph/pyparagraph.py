import os
import csv
import re

txt_input_path = os.path.join('raw_data','paragraph_1.txt')


with open(txt_input_path, mode='r', newline='') as paragraph:
    reader = paragraph.read()

    sentences_stripped = re.sub('\n', '', reader)
    sentences_split = re.split('\.', sentences_stripped)

    letters_stripped = re.sub("[\., \-')()><\n]", '', reader).replace('"', '')
    letters = list(letters_stripped)

    words_stripped = re.sub("[\.,\-')()><\n]", '', reader).replace('"', '')
    words_split = re.split(' ', words_stripped)



print("\nParagraph Analysis")
print("-" * 40)
print("Approximate Word Count:", len(words_split))
print("Approximate Sentence Count:", len(sentences_split) - 1)
print("Average Letter Count:", round(len(letters_stripped) / len(words_split), 4), "per word")
print("Average Sentence Length:", round(len(words_split) / (len(sentences_split) - 1), 4), "words")
print("\n\n")


# *----------------------*
# |  Output TXT Summary  |
# *----------------------*

#with open(txt_output_path, mode='w', newline='') as summary:
 #   writer = csv.writer(summary)

  #  writer.writerows([
   #     ["Paragraph Analysis for: " + input_file],
    #    ["-" * 40],
     #   ["Approximate Word Count: " + str(len(words_split))],
      #  ["Approximate Sentence Count: " + str(len(sentences_split) - 1)],
       # ["Average Letter Count: " + str(round(len(letters_stripped) / len(words_split), 4)) + " per word"],
       # ["Average Sentence Length: " + str(round(len(words_split) / (len(sentences_split) - 1), 4)) + " words"]
   # ])


