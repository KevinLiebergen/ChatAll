# ChatALL

Ask to ChatGPT, Bing, and Bard at once!

## Activate environment

```bash
$ conda create --name chatall python=3.9
$ conda activate chatall
$ pip3 install -r requirements.txt
```

## config.ini file

Fill the API fields depending on which LLM you want to ask

### ChatGPT

* https://platform.openai.com/api-keys

### Bard

* https://github.com/dsdanielpark/Bard-API#authentication

### Bing

* https://github.com/vsakkas/sydney.py#prerequisites

## Running

Write down your question in `data/question.txt` and execute

```bash
$ python3 main.py
```

Or

```bash
$ python3 main.py -c config.ini
```

Or

```bash
$ python3 main.py -q question_path.txt
```
