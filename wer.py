import os
from jiwer import wer
from otter_auto import otter_auto
from stt_by_otter import remove_line_from_file


def stt_by_otter(otter_path, stt_path, wer_standardize = True, wer_words_to_filter = []):
    """
    otter_path - path to otter transcripts (.txt)
    stt_path - path to stt output (.txt)
    wer_standardize - preprocessing wer function; True/False; "he's -> he; let's -> let" if True
    wer_word_to_filter - preprocessing wer function;
            wer_words_to_filter = ['Yeah'] -> "Yeah about the bug" ~ "about the bug"
    """


    model_dir = stt_path
    model_data = os.listdir(model_dir)

    otter_dir = otter_path
    otter_data = os.listdir(otter_dir)

    stt = []
    otter = []

    for i in range(len(model_data)):
        with open(os.path.join(model_dir,model_data[i]), 'r') as f1:
            test = f1.read()
            stt.append(test)
    for i in range(len(otter_data)):
        with open(os.path.join(otter_dir,otter_data[i]), 'r') as f2:
            original = f2.read()
            otter.append(original)


    wer_stt = wer(otter, stt, standardize = wer_standardize, words_to_filter= wer_words_to_filter)
    print(wer_stt)



if __name__ == "__main__":
 stt_by_otter()


#testing
filepath = r'C:\Users\milic\Desktop\wave\originals\A ballet interview with Roberto Bolle.wav'



