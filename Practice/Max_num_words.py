# Question No : 2
# Maximum Number of Words Found in Sentences
# A sentence is a list of words that are separated by a single space with no leading or trailing spaces.
#
# You are given an array of strings sentences, where each sentences[i] represents a single sentence.
#
# Return the maximum number of words that appear in a single sentence.
# Example 1:
# Input:
from itertools import count

# sentences = ["alice and bob love leetcode", "i think so too", "this is great thanks very much"]
# Output: 6
# Explanation:
# - The first sentence, "alice and bob love leetcode", has 5 words in total.
# - The second sentence, "i think so too", has 4 words in total.
# - The third sentence, "this is great thanks very much", has 6 words in total.
# Thus, the maximum number of words in a single sentence comes from the third sentence, which has 6 words.
#
# Example 2:
# Input: sentences = ["please wait", "continue to fight", "continue to win"]
# Output: 3
# Explanation: It is possible that multiple sentences contain the same number of words.
# In this example, the second and third sentences (underlined) have the same number of words.

# Problem-2:
#
# def max_words(sentences):
#     words_list=(map(lambda x: len(x.split()), sentences))
#     return max(words_list)
#
# sent1 = ["alice and bob love leetcode", "i think so too", "this is great thanks very much"]
# sent2=  ["please wait", "continue to fight", "continue to win"]
# print(max_words(sent1))
# print(max_words(sent2))

import sqlite3

# connecting to the database
connection = sqlite3.connect("gfg.db")

# cursor
crsr = connection.cursor()

# SQL command to create a table in the database
sql_command = """CREATE TABLE emp (
staff_number INTEGER PRIMARY KEY,
fname VARCHAR(20),
lname VARCHAR(30),
gender CHAR(1),
joining DATE);"""

# execute the statement
crsr.execute(sql_command)

# close the connection
connection.close()







