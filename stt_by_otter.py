import os, shutil
import otter_auto
from otter_auto import otter_auto
from jiwer import wer
import subprocess


def remove_line_from_file(filename, line_to_remove, dirpath=''):
    """Remove all occurences of `line_to_remove` from file
    with name `filename`, contained at path `dirpath`.
    If `dirpath` is omitted, relative paths are used."""
    filename = os.path.join(dirpath, filename)
    temp_path = os.path.join(dirpath, 'temp.txt')

    with open(filename, 'r') as f_read, open(temp_path, 'w') as temp:
        for line in f_read:
            if line.strip() == line_to_remove:
                continue
            temp.write(line)

    os.remove(filename)
    os.rename(temp_path, filename)


def stt_by_otter(file_path, wer_standardize=True, wer_words_to_filter = []):
    otter_auto(file_path)
    subprocess.run('bash ./run.sh'+file_path, shell = True, check = True)
    files = os.listdir(os.getcwd()+'\otter_download')
    for i in range(len(files)):
        remove_line_from_file(files[i], 'Transcribed by https://otter.ai',
                                  os.path.join(os.getcwd(),'otter_download'))

    truth = os.path.abspath(os.listdir(os.path.join(os.getcwd(),'otter_download'))+'.txt')
    hypothesis = os.path.join(os.getcwd(), files)[-4:]+'.wav'+'.txt'
    
    a = wer(truth,hypothesis, standardize=wer_standardize, words_to_filter=wer_words_to_filter )
    shutil.rmtree(os.path.join(os.getcwd(), 'otter_download'))
    print('Word error rate: %.4f' %a)



if __name__ == "__main__":
    remove_line_from_file()
    stt_by_otter()



