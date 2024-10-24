def sentence_split(text):

    from IPython.display import display, HTML

    import re
    sentences = re.split(r'(?<=\.)\s+', text.strip())

    #for i, sentence in enumerate(sentences):
        #print(f"S{i+1} = '''{sentence}'''")

    

    
    # Function to count the number of words in a sentence
    def word_count(sentence):
        return len(sentence.split())
    
    # List to hold the adjusted sentences
    combined_sentences = []
    current_sentence = ""
    
    for sentence in sentences:
        # If current_sentence is empty, start with the current sentence
        if not current_sentence:
            current_sentence = sentence
        else:
            # If the combined sentence so far has less than 20 words, add the next sentence
            if word_count(current_sentence) < 20:
                current_sentence += " " + sentence
            else:
                combined_sentences.append(current_sentence)
                current_sentence = sentence
        
    # Append the last sentence if any remains
    if current_sentence:
        combined_sentences.append(current_sentence)
    
    # Printing each combined sentence with the desired format
    for i, sentence in enumerate(combined_sentences):
        print(f"S{i+1} = '''{sentence}'''")






    output_text = "\n".join([f"S{i+1} = '''{sentence}'''" for i, sentence in enumerate(sentences)])













    

    button_html = f"""
<button onclick="copyToClipboard()">Copy Output</button>
<script>
function copyToClipboard() {{
  const outputText = `{output_text}`;
  const el = document.createElement('textarea');
  el.value = outputText;
  document.body.appendChild(el);
  el.select();
  document.execCommand('copy');
  document.body.removeChild(el);
  alert('Output copied to clipboard');
}}
</script>
"""

    display(HTML(button_html))

# Display the button
    return button_html



def moveVoices(VOICES, CUSTOM_VOICE_NAME = "ABDULLAH"):

    import os 
        
    CUSTOM_VOICE_NAME = "ABDULLAH"
    
    custom_voice_folder = f"tortoise/voices/{CUSTOM_VOICE_NAME}"
    
    # Ensure the directory exists
    os.makedirs(custom_voice_folder, exist_ok=True)
    
    for i, file_path in enumerate(VOICES):
        with open(file_path, 'rb') as source_file:
            file_data = source_file.read()
        with open(os.path.join(custom_voice_folder, f'{i}.wav'), 'wb') as destination_file:
            destination_file.write(file_data)
    



def getAudio(text, tts, CUSTOM_VOICE_NAME, voice_samples, conditioning_latents, preset="fast"):
    
  gen = tts.tts_with_preset(text, voice_samples=voice_samples, conditioning_latents=conditioning_latents,
                            preset=preset)
  torchaudio.save(f'generated-{CUSTOM_VOICE_NAME}.wav', gen.squeeze(0).cpu(), 24000)



VOICES_DIR = "/content/VoiceCloning/input/ABDULLAH_3/"

def getVoiceDir(x):
    VOICES = [VOICES_DIR + f"sample_{i+1}.wav" for i in range(x)]
    return VOICES
