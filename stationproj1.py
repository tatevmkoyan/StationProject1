import random
print("Choose a template:")

choice = input("Input 1, 2, or 3: ")

if choice == "1":
 number = input("Input a number: ")
 measure_time = input("Input a measure of time: ")
 transport = input("Input a mode of transportation: ")
 adjective = input("Input an adjective: ")
 adjective2 = input("Input another adjective: ")
 noun = input("Input a noun: ")
 color = input("Input a color: ")
 body_part = input("Input a part of the body: ")
 verb = input("Input a verb: ")
 number2 = input("Input another number: ")
 noun2 = input("Input another noun: ")
 noun3 = input("Input another noun: ")
 body_part2 = input("Input another part of the body: ")
 verb2 = input("Input another verb: ")
 noun4 = input("Inputpe another noun: ")
 adjective3 = input("Input another adjective: ")
 silly_word = input("Input a silly word: ")

 print("It was about", number, measure_time, "ago when I arrived at the hospital in a", transport + ".",
"The hospital is a", adjective, "place, there are a lot of", adjective2, noun, "here.",
"There are nurses here who have", color, body_part + ".",
"If someone wants to come into my room I told them that they have to", verb, "first.",
"I've decorated my room with", number2, noun2 + ".",
"Today I talked to a doctor and they were wearing a", noun3, "on their", body_part2 + ".",
"I heard that all doctors", verb2, noun4, "every day for breakfast.",
"The most", adjective3, "thing about being in the hospital is the", silly_word, noun + "!")

elif choice == "2":
 name = input("Input a person's name: ")
 noun = input("Input a noun: ")
 feeling1 = input("Input a feeling adjective: ")
 verb = input("Input a verb: ")
 feeling2 = input("Input another feeling adjective: ")
 animal = input("Input an animal: ")
 verb2 = input("Input another verb: ")
 color = input("Input a color: ")
 verb_ing = input("Input a verb ending in 'ing': ")
 adverb = input("Input an adverb ending in 'ly': ")
 number = input("Input a number: ")
 measure_time = input("Input a measure of time: ")
 color2 = input("Input another color: ")
 animal2 = input("Input another animal: ")
 number2 = input("Input another number: ")
 silly_word = input("Input a silly word: ")
 noun2 = input("Input another noun: ")

 print("This weekend I am going camping with", name + ".",
"I packed my lantern, sleeping bag, and", noun + ".",
"I am so", feeling1, "to", verb, "in a tent.",
"I am", feeling2, "we might see a", animal + ", I hear they're kind of dangerous.",
"While we're camping, we are going to hike, fish, and", verb2 + ".",
"I have heard that the", color, "lake is great for", verb_ing + ".",
"Then we will", adverb, "hike through the forest for", number, measure_time + ".",
"If I see a", color2, animal2, "while hiking, I am going to bring it home as a pet!",
"At night we will tell", number2, silly_word, "stories and roast", noun2, "around the campfire!!")

elif choice == "3":
 name = input("Input a person's name: ")
 adjective = input("Input an adjective: ")
 color = input("Input a color: ")
 animal = input("Input an animal: ")
 place = input("Input a place: ")
 adjective2 = input("Input another adjective: ")
 magical1 = input("Input a magical creature (plural): ")
 adjective3 = input("Input another adjective: ")
 magical2 = input("Input another magical creature (plural): ")
 room = input("Input a room in a house: ")
 noun = input("Input a noun: ")
 noun2 = input("Input another noun: ")
 noun3 = input("Input a plural noun: ")
 adjective4 = input("Input another adjective: ")
 noun4 = input("Input another plural noun: ")
 number = input("Input a number: ")
 measure_time = input("Input a measure of time: ")
 verb_ing = input("Input a verb ending in 'ing': ")
 adjective5 = input("Input another adjective: ")
 noun5 = input("Input another noun: ")


 print("Dear", name + ",",
"I am writing to you from a", adjective, "castle in an enchanted forest.",
"I found myself here one day after going for a ride on a", color, animal, "in", place + ".",
"There are", adjective2, magical1, "and", adjective3, magical2, "here!",
"In the", room, "there is a pool full of", noun + ".",
"I fall asleep each night on a", noun2, "of", noun3,
"and dream of", adjective4, noun4 + ".",
"It feels as though I have lived here for", number, measure_time + ".",
"I hope one day you can visit, although the only way to get here now is",
verb_ing, "on a", adjective5, noun5 + "!!")
