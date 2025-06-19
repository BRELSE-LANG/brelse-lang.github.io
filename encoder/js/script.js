const brailleMap = {
  'A': '100000', 'B': '101000', 'C': '110000', 'D': '110100',
  'E': '100100', 'F': '111000', 'G': '111100', 'H': '101100',
  'I': '011000', 'J': '011100', 'K': '100010', 'L': '101010',
  'M': '110010', 'N': '110110', 'O': '100110', 'P': '111010',
  'Q': '111110', 'R': '101110', 'S': '011010', 'T': '011110',
  'U': '100011', 'V': '101011', 'W': '011101', 'X': '110011',
  'Y': '110111', 'Z': '100111',
  '1': '100000', '2': '101000', '3': '110000', '4': '110100',
  '5': '100100', '6': '111000', '7': '111100', '8': '101100',
  '9': '011000', '0': '011100',
  ' ': '000000'
};

const morseMap = {
  'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..',
  'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
  'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
  'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
  'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
  'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
  'Y': '-.--', 'Z': '--..',
  '1': '.----', '2': '..---', '3': '...--', '4': '....-',
  '5': '.....', '6': '-....', '7': '--...', '8': '---..',
  '9': '----.', '0': '-----',
  ' ': '/'
};

document.getElementById('encodeBtn').addEventListener('click', () => {
  const input = document.getElementById('inputText').value.toUpperCase();
  const showBraille = document.getElementById('showBraille').checked;
  const showMorse = document.getElementById('showMorse').checked;
  const output = document.getElementById('output');
  let result = '';

  for (let char of input) {
    if (!(char in brailleMap)) continue;
    const braille = brailleMap[char];
    const morse = morseMap[char];

    if (showBraille && !showMorse) {
      result += `${char}: ${braille}\n`;
    } else if (!showBraille && showMorse) {
      result += `${char}: ${morse}\n`;
    } else {
      result += `${char}: ${braille} | ${morse}\n`;
    }
  }

  output.textContent = result || 'No valid characters to encode.';
  document.getElementById('downloadBtn').style.display = result ? 'inline-block' : 'none';
});

document.getElementById('downloadBtn').addEventListener('click', () => {
  const output = document.getElementById('output').textContent;
  const blob = new Blob([output], { type: 'text/plain' });
  const url = URL.createObjectURL(blob);
  const a = document.createElement('a');
  a.href = url;
  a.download = 'brelse_encoded_output.txt';
  a.click();
  URL.revokeObjectURL(url);
});
