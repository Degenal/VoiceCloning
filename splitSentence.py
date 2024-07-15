def sentence_split(text):
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


    import re
    sentences = re.split(r'(?<=\.)\s+', text.strip())

    for i, sentence in enumerate(sentences):
        print(f"S{i+1} = '''{sentence}'''")

    
    output_text = "\n".join([f"S{i+1} = '''{sentence}'''" for i, sentence in enumerate(sentences)])



# Display the button
    return button_html
    display(HTML(button_html))

