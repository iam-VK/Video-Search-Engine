from transformers import pipeline
def summarize():
    summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
    input_text = ""
    with open("img2txt.txt","r") as file:
        for line in file:
            input_text += line
        file.close()
    print(input_text)

    output = summarizer(input_text, max_length=250, min_length=100, do_sample=False) #130 30
    print(output)