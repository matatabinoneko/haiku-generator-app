import subprocess
import logging
import sys
from typing import List
import MeCab
import random
import re

logger = logging.getLogger("app")

m = MeCab.Tagger('-Owakati')
def word_tokenizer(x): return m.parse(x).rstrip("\n").split()
def char_tokenizer(x): return list(x)


japanese_pattern = re.compile(r'[ぁ-んァ-ン一-龥]+')

dup_threshold = 0.8


def calc_score(haiku: str) -> float:
    '''
    重複度スコア計算
    '''
    word_tokens = word_tokenizer(haiku)
    char_tokens = char_tokenizer(haiku)
    word_score = len(set(word_tokens)) / len(word_tokens)
    char_score = len(set(char_tokens)) / len(char_tokens)
    score = (word_score + char_score)/2
    return score, word_score, char_score


def generate_haiku(key1: str, key2: str, key3: str, prefix: str) -> str:
    # 日本語判定 + 文字数判定
    if not is_japanese(key1) or not is_japanese(key2) or not is_japanese(key3) or not is_japanese(prefix) or 5 < len(prefix):
        raise ValueError

    key1 = ' '.join(list(key1))
    key2 = ' '.join(list(key2))
    key3 = ' '.join(list(key3))
    prefix = ' '.join(list(prefix))
    inputs = []
    for w in [key1, key2, key3]:
        if w != '':
            inputs.append(w)
            inputs.append("[SEP]")
    if prefix != '':
        inputs.append(prefix)

    inputs = ' '.join(inputs)

    logger.debug(inputs)

    # subprocessでinteractive.shを実行
    cmd0 = f"echo '{inputs}'"
    cmd1 = '|bash generator/interactive.sh'
    cmd2 = "| grep output:"
    outputs = subprocess.run(f"{cmd0} {cmd1} {cmd2}",
                             shell=True, stdout=subprocess.PIPE)
    outputs = outputs.stdout.decode('utf8').strip().split('\n')

    # output:Array(ppl, 俳句)
    outputs = list(map(lambda x: x.split('\t'), outputs))
    logger.debug(outputs)

    suffix = select_best_haiku_from_candidate(outputs)
    haiku = f"{prefix}{suffix}".replace(' ', '')

    return haiku


def run_and_capture(cmd: str) -> str:
    '''
    :param cmd: str 実行するコマンド.
    :rtype: str
    :return: 標準出力.
    '''
    # ここでプロセスが (非同期に) 開始する.
    proc = subprocess.Popen(
        cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    buf = []

    while True:
        # バッファから1行読み込む.
        line = proc.stdout.readline()
        buf.append(str(line))
        sys.stdout.write(str(line))

        # バッファが空 + プロセス終了.
        if not line and proc.poll() is not None:
            break
    return ''.join(buf)


def select_best_haiku_from_candidate(haiku_list: List) -> str:
    valid_haiku_list = []
    for ppl, haiku in haiku_list:
        # 重複度スコアを計算
        dup_score, _, _ = calc_score(haiku)
        if dup_score < dup_threshold:
            valid_haiku_list.append(haiku)
    if valid_haiku_list:
        haiku = random.choice(valid_haiku_list)
    else:
        haiku = random.choice(haiku_list)[1]

    return haiku


def is_japanese(word):
    '''
    wordが空文字または日本語であればtrueを返す
    '''
    if word == '' or japanese_pattern.fullmatch(word):
        return True
    else:
        return False
