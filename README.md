# ECPS-207---Security-and-Privacy-in-Cyber-Physical-Systems
Assignments for course ECPS 207 relating cryptography and network security

Write a program which implements encryption using the Vigenere Cipher. 
Arguments - The program should take three command-line arguments. The first argument is the filename of a file containing the plaintext. The second argument is the name of a file where the ciphertext will be written. The third argument is a key to be used for encryption. 
Output - The program should create a file, with the appropriate name, containing the ciphertext. The program should print nothing to the screen.

Write a program which implements decryption using the Vigenere Cipher. 
Arguments - The program should take three command-line arguments. The first argument is the filename of a file containing the ciphertext. The second argument is the name of a file where the plaintext will be written. The third argument is a key to be used for decryption.
Output - The program should create a file, with the appropriate name, containing the plaintext. The program should print nothing to the screen.

Write a program which cracks the Vigenere Cipher by discovering the key from the ciphertext, without seeing the corresponding plaintext. In order to accomplish this, your program will use a hint word: a single word which is known to be in the plaintext, and which is at least as long as the key.
Arguments - The program should take two command-line arguments, 1) the name of the file containing the ciphertext, and 2) the hint word. 
Output - The program should print the key on the screen. 


These are some assumptions about the plaintext and the key.

- Each word in the plaintext must be a word in the English language.
- The plaintext must be sufficiently long, containing at least 100 words.
- Each word in the plaintext must contain only lowercase, alphabetic characters.
- The key must contain only lowercase, alphabetic characters.
- The key must contain no spaces; it is a single word.
- Spaces will almost certainly be included in the the plaintext, but the spaces should NOT be encrypted and they will 
  appear as-is, in the ciphertext. For example, let's say that we have plaintext "attack at dawn". This string has 3 words,
  including 12 non-space characters and 2 spaces. The ciphertext for this plaintext would also have 3 words, including
  2 spaces and 12 non-space characters. However, the non-space characters would be different because they are
  substituted using the Vigenere encryption algorithm. So if the key is "lemon" then the ciphertext would be "lxfopv ef
  rnhr".
  
  Hint:
  
  Part of this will likely be trial and error. You will need to try a small number of possible keys to see if they are correct.
  You will need to use a list of words in English to check if your decrypted message is composed of only words in English.
  You will need to find a list of English words online for that purpose.
  
