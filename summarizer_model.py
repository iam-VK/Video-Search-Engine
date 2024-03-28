from transformers import AutoTokenizer, BartForConditionalGeneration
def summarize(file_path="img2txt.txt"):
    model = BartForConditionalGeneration.from_pretrained("facebook/bart-large-cnn")
    tokenizer = AutoTokenizer.from_pretrained("facebook/bart-large-cnn")

    input_text = ""

    with open(file_path,"r") as file:
        for line in file:
            input_text += line
        file.close()
    print(input_text)

    inputs = tokenizer(input_text, max_length=2048, truncation=True, return_tensors="pt")
    summary_ids = model.generate(inputs["input_ids"], num_beams=2, min_length=70, max_length=250)
    output = tokenizer.batch_decode(summary_ids, skip_special_tokens=True, clean_up_tokenization_spaces=False)[0]
    print(output)