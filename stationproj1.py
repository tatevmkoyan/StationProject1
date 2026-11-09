import random


def hospital_story():
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
  noun4 = input("Input another noun: ")
  adjective3 = input("Input another adjective: ")
  silly_word = input("Input a silly word: ")

  print(
      f"It was about {number} {measure_time} ago when I arrived at the hospital"
      f" in a {transport}. The hospital is a {adjective} place, there are a lot"
      f" of {adjective2} {noun} here. There are nurses here who have {color}"
      f" {body_part}. If someone wants to come into my room I told them that"
      f" they have to {verb} first. I've decorated my room with {number2}"
      f" {noun2}. Today I talked to a doctor and they were wearing a {noun3}"
      f" on their {body_part2}. I heard that all doctors {verb2} {noun4} every"
      f" day for breakfast. The most {adjective3} thing about being in the"
      f" hospital is the {silly_word} {noun}!"
  )


def camping_story():
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

  print(
      f"This weekend I am going camping with {name}. I packed my lantern,"
      f" sleeping bag, and {noun}. I am so {feeling1} to {verb} in a tent. I"
      f" am {feeling2} we might see a {animal}, I hear they're kind of"
      f" dangerous. While we're camping, we are going to hike, fish, and"
      f" {verb2}. I have heard that the {color} lake is great for {verb_ing}."
      f" Then we will {adverb} hike through the forest for {number}"
      f" {measure_time}. If I see a {color2} {animal2} while hiking, I am going"
      f" to bring it home as a pet! At night we will tell {number2}"
      f" {silly_word} stories and roast {noun2} around the campfire!!"
  )


def castle_story():
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

  print(
      f"Dear {name}, I am writing to you from a {adjective} castle in an"
      f" enchanted forest. I found myself here one day after going for a ride"
      f" on a {color} {animal} in {place}. There are {adjective2} {magical1} and"
      f" {adjective3} {magical2} here! In the {room} there is a pool full of"
      f" {noun}. I fall asleep each night on a {noun2} of {noun3} and dream of"
      f" {adjective4} {noun4}. It feels as though I have lived here for {number}"
      f" {measure_time}. I hope one day you can visit, although the only way to"
      f" get here now is {verb_ing} on a {adjective5} {noun5}!!"
  )


def main():
  while True:
    print("Choose a template:")
    print("1 — Hospital Story")
    print("2 — Camping Story")
    print("3 — Castle Story")
    print("4 — Random Template")
    choice = input("Input 1, 2, 3, or 4: ")

    if choice == "4":
      choice = random.choice(["1", "2", "3"])
      print(f"Randomly selected template #{choice}!")

    if choice == "1":
      hospital_story()
      break
    elif choice == "2":
      camping_story()
      break
    elif choice == "3":
      castle_story()
      break

    print("Wrong input, please try again.\n")


if __name__ == "__main__":
  main()
