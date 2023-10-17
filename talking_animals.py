def speak(animal="dog"):
    sounds = {"dog": "woof", "pig": "oink", "duck": "quack", "cat": "meow"}
    sound = sounds.get(animal)
    if sound:
        return sound
    return "?"

print(speak())  # "woof"
print(speak("pig"))  # "oink"
print(speak("duck"))  # "quack"
print(speak("cat"))  # "meow"
print(speak("dog"))  # "woof"
print(speak("banana"))  # "?"
