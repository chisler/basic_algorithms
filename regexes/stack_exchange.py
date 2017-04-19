# <h3><a href="/questions/80405/5v-regulator-power-dissipation" class="question-hyperlink">5V Regulator Power Dissipation</a></h3>
# class="relativetime">11 hours ago</span>

import re

current_question = ''

q = r"/questions/(\d{5})*"
title = r"class=\"question-hyperlink\">(.*)</a>"
time = r"class=\"relativetime\">(.*)</span>"


def readline():
    line = None
    while not line:
        try:
            line = input()
        except:
            break
    return line


def get_by_pattern(line, pattern, storage):
    search = re.search(pattern, line, re.MULTILINE | re.DOTALL)
    if search and search.group(1):
        storage.append(search.group(1))


ids = []
titles = []
times = []

line = readline()
while line:
    get_by_pattern(line, q, ids)
    get_by_pattern(line, title, titles)
    get_by_pattern(line, time, times)
    line = readline()

for i in zip(ids, titles, times):
    print(";".join(i))
