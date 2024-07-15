def sentence_split(text):

    from IPython.display import display, HTML

    import re
    sentences = re.split(r'(?<=\.)\s+', text.strip())

    for i, sentence in enumerate(sentences):
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
    

def GetVoicesDir(VOICES_DIR):
    VOICES = [VOICES_DIR + "sample_1.wav",
          VOICES_DIR + "sample_2.wav",
          VOICES_DIR + "sample_3.wav",
          VOICES_DIR + "sample_4.wav",
          VOICES_DIR + "sample_5.wav"
         ]