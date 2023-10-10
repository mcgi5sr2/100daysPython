#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
with open("Input/Names/invited_names.txt") as file:
    file_names = file.readlines()
file_names = [f.strip() for f in file_names]
print(file_names)

for item, index in enumerate(file_names):
    with open("Input/Letters/starting_letter.txt", mode="r") as file:
        file_letter = file.readlines()
    file_letter[0] = file_letter[0].replace("[name]", file_names[item])
    with open(f"ReadyToSend/{file_names[item]}", mode="w") as file:
        file.write(''.join(file_letter))
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp