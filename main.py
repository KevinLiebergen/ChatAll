from config import Config
from openai import OpenAI
from sydney import SydneyClient
from bardapi import Bard, SESSION_HEADERS, BardCookies
import argparse
import logging
import sys
import os

# Logging to file
log_name = 'chatall.logs'
sys.stdout.write("[+] Saving logs in {}\n".format(log_name))

logging.basicConfig(filename=log_name,
                    filemode='w',
                    level=logging.INFO)

# Logging to console
console = logging.StreamHandler()
console.setLevel(logging.INFO)
logging.getLogger('').addHandler(console)

log = logging.getLogger(__name__)


def read_question(path):
    """ Read question from file """
    path_fd = open(path, 'r')
    return path_fd.read()


def ask_chatgpt(question: str, chatgpt_key: str):
    """ Using API, ask chatGPT """
    client = OpenAI(
        api_key=chatgpt_key
    )

    response = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": question,
            }
        ],
        model="gpt-3.5-turbo",
    )

    log.info("ChatGPT")
    log.info(response)


def ask_bing(question):
    """ Using API, ask Bing LLM """

    os.environ["BING_U_COOKIE"] = "<your-cookie>"


def ask_bard(question: str, psid: str, psidcc: str, psidts: str):
    """ Using API, ask Bard LLM """

    cookie_dict = {
        "__Secure-1PSID": psid,
        "__Secure-1PSIDCC": psidcc,
        "__Secure-1PSIDTS": psidts
    }

    bard = BardCookies(cookie_dict=cookie_dict)

    response = bard.get_answer(question)['content']

    log.info("Bard")
    log.info(response)


if __name__ == '__main__':
    argparser = argparse.ArgumentParser()

    argparser.add_argument('-c', '--config', action='store',
                           help='Config file',
                           default='./data/config.ini')

    argparser.add_argument('-q', '--question', action='store',
                           help='Question file',
                           default='./data/question.txt')

    args = argparser.parse_args()

    conf = Config(args.config)

    question = read_question(args.question)
    if not conf.chatgpt_key:
        ask_chatgpt(question=question, chatgpt_key=conf.chatgpt_key)

    if conf.bing_key:
        ask_bing(question)

    if conf.bard_secure_1psid:
        ask_bard(question=question,
                 psid=conf.bard_secure_1psid,
                 psidcc=conf.bard_secure_1psidcc,
                 psidts=conf.bard_secure_1psidts)
